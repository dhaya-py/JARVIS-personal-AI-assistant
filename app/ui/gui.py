import tkinter as tk
from threading import Thread
from app.core.engine import JarvisEngine

engine = JarvisEngine()

def start_engine(status_label):
    status_label.config(text="🟢 Jarvis is running...")
    engine.start()
    status_label.config(text="🔴 Jarvis stopped")

def start_gui():
    window = tk.Tk()
    window.title("Jarvis AI Assistant")
    window.geometry("400x200")

    status_label = tk.Label(window, text="⚪ Jarvis is idle", font=("Arial", 12))
    status_label.pack(pady=20)

    tk.Button(
        window,
        text="Start Jarvis",
        command=lambda: Thread(target=start_engine, args=(status_label,), daemon=True).start()
    ).pack(pady=5)

    tk.Button(
        window,
        text="Stop Jarvis",
        command=engine.stop
    ).pack(pady=5)

    window.mainloop()
