This project is a discrete event simulation designed to model the flow and density of a university cafeteria using SimPy and Matplotlib. The simulation tracks student arrivals, queuing, service at counters, and table occupancy within a visual interface.

Key Features
➤Dynamic Student Flow: Students enter the queue at defined intervals based on the ARRIVAL_INTERVAL parameter.
➤Multi-Server System: The system utilizes 3 active service counters to process students simultaneously.
➤Table Management: The occupancy of 5 different tables in the dining area is monitored and visualized in real-time.
➤Visualization: An animated interface created with matplotlib features custom icons and a thematic background for Manisa Celal Bayar University.
➤Statistical Reporting: At the end of the simulation, data such as total student count, average wait time, service time, and eating duration are reported.

Installation
Python must be installed to run the simulation. You can install the required libraries using the following command:
pip install simpy matplotlib pillow

Usage
To start the simulation, run the following command in the main directory:
python cafeteria_simulation.py

Simulation Parameters
You can modify the following variables within the cafeteria_simulation.py file to test different scenarios:

●SERVICE_TIME: The duration a student spends at the counter (Random range).
●EATING_TIME: The duration a student spends at a table.
●ARRIVAL_INTERVAL: The frequency at which new students arrive.
●SIM_TIME: Total duration of the simulation.

File Structure
cafeteria_simulation.py: Main logic and visualization code for the simulation.
cafe_background.png: Background image themed for MCBU.
student_icon.png: Graphical asset for student representation.
server_icon.png: Graphical asset for service staff.
table_icon.png: Graphical asset for dining tables.

Developer Note: This simulation was developed for educational purposes to understand queue theory and resource management principles.

Would you like me to add a section explaining the specific logic used for the table occupancy or the queue management?
