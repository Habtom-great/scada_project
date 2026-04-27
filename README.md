# 🏭 Industrial SCADA HMI System (Django PLC Simulator)

A real-time **Industrial SCADA (Supervisory Control and Data Acquisition)** simulation system built with **Django**, implementing core PLC concepts such as **TON timer, seal-in circuit, overload protection, and HMI visualization**.

This project simulates how real industrial automation systems behave in factories, including motor control logic and SCADA-style monitoring.

---

## ⚙️ Features

### 🧠 PLC Logic Engine
- Seal-in (self-holding circuit)
- TON (On-delay timer)
- Motor start/stop logic
- Overload protection
- Real-time scan cycle simulation

### 🖥️ SCADA HMI Dashboard
- Live motor status (ON/OFF lamp indicator)
- Real-time timer display
- Overload alarm system
- Event log (history tracking)
- Ladder diagram visualization (basic)

### 📡 Real-Time Communication
- Django API-based PLC status endpoint
- Auto-refresh HMI every 0.5 seconds
- Simulated PLC scan cycle

---

## 🏗️ Project Structure


scada_project/
│
├── scada_project/ # Django project settings
├── plc/ # PLC logic app
│ ├── views.py # PLC engine (scan + logic)
│ ├── urls.py
│
├── templates/ # SCADA HMI UI
│ └── index.html
│
├── static/ # CSS / JS (optional)
├── manage.py


---

## 🔌 PLC Logic Description

### 🟢 Seal-in Circuit
Keeps motor ON after START is pressed until STOP or OVERLOAD is triggered.

### ⏱️ TON Timer (3s delay)
Motor turns ON only after 3 seconds of continuous START condition.

### 🚨 Overload Protection
Immediately stops motor and resets system when triggered.

---

## 🖥️ HMI Preview

### Dashboard Includes:
- Motor Status Indicator (Green/Red Lamp)
- Timer Display (TON counter)
- Overload Alarm
- Event Log Window
- Ladder Diagram Simulation

---

## 🚀 How to Run

### 1. Clone Project
```bash
git clone https://github.com/Habtom-great/scada_project.git
cd scada_project
2. Create Virtual Environment
python3 -m venv venv
source venv/bin/activate   # Mac/Linux
3. Install Django
pip install django
4. Run Migrations
python manage.py migrate
5. Start Server
python manage.py runserver
6. Open SCADA HMI
http://127.0.0.1:8000/
📡 API Endpoints
Endpoint	Description
/plc/status/	Get PLC live status
/plc/start/	Start motor sequence
/plc/stop/	Stop motor
/plc/overload/	Trigger alarm
/plc/reset/	Reset system
🧠 Industrial Concepts Used
PLC Scan Cycle
Ladder Logic Simulation
Timer ON Delay (TON)
Seal-in Circuit (Latch)
SCADA HMI Design
Industrial Alarm Handling
🎯 Future Improvements
Multi-motor control system (M1, M2, M3)
Data historian (SQLite logging)
Graphical trend charts
User login (Engineer / Operator mode)
Mobile SCADA dashboard
MQTT / IoT integration
👨‍💻 Author

Habtom A.
Electrical Engineer | Industrial Automation & Software Developer

📌 License

This project is for educational and industrial training purposes.

⭐ If you like this project

Give it a ⭐ on GitHub and follow for more industrial automation systems.


---

# 🚀 What you achieved

You now have a **real industrial-grade SCADA portfolio project**:

✔ PLC simulation engine  
✔ HMI dashboard  
✔ Ladder logic visualization  
✔ Industrial timing + safety logic  
✔ API-based SCADA system  

This is already at **junior automation engineer portfolio level**.

---

If you want next upgrade, just say:

👉 **“:contentReference[oaicite:0]{index=0}”**