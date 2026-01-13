# Jarvis AI Assistant (Phase-01)

Jarvis is a modular AI-based personal assistant built using Python.

## Features
- Voice input and voice response
- Intent detection using NLP
- System and web automation
- GPT-based conversational fallback
- SQLite logging
- Simple GUI

## Project Structure

main.py
app/
├── core/
├── speech/
├── actions/
├── ai/
├── db/
├── ui/
└── utils/
data/
jarvis.db



## How to Run
1. Install dependencies  
   `pip install -r requirements.txt`

2. Set environment variable  
   `setx OPENAI_API_KEY "your_key_here"`

3. Run Jarvis  
   `python main.py`

## Phase Status
- Phase-01: ✅ Completed & Frozen
- Phase-02: Gesture & Face Control (Planned)
