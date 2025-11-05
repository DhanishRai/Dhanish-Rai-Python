import customtkinter as ctk
import random
import threading
import time
from openai import OpenAI

# ---------- Optional AI Setup ----------
AI_KEY = ""  # Add your OpenAI API key (optional)
client = OpenAI(api_key=AI_KEY) if AI_KEY else None

# ---------- Huge Local Word Pools ----------
easy_words = [
    "Keyboard", "Mouse", "Monitor", "Laptop", "Phone", "Speaker", "Camera", "Charger",
    "Tablet", "Smartwatch", "Cable", "Router", "Printer", "Drone", "Pen Drive", "Fan",
    "Bulb", "Remote", "Earbuds", "Monitor Stand", "Smart Light", "Joystick", "TV",
    "Clock", "Radio", "Mic", "Headphones", "Smart Plug", "USB Cable", "WiFi Modem",
    "Power Bank", "Tripod", "Speaker Dock", "Extension Board", "Battery", "Fan Remote"
]

medium_words = [
    "Motherboard", "Processor", "GPU", "SSD", "RAM", "Power Supply", "Heat Sink",
    "Bluetooth Module", "VR Headset", "Webcam", "Projector", "Server Rack",
    "Graphics Tablet", "Data Cable", "Motherboard Chipset", "Smart Keyboard",
    "Network Switch", "Ethernet Port", "Cooling Fan", "Gaming Console",
    "Smart Display", "VR Controller", "Router Antenna", "AI Speaker",
    "Smart Drone", "Touchscreen Panel", "Motion Sensor", "LED Controller",
    "Smart Door Lock", "Docking Station", "NAS Storage", "UPS Inverter"
]

hard_words = [
    "Quantum Processor", "Neural Engine", "AI Chipset", "Holographic Display",
    "Augmented Reality Glasses", "Cloud Server Cluster", "Machine Vision Sensor",
    "Quantum Storage Unit", "AI Robotic Arm", "Neural Interface", "Optical Data Transmitter",
    "Lidar Scanner", "Virtualization Module", "Deep Learning Accelerator", "Photon Transistor",
    "Neural Data Bridge", "Smart Energy Hub", "Cybernetic Implant", "Neural Gateway",
    "Autonomous Drone Swarm", "Parallel Compute Node", "Quantum Router", "Cloud Container Node",
    "AI Edge Device", "Zero-Latency Transmitter", "Smart Biochip", "AI Audio Synthesizer",
    "Predictive Neural Model", "Robotic Vision Engine", "Data Fusion Processor"
]

difficulty_map = {
    "Easy": easy_words,
    "Medium": medium_words,
    "Hard": hard_words
}

current_difficulty = "Easy"
available_words = []
used_words = set()
game_active = False

# ---------- CustomTkinter UI ----------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("ALTIUS 2025 | AIML Tech Pictionary")
app.state('zoomed')  # fullscreen
app.configure(fg_color="#0f172a")

# ---------- Background ----------
bg_frame = ctk.CTkFrame(app, fg_color="#74b9ff")
bg_frame.pack(fill="both", expand=True)

# ---------- Header ----------
header_frame = ctk.CTkFrame(bg_frame, fg_color="transparent")
header_frame.pack(pady=20)

event_label = ctk.CTkLabel(
    header_frame, text="🎉 ALTIUS 2025 🎉",
    font=ctk.CTkFont(size=40, weight="bold"),
    text_color="#003366"
)
event_label.pack()

dept_label = ctk.CTkLabel(
    header_frame, text="Department of Artificial Intelligence and Machine Learning",
    font=ctk.CTkFont(size=22, weight="bold"),
    text_color="#0a0a0a"
)
dept_label.pack(pady=(5, 30))

# ---------- Difficulty Selection ----------
difficulty_frame = ctk.CTkFrame(bg_frame, fg_color="#d6eaf8", corner_radius=20)
difficulty_frame.pack(pady=10)

difficulty_label = ctk.CTkLabel(
    difficulty_frame, text="Select Difficulty:",
    font=ctk.CTkFont(size=20, weight="bold"),
    text_color="#003366"
)
difficulty_label.grid(row=0, column=0, padx=20, pady=10)

def set_difficulty(choice):
    global current_difficulty
    current_difficulty = choice
    difficulty_label.configure(text=f"Difficulty: {choice}")

