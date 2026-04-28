# 🏭 Industrial SCADA HMI System (Django PLC Simulator)

A real-time **Industrial SCADA (Supervisory Control and Data Acquisition)** simulation platform built with **Django**.  
This system demonstrates core **PLC automation principles** such as ladder logic execution, TON timers, seal-in circuits, overload protection, and SCADA HMI visualization.

It simulates real factory automation behavior including motor sequencing, process control, and industrial monitoring dashboards.

---

## ⚙️ Features

### 🧠 PLC Logic Engine
- Seal-in (self-holding / latch circuit)
- TON (On-delay timer simulation)
- Sequential motor control (M1 → M2 → M3)
- Overload protection and system trip handling
- Continuous PLC scan cycle simulation

### 🖥️ SCADA HMI Dashboard
- Real-time motor status (ON/OFF indicators)
- Live timer display (T1, T2, T3)
- Overload alarm system
- Event log with timestamps
- Ladder logic visualization
- Process schematic diagram (industrial flow)

### 📡 Real-Time Communication
- REST API-based PLC communication
- Auto-refresh SCADA dashboard
- JSON data exchange between backend and frontend
- Simulated PLC scan cycle engine

---

## 🏗️ Project Structure


scada_project/
│
├── scada_project/ # Django configuration
│ ├── settings.py
│ ├── asgi.py
│ ├── urls.py
│
├── plc/ # PLC simulation engine
│ ├── views.py # PLC logic + API endpoints
│ ├── consumers.py # WebSocket upgrade ready
│ ├── engine.py # Ladder logic engine
│ ├── routing.py
│
├── templates/ # SCADA HMI UI
│ └── index.html
│
├── static/ # CSS / JS assets (optional)
├── manage.py


---

## 🔌 PLC Logic Description

### 🟢 Seal-in Circuit (Latch Logic)
Maintains motor RUN state after START is pressed until STOP or OVERLOAD is triggered.

### ⏱️ TON Timer (On-Delay)
Each motor starts sequentially after a predefined delay, simulating industrial automation behavior.

### 🚨 Overload Protection
Immediately stops all motors and resets system outputs when triggered.

---

## 🖥️ SCADA Dashboard Includes

- ⚙ Motor status indicators (M1, M2, M3)
- ⏱ Real-time timer values
- ⚠ Overload alarm system
- 📜 Event log with timestamps
- 🧭 Process schematic flow diagram
- 🔌 Ladder logic visualization panel

---

## 🚀 Installation & Setup

### 1. Clone Repository
```bash
git clone https://github.com/Habtom-great/scada_project.git
cd scada_project
2. Create Virtual Environment
python3 -m venv venv
source venv/bin/activate   # Mac/Linux
3. Install Dependencies
pip install django
pip install channels
4. Run Migrations
python manage.py migrate
5. Start Server
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
🧠 Industrial Concepts Used
PLC Scan Cycle Simulation
Ladder Logic Execution
TON (On-Delay Timer)
Seal-in Circuit (Latch Logic)
Motor Interlocking System
SCADA HMI Architecture
Industrial Alarm Handling
🎯 Future Improvements
Multi-motor conveyor system
Real-time WebSocket SCADA (Django Channels)
React-based industrial HMI dashboard
Data historian (SQLite logging)
Trend charts (motor runtime & production data)
Role-based access (Operator / Engineer)
MQTT / IoT integration
Drag & drop ladder editor
👨‍💻 Author

Habtom A.
Electrical Engineer | Industrial Automation Developer | SCADA & PLC Systems Designer

📌 License

This project is for educational and industrial training purposes only.

⭐ Project Value

This project demonstrates:

✔ Real PLC simulation engine
✔ Industrial SCADA HMI design
✔ Ladder logic fundamentals
✔ Automation system architecture
✔ Full-stack industrial control simulation

👉 Suitable for automation engineer portfolio / SCADA developer showcase


---

If you want next upgrade, I can help you build:

👉 :contentReference[oaicite:0]{index=0}  
👉 :contentReference[oaicite:1]{index=1}  
👉 :contentReference[oaicite:2]{index=2}

Just say:
**“upgrade to React SCADA digital twin”**
