import tkinter as tk
from threading import Thread
from app.core.engine import JarvisEngine

engine = JarvisEngine()

def start_engine():
    engine.start()

def start_gui():
    window = tk.Tk()
    window.title("Jarvis AI Assistant")

    tk.Button(window, text="Start Jarvis", command=lambda: Thread(target=start_engine).start()).pack(pady=10)
    tk.Button(window, text="Stop Jarvis", command=engine.stop).pack(pady=10)

    window.mainloop()