for i, level in enumerate(["Easy", "Medium", "Hard"]):
    btn = ctk.CTkButton(
        difficulty_frame,
        text=level,
        font=ctk.CTkFont(size=18, weight="bold"),
        width=120,
        fg_color="#0096FF",
        hover_color="#00BFFF",
        command=lambda l=level: set_difficulty(l)
    )
    btn.grid(row=0, column=i + 1, padx=10, pady=10)

# ---------- Word Display ----------
word_card = ctk.CTkFrame(
    bg_frame, width=700, height=250, corner_radius=40, fg_color="#e3f2fd"
)
word_card.pack(pady=50)
word_card.pack_propagate(False)

word_label = ctk.CTkLabel(
    word_card, text="Click Start to Begin!",
    font=ctk.CTkFont(size=40, weight="bold"),
    text_color="#003366"
)
word_label.pack(expand=True)

hint_label = ctk.CTkLabel(
    bg_frame,
    text="Draw the displayed item — others guess what it is!",
    font=ctk.CTkFont(size=22),
    text_color="#0a0a0a"
)
hint_label.pack(pady=20)

# ---------- Functions ----------
def get_ai_word():
    if not client:
        prefix = random.choice(["Neural", "Smart", "Quantum", "Cyber", "AI", "Nano", "Virtual"])
        item = random.choice(["Hub", "Module", "Chip", "Device", "System", "Node", "Cluster"])
        return f"{prefix} {item}"
    try:
        res = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": f"Give a random unique {current_difficulty.lower()} level tech item (1-3 words only)."}]
        )
        return res.choices[0].message.content.strip()
    except Exception:
        return random.choice(difficulty_map[current_difficulty])

def fade_in_text(new_word):
    for alpha in range(0, 101, 20):
        word_label.configure(text=new_word, text_color=f"#0033{hex(alpha)[2:].zfill(2)}")
        word_label.update()
        time.sleep(0.02)
    word_label.configure(text=new_word, text_color="#003366")

def next_unique_word():
    global available_words, used_words
    if not available_words:
        # refill with unused + AI-generated words
        available_words = list(set(difficulty_map[current_difficulty]) - used_words)
        if not available_words:
            new_word = get_ai_word()
            used_words.add(new_word)
            fade_in_text(new_word)
            return
    new_word = random.choice(available_words)
    available_words.remove(new_word)
    used_words.add(new_word)
    fade_in_text(new_word)

def show_next_word():
    if not game_active:
        word_label.configure(text="Start the game first!", text_color="#aa0000")
        return
    threading.Thread(target=next_unique_word, daemon=True).start()

def toggle_game():
    global game_active, used_words, available_words
    if not game_active:
        game_active = True
        start_btn.configure(text="⛔ End Game", fg_color="#cc0000", hover_color="#ff4444")
        next_btn.configure(state="normal")
        word_label.configure(text=f"Game Started ({current_difficulty})!", text_color="#003366")
        used_words.clear()
        available_words = difficulty_map[current_difficulty].copy()
    else:
        game_active = False
        start_btn.configure(text="🚀 Start Game", fg_color="#0096FF", hover_color="#00BFFF")
        next_btn.configure(state="disabled")
        word_label.configure(text="Game Ended. Select difficulty & Start again!", text_color="#003366")

# ---------- Buttons ----------
button_frame = ctk.CTkFrame(bg_frame, fg_color="transparent")
button_frame.pack(pady=30)

start_btn = ctk.CTkButton(
    button_frame, text="🚀 Start Game",
    font=ctk.CTkFont(size=22, weight="bold"),
    corner_radius=25,
    fg_color="#0096FF", hover_color="#00BFFF",
    width=200, height=60,
    command=toggle_game
)
start_btn.grid(row=0, column=0, padx=20)

next_btn = ctk.CTkButton(
    button_frame, text="➡️ Next Word",
    font=ctk.CTkFont(size=22, weight="bold"),
    corner_radius=25,
    fg_color="#0073e6", hover_color="#3399ff",
    width=200, height=60,
    state="disabled",
    command=show_next_word
)
next_btn.grid(row=0, column=1, padx=20)

# ---------- Footer ----------
footer = ctk.CTkLabel(
    bg_frame,
    text="♾️ Tech Pictionary | ALTIUS 2025 - AIML Department",
    font=ctk.CTkFont(size=18, weight="bold"),
    text_color="#003366"
)
footer.pack(side="bottom", pady=25)

# ---------- Run ----------
app.mainloop()
