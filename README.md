🏭 Industrial SCADA HMI System (Django PLC Simulator)

A real-time Industrial SCADA (Supervisory Control and Data Acquisition) simulation platform built with Django.
It demonstrates core PLC automation principles including ladder logic execution, TON timers, seal-in circuits, overload protection, and HMI visualization.

This project simulates how industrial control systems operate in real manufacturing environments such as conveyor systems, motor control panels, and factory automation lines.

⚙️ Features
🧠 PLC Logic Engine
Seal-in (self-holding / latch circuit)
TON (On-delay timer simulation)
Sequential motor control logic
Overload protection & system trip handling
Continuous PLC scan cycle simulation
🖥️ SCADA HMI Dashboard
Real-time motor status (ON/OFF indicators)
Live timer visualization (T1, T2, T3)
Overload alarm system with trip indication
Event log with timestamp history
Ladder logic visualization (simplified industrial format)
Process schematic flow representation
📡 Real-Time Communication
REST API-based PLC communication layer
Auto-refresh HMI dashboard (real-time simulation)
PLC scan cycle executed in backend loop
JSON-based data exchange between backend and UI
🏗️ Project Structure
scada_project/
│
├── scada_project/        # Django project configuration
│   ├── settings.py
│   ├── asgi.py
│   ├── urls.py
│
├── plc/                  # PLC simulation engine
│   ├── views.py         # API + PLC logic controller
│   ├── consumers.py     # (optional WebSocket SCADA upgrade)
│   ├── engine.py        # Ladder logic engine (future upgrade)
│   ├── routing.py
│
├── templates/           # SCADA HMI interface
│   └── index.html
│
├── static/              # CSS / JS assets (optional)
├── manage.py
🔌 PLC Logic Description
🟢 Seal-in Circuit (Latch Logic)

Maintains motor RUN state after START is pressed until STOP or OVERLOAD is activated.

⏱️ TON Timer (On-Delay)

Each motor starts after a defined delay, simulating industrial sequential control.

🚨 Overload Protection

Triggers an immediate system shutdown and resets all outputs for safety compliance.

🖥️ HMI Dashboard Overview

The SCADA interface includes:

⚙ Motor status indicators (M1, M2, M3)
⏱ Real-time timer display (TON counters)
⚠ Overload alarm system
📜 Event log with timestamps
🧭 Process flow schematic diagram
🔌 Ladder logic visualization panel
🚀 Installation & Setup
1. Clone Repository
git clone https://github.com/Habtom-great/scada_project.git
cd scada_project
2. Create Virtual Environment
python3 -m venv venv
source venv/bin/activate   # Mac/Linux
3. Install Dependencies
pip install django
pip install channels
4. Run Database Migrations
python manage.py migrate
5. Start Development Server
python manage.py runserver
6. Open SCADA Dashboard
http://127.0.0.1:8000/
📡 API Endpoints
Endpoint	Description
/plc/status/	Get real-time PLC state
/plc/start/	Start motor sequence
/plc/stop/	Stop system
/plc/overload/	Trigger overload alarm
/plc/reset/	Reset PLC system
🧠 Industrial Concepts Implemented
PLC Scan Cycle Simulation
Ladder Logic Execution Model
TON (On-Delay Timer Function)
Seal-in / Latching Circuit
Motor Interlocking Logic
SCADA HMI Architecture
Industrial Alarm Handling System
🎯 Future Improvements (Roadmap)
Multi-line factory system (conveyor + pumps + tanks)
Real-time WebSocket SCADA (Django Channels)
React-based industrial HMI dashboard
Historical data logging (SCADA historian)
Trend charts (motor runtime, production data)
Role-based access (Operator / Engineer / Admin)
MQTT / IoT integration for real devices
PLC function block editor (drag & drop ladder editor)
👨‍💻 Author

Habtom A.
Electrical Engineer | Industrial Automation Developer | SCADA & PLC Systems Designer

📌 License

This project is intended for educational and industrial training purposes.

⭐ Project Value

This project demonstrates:

✔ Real PLC simulation logic
✔ Industrial SCADA HMI design
✔ Ladder logic fundamentals
✔ Automation system architecture
✔ Backend + frontend industrial integration

👉 Suitable for portfolio (automation engineer / SCADA developer role)
