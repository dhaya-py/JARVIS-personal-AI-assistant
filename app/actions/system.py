import subprocess
import pyautogui
import time

def handle_system(label: str):
    try:
        if label.startswith("open"):
            app = label.replace("open ", "").strip()
            subprocess.Popen(["start", "", app], shell=True)
            return f"{app} opened successfully"

        elif label.startswith("close"):
            pyautogui.hotkey("alt", "f4")
            return "Application closed"

        return "System command executed"
    except Exception as e:
        return "System action failed"
