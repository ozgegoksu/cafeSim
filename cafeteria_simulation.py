import simpy
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from PIL import Image

# Ayarlar
RANDOM_SEED = 42
ARRIVAL_INTERVAL = 1
SIM_TIME = 100
SERVICE_TIME = (5, 10)
EATING_TIME = (2, 10)
MAX_QUEUE_LENGTH = 50

queue = []
servers = [None] * 3
students = []
tables = [None] * 5
time = 0
student_id = 1

# İstatistikler
statistics = {
    "total_students": 0,
    "total_service_time": 0,
    "total_wait_time": 0,
    "total_eat_time": 0,
    "max_queue_length": 0
}

fig, ax = plt.subplots(figsize=(14, 7))

# Masaların karışık konumları (serverların sağına dağılmış)
table_positions = [
    (13, 2),
    (15, 4),
    (17, 6),
    (14, 8),
    (16, 1)
]

# İkonları yükle
table_icon = Image.open('table_icon.png')  # Masa ikonu
server_icon = Image.open('server_icon.png')  # Server ikonu
student_icon = Image.open('student_icon.png')  # Öğrenci ikonu
background_image = Image.open('cafe_background.png')  # Kafe arka plan resmi

# Masa, Gişe ve Öğrenci ikonlarını eklemek için fonksiyon
def add_image(ax, img, position, zoom=0.1):
    img = OffsetImage(img, zoom=zoom)
    ab = AnnotationBbox(img, position, frameon=False, xycoords='data', boxcoords="offset points", pad=0)
    ax.add_artist(ab)

def update(frame):
    global time, student_id

    if frame % ARRIVAL_INTERVAL == 0:
        student = {
            'id': student_id,
            'arrival': frame,
            'service_time': random.randint(*SERVICE_TIME),
            'start': None,
            'eating_time': None,
            'wait_time': None
        }
        queue.append(student)
        students.append(student)
        student_id += 1
        statistics["total_students"] += 1

    statistics["max_queue_length"] = max(statistics["max_queue_length"], len(queue))

    for i in range(len(servers)):
        if servers[i] is None and queue:
            student = queue.pop(0)
            student['start'] = frame
            student['wait_time'] = frame - student['arrival']
            statistics["total_wait_time"] += student['wait_time']
            statistics["total_service_time"] += student['service_time']
            servers[i] = (student, student['service_time'])

    for i in range(len(servers)):
        if servers[i] is not None:
            student, remaining = servers[i]
            remaining -= 1
            if remaining <= 0:
                servers[i] = None
                placed = False
                for j in range(len(tables)):
                    if tables[j] is None:
                        tables[j] = student
                        student['eating_time'] = random.randint(*EATING_TIME)
                        statistics["total_eat_time"] += student['eating_time']
                        placed = True
                        break
                if not placed:
                    queue.append(student)
            else:
                servers[i] = (student, remaining)

    for j in range(len(tables)):
        if tables[j] is not None:
            student = tables[j]
            student['eating_time'] -= 1
            if student['eating_time'] <= 0:
                tables[j] = None

    ax.clear()
    ax.set_xlim(0, 22)
    ax.set_ylim(0, 12)
    ax.set_title(f"Time: {frame}", fontsize=16)

    # Arka planı ekle
    ax.imshow(background_image, extent=[0, 22, 0, 12], aspect='auto')

    # Kuyruk
    for idx, s in enumerate(queue):
        ax.add_patch(plt.Rectangle((1, 8 - idx), 1, 0.8, facecolor='orange', edgecolor='black'))
        ax.text(1.5, 8 - idx + 0.4, f"S{s['id']}", ha='center', va='center', fontsize=10)
        add_image(ax, student_icon, (1.5, 8 - idx + 0.4), zoom=0.1)

    ax.text(0.5, 7.6, 'Queue', ha='center', va='center', fontsize=12, color='black')

    # Gişeler
    for i, server in enumerate(servers):
        ax.add_patch(plt.Rectangle((5 + i * 2, 5), 1, 0.8, edgecolor='black', facecolor='lightgray'))
        ax.text(5 + i * 2 + 0.5, 5.4, f"Server {i + 1}", ha='center', va='center', fontsize=10)

        if server is not None:
            s, rem = server
            ax.add_patch(plt.Rectangle((5 + i * 2, 6), 1, 0.8, facecolor='green', edgecolor='black'))
            ax.text(5 + i * 2 + 0.5, 6.4, f"S{s['id']}", ha='center', va='center', fontsize=10)
            add_image(ax, server_icon, (5 + i * 2 + 0.5, 5.5), zoom=0.1)

    # Masalar (Yeşil dikdörtgenler)
    for j, pos in enumerate(table_positions):
        if tables[j] is None:
            color = 'green'
            text = 'Free'
        else:
            color = 'red'
            text = 'Occupied'

        ax.add_patch(plt.Rectangle((pos[0], pos[1] + 0.8), 1.7, 1, facecolor=color, edgecolor='black'))  # Dikdörtgen masalar
        ax.text(pos[0] + 0.85, pos[1] + 1.3, f"Table {j + 1}\n{text}", ha='center', va='center', fontsize=10)

        # Masa ikonu eklemek
        add_image(ax, table_icon, (pos[0] + 0.5, pos[1] + 0.1), zoom=0.1)

    # Simülasyon bittiğinde istatistikleri ekrana yaz
    if frame == SIM_TIME - 1:
        avg_wait_time = statistics["total_wait_time"] / statistics["total_students"] if statistics["total_students"] > 0 else 0
        avg_service_time = statistics["total_service_time"] / statistics["total_students"] if statistics["total_students"] > 0 else 0
        avg_eat_time = statistics["total_eat_time"] / statistics["total_students"] if statistics["total_students"] > 0 else 0

        stats_text = (
            f"--- Simulation Statistics ---\n"
            f"Total students: {statistics['total_students']}\n"
            f"Average wait time: {avg_wait_time:.2f}\n"
            f"Average service time: {avg_service_time:.2f}\n"
            f"Average eating time: {avg_eat_time:.2f}\n"
            f"Max queue length: {statistics['max_queue_length']}"
        )
        ax.text(0.5, 0.5, stats_text,
                transform=ax.transAxes,
                fontsize=12,
                verticalalignment='center',
                horizontalalignment='center',
                bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=1'))

ani = animation.FuncAnimation(fig, update, frames=SIM_TIME, interval=500, repeat=False)
plt.show()
