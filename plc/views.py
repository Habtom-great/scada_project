from django.shortcuts import render

# Create your views here.
import time
from django.http import JsonResponse

# ================= PLC MEMORY =================
PLC = {
    "start": False,
    "stop": True,
    "seal": False,          # latch bit (M0.0 equivalent)
    "motor": False,
    "overload": False,
    "ton_start_time": None,
    "timer": 0.0,
    "ton_delay": 3.0,
    "events": []
}

# ================= LOG FUNCTION =================
def log(msg):
    PLC["events"].append(msg)
    PLC["events"] = PLC["events"][-10:]

# ================= PLC SCAN (REAL LOGIC) =================
def scan():
    # ---------------- SEAL-IN CIRCUIT ----------------
    if PLC["start"] and not PLC["stop"] and not PLC["overload"]:
        PLC["seal"] = True

    if PLC["stop"] or PLC["overload"]:
        PLC["seal"] = False
        PLC["motor"] = False
        PLC["ton_start_time"] = None
        PLC["timer"] = 0

    # ---------------- TON TIMER ----------------
    if PLC["seal"]:
        if PLC["ton_start_time"] is None:
            PLC["ton_start_time"] = time.time()

        PLC["timer"] = time.time() - PLC["ton_start_time"]

        if PLC["timer"] >= PLC["ton_delay"]:
            PLC["motor"] = True
            log("MOTOR RUN")

    else:
        PLC["ton_start_time"] = None
        PLC["timer"] = 0

# ================= API =================
def status(request):
    scan()
    return JsonResponse(PLC)

def start(request):
    PLC["start"] = True
    PLC["stop"] = False
    log("START pressed")
    return JsonResponse({"ok": True})

def stop(request):
    PLC["stop"] = True
    PLC["start"] = False
    log("STOP pressed")
    return JsonResponse({"ok": True})

def overload(request):
    PLC["overload"] = True
    log("OVERLOAD TRIP")
    return JsonResponse({"ok": True})

def reset(request):
    PLC.update({
        "start": False,
        "stop": True,
        "seal": False,
        "motor": False,
        "overload": False,
        "ton_start_time": None,
        "timer": 0
    })
    log("SYSTEM RESET")
    return JsonResponse({"ok": True})
def home(request):
    return render(request, "index.html")