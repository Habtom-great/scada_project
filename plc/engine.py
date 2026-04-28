# plc/engine.py (or inside consumer)

import time

PLC = {
    "start": False,
    "stop": True,
    "overload": False,

    "m1": False,
    "m2": False,
    "m3": False,

    "t1_start": None,
    "t2_start": None,
    "t3_start": None,

    "t1": 0,
    "t2": 0,
    "t3": 0,

    "seal": False,
    "events": []
}