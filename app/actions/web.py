import webbrowser

def handle_web(query):
    try:
        webbrowser.open(query)
        return "Browser opened"
    except Exception:
        return "Unable to open browser"
