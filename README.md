☕ University Cafeteria Simulation
This project is a discrete event simulation designed to model the flow and density of a university cafeteria using SimPy and Matplotlib. The simulation tracks student arrivals, queuing, service at counters, and table occupancy within a visual interface.

🚀 Key Features
Dynamic Student Flow: Students enter the queue at defined intervals based on the ARRIVAL_INTERVAL parameter.

Multi-Server System: The system utilizes 3 active service counters to process students simultaneously.

Table Management: The occupancy of 5 different tables in the dining area is monitored and visualized in real-time.

Visualization: An animated interface created with Matplotlib features custom icons and a thematic background for Manisa Celal Bayar University.

Statistical Reporting: Comprehensive data (total student count, average wait time, service time, and eating duration) reported at the end of the simulation.

🛠 Installation & Usage
1. Install required libraries:
 pip install simpy matplotlib pillow
2. Run the simulation:
 python cafeteria_simulation.py

⚙️ Simulation Parameters
You can modify the following variables within cafeteria_simulation.py to test different scenarios:
SERVICE_TIME, Duration a student spends at the counter (Random range).
EATING_TIME, Duration a student spends at a table.
ARRIVAL_INTERVAL, The frequency at which new students arrive.
SIM_TIME, Total duration of the simulation.

📂 File Structure
cafeteria_simulation.py: Main logic and visualization code.
cafe_background.png: Background image themed for MCBU.
student_icon.png, server_icon.png, table_icon.png: Graphical assets for the simulation.
Developer Note: This simulation was developed for educational purposes to understand queue theory and resource management principles.
