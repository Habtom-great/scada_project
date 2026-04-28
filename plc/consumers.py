import json
import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer


class PLCConsumer(AsyncWebsocketConsumer):

    # ================= CONNECT =================
    async def connect(self):
        await self.accept()

        # 🔴 PLC MEMORY (Industrial model)
        self.memory = {
            "I": {
                "START": False,
                "STOP": False,
                "RESET": False
            },
            "Q": {
                "M1": False,
                "M2": False,
                "M3": False
            },
            "M": {
                "RUN": False,
                "STEP": 0
            },
            "T": {
                "T1": 0.0,
                "T2": 0.0,
                "T3": 0.0
            }
        }

        self.running = True
        self.scan_task = asyncio.create_task(self.scan_cycle())

    # ================= DISCONNECT =================
    async def disconnect(self, close_code):
        self.running = False

        if hasattr(self, "scan_task"):
            self.scan_task.cancel()

    # ================= RECEIVE (HMI → PLC INPUTS) =================
    async def receive(self, text_data):
        data = json.loads(text_data)
        cmd = data.get("cmd")

        if cmd == "start":
            self.memory["I"]["START"] = True

        elif cmd == "stop":
            self.memory["I"]["STOP"] = True

        elif cmd == "reset":
            self.memory["I"]["RESET"] = True

    # ================= LADDER LOGIC ENGINE =================
    def ladder_logic(self):
        I = self.memory["I"]
        Q = self.memory["Q"]
        M = self.memory["M"]
        T = self.memory["T"]

        # ================= RESET =================
        if I["RESET"]:
            M["RUN"] = False
            M["STEP"] = 0

            Q["M1"] = Q["M2"] = Q["M3"] = False
            T["T1"] = T["T2"] = T["T3"] = 0.0

            I["START"] = False
            I["STOP"] = False
            I["RESET"] = False

        # ================= START =================
        if I["START"]:
            M["RUN"] = True
            I["START"] = False

        # ================= STOP =================
        if I["STOP"]:
            M["RUN"] = False
            M["STEP"] = 0

            Q["M1"] = Q["M2"] = Q["M3"] = False
            T["T1"] = T["T2"] = T["T3"] = 0.0

            I["STOP"] = False

        # ================= STEP 0 → M1 =================
        if M["RUN"] and M["STEP"] == 0:
            Q["M1"] = True
            T["T1"] += 0.2

            if T["T1"] > 3:
                M["STEP"] = 1

        # ================= STEP 1 → M2 (INTERLOCK M1) =================
        if M["STEP"] == 1 and Q["M1"]:
            Q["M2"] = True
            T["T2"] += 0.2

            if T["T2"] > 3:
                M["STEP"] = 2

        # ================= STEP 2 → M3 (INTERLOCK M2) =================
        if M["STEP"] == 2 and Q["M2"]:
            Q["M3"] = True
            T["T3"] += 0.2

    # ================= SCAN CYCLE (PLC CPU LOOP) =================
    async def scan_cycle(self):
        try:
            while self.running:

                # 1️⃣ INPUT SCAN (from receive)

                # 2️⃣ LOGIC SCAN
                self.ladder_logic()

                # 3️⃣ OUTPUT SCAN (to SCADA HMI)
                await self.send(text_data=json.dumps({
                    "M1": self.memory["Q"]["M1"],
                    "M2": self.memory["Q"]["M2"],
                    "M3": self.memory["Q"]["M3"],
                    "RUN": self.memory["M"]["RUN"],
                    "STEP": self.memory["M"]["STEP"],
                    "T1": round(self.memory["T"]["T1"], 2),
                    "T2": round(self.memory["T"]["T2"], 2),
                    "T3": round(self.memory["T"]["T3"], 2)
                }))

                await asyncio.sleep(0.2)

        except asyncio.CancelledError:
            pass