import tkinter as tk
from tkinter import messagebox
import time
import threading

# --- Main Functions ---
def start_timer():
    try:
        hours = int(hour_entry.get() or 0)
        minutes = int(min_entry.get() or 0)
        seconds = int(sec_entry.get() or 0)
        total_seconds = hours * 3600 + minutes * 60 + seconds

        def countdown(t):
            while t >= 0 and running[0]:
                mins, secs = divmod(t, 60)
                hrs, mins = divmod(mins, 60)
                time_display.config(text=f"{hrs:02d}:{mins:02d}:{secs:02d}")
                time.sleep(1)
                t -= 1
            if t < 0 and running[0]:
                messagebox.showinfo("Time's Up!", "⏰ Timer Finished!")
        
        running[0] = True
        threading.Thread(target=countdown, args=(total_seconds,), daemon=True).start()
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers!")

def start_stopwatch():
    start_time = time.time()
    running[0] = True

    def update():
        while running[0]:
            elapsed = int(time.time() - start_time)
            mins, secs = divmod(elapsed, 60)
            hrs, mins = divmod(mins, 60)
            time_display.config(text=f"{hrs:02d}:{mins:02d}:{secs:02d}")
            time.sleep(1)
    
    threading.Thread(target=update, daemon=True).start()

def stop():
    running[0] = False

def reset():
    running[0] = False
    time_display.config(text="00:00:00")
    hour_entry.delete(0, tk.END)
    min_entry.delete(0, tk.END)
    sec_entry.delete(0, tk.END)

# --- GUI Setup ---
root = tk.Tk()
root.title("🕒 Timer & Stopwatch")
root.geometry("300x350")
root.config(bg="#1e1e1e")

running = [False]

title = tk.Label(root, text="Timer & Stopwatch", font=("Helvetica", 16, "bold"), bg="#1e1e1e", fg="white")
title.pack(pady=10)

time_display = tk.Label(root, text="00:00:00", font=("Helvetica", 36, "bold"), bg="#1e1e1e", fg="#00FF99")
time_display.pack(pady=20)

# Input for Timer
tk.Label(root, text="Set Timer (H:M:S):", bg="#1e1e1e", fg="white", font=("Helvetica", 10)).pack()
frame = tk.Frame(root, bg="#1e1e1e")
frame.pack()

hour_entry = tk.Entry(frame, width=5)
hour_entry.grid(row=0, column=0, padx=3)
min_entry = tk.Entry(frame, width=5)
min_entry.grid(row=0, column=1, padx=3)
sec_entry = tk.Entry(frame, width=5)
sec_entry.grid(row=0, column=2, padx=3)

# Buttons
btn_frame = tk.Frame(root, bg="#1e1e1e")
btn_frame.pack(pady=15)

tk.Button(btn_frame, text="Start Timer", command=start_timer, bg="#00bcd4", fg="white", width=10).grid(row=0, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="Stopwatch", command=start_stopwatch, bg="#4caf50", fg="white", width=10).grid(row=0, column=1, padx=5, pady=5)
tk.Button(btn_frame, text="Stop", command=stop, bg="#f44336", fg="white", width=10).grid(row=1, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="Reset", command=reset, bg="#9c27b0", fg="white", width=10).grid(row=1, column=1, padx=5, pady=5)

root.mainloop()
