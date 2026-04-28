
# Create your views here.
import time

from django.http import JsonResponse
from django.shortcuts import render

# ================= PLC MEMORY =================
PLC = {
    # COMMANDS
    "start": False,
    "stop": True,

    # MOTORS
    "M1": False,
    "M2": False,
    "M3": False,

    # INTERNAL
    "seal": False,

    # TIMERS
    "t1_start": None,
    "t2_start": None,
    "t3_start": None,
    "t1": 0.0,
    "t2": 0.0,
    "t3": 0.0,
    "delay": 3.0,  # seconds

    # SAFETY
    "overload": False,

    # LOG
    "events": []
}

# ================= LOG =================
def log(msg):
    PLC["events"].append(f"{time.strftime('%H:%M:%S')} - {msg}")
    PLC["events"] = PLC["events"][-25:]

# ================= PLC SCAN =================
def scan():
    # --- SAFETY ---
    if PLC["stop"] or PLC["overload"]:
        PLC["seal"] = False
        PLC["M1"] = PLC["M2"] = PLC["M3"] = False
        PLC["t1_start"] = PLC["t2_start"] = PLC["t3_start"] = None
        PLC["t1"] = PLC["t2"] = PLC["t3"] = 0.0
        return

    # --- SEAL-IN ---
    if PLC["start"]:
        PLC["seal"] = True

    if not PLC["seal"]:
        return

    now = time.time()

    # ===== MOTOR 1 =====
    if PLC["t1_start"] is None:
        PLC["t1_start"] = now
    PLC["t1"] = now - PLC["t1_start"]

    if PLC["t1"] >= PLC["delay"]:
        if not PLC["M1"]:
            log("M1 STARTED")
        PLC["M1"] = True

    # ===== MOTOR 2 =====
    if PLC["M1"]:
        if PLC["t2_start"] is None:
            PLC["t2_start"] = now
        PLC["t2"] = now - PLC["t2_start"]

        if PLC["t2"] >= PLC["delay"]:
            if not PLC["M2"]:
                log("M2 STARTED")
            PLC["M2"] = True

    # ===== MOTOR 3 =====
    if PLC["M2"]:
        if PLC["t3_start"] is None:
            PLC["t3_start"] = now
        PLC["t3"] = now - PLC["t3_start"]

        if PLC["t3"] >= PLC["delay"]:
            if not PLC["M3"]:
                log("M3 STARTED")
            PLC["M3"] = True


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
    log("⚠ OVERLOAD TRIPPED")
    return JsonResponse({"ok": True})

def reset(request):
    PLC.update({
        "start": False,
        "stop": True,
        "seal": False,
        "M1": False,
        "M2": False,
        "M3": False,
        "overload": False,
        "t1_start": None,
        "t2_start": None,
        "t3_start": None,
        "t1": 0.0,
        "t2": 0.0,
        "t3": 0.0
        
    })
    
    log("SYSTEM RESET")
    return JsonResponse({"ok": True})

def home(request):
    return render(request, "index.html")
