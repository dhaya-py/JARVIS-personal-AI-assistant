import os
import pyautogui

def handle_system(label):
    try:
        if label.startswith("open"):
            app = label.replace("open ", "")
            os.startfile(app)
            return f"{app} opened successfully"

        elif label.startswith("close"):
            app = label.replace("close ", "")
            pyautogui.hotkey('alt', 'f4')
            return f"{app} closed successfully"

        return "System command executed"
    except Exception:
        return "System action failed"
