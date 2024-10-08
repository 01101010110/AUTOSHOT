import os
import pyautogui
import keyboard
import threading
from datetime import datetime

# Directory to save screenshots
screenshots_folder = "screenshots"

# Check if the directory exists, and create it if it does not
if not os.path.exists(screenshots_folder):
    os.makedirs(screenshots_folder)

# Global control variables
running = True
paused = False

def take_screenshot():
    global running, paused
    while running:
        if not paused:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
            filename = f"screenshot_{timestamp}.png"
            file_path = os.path.join(screenshots_folder, filename)
            screenshot = pyautogui.screenshot()
            screenshot.save(file_path)
            print(f"Saved screenshot to {file_path}")
        pyautogui.time.sleep(interval)  # Wait for the specified interval

def countdown_timer(countdown_time):
    for i in range(countdown_time, 0, -1):
        print(f"Starting in {i} seconds...", end='\r')
        pyautogui.time.sleep(1)
    print("Starting capture now!")

def control():
    global running, paused
    while running:
        if keyboard.is_pressed('F8'):  # Pause/Resume
            paused = not paused
            print("Paused" if paused else "Resumed")
            pyautogui.time.sleep(0.2)  # Debounce delay
        if keyboard.is_pressed('F9'):  # Stop
            running = False
            print("Stopped")
            pyautogui.time.sleep(0.2)  # Debounce delay

def main():
    global interval
    try:
        # Display the program name
        print("\n")
        print(" ▄▄▄       █    ██ ▄▄▄█████▓ ▒█████    ██████  ██░ ██  ▒█████  ▄▄▄█████▓")
        print("▒████▄     ██  ▓██▒▓  ██▒ ▓▒▒██▒  ██▒▒██    ▒ ▓██░ ██▒▒██▒  ██▒▓  ██▒ ▓▒")
        print("▒██  ▀█▄  ▓██  ▒██░▒ ▓██░ ▒░▒██░  ██▒░ ▓██▄   ▒██▀▀██░▒██░  ██▒▒ ▓██░ ▒░")
        print("░██▄▄▄▄██ ▓▓█  ░██░░ ▓██▓ ░ ▒██   ██░  ▒   ██▒░▓█ ░██ ▒██   ██░░ ▓██▓ ░ ")
        print(" ▓█   ▓██▒▒▒█████▓   ▒██▒ ░ ░ ████▓▒░▒██████▒▒░▓█▒░██▓░ ████▓▒░  ▒██▒ ░ ")
        print(" ▒▒   ▓▒█░░▒▓▒ ▒ ▒   ▒ ░░   ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒░ ▒░▒░▒░   ▒ ░░   ")
        print("  ▒   ▒▒ ░░░▒░ ░ ░     ░      ░ ▒ ▒░ ░ ░▒  ░ ░ ▒ ░▒░ ░  ░ ▒ ▒░     ░    ")
        print("  ░   ▒    ░░░ ░ ░   ░      ░ ░ ░ ▒  ░  ░  ░   ░  ░░ ░░ ░ ░ ▒    ░      ")
        print("      ░  ░   ░                  ░ ░        ░   ░  ░  ░    ░ ░           ")
        print("\n")
        
        # Ask for interval and countdown without closing
        while True:
            try:
                interval = float(input("Enter the time between screenshots (in seconds, e.g., 0.5 for half a second): "))
                if interval <= 0:
                    print("Interval must be greater than 0. Please try again.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        while True:
            try:
                countdown_time = int(input("How long would you like the countdown to be before starting the screenshots? (Enter a number of seconds): "))
                if countdown_time < 0:
                    print("Countdown time cannot be negative. Please try again.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        
        # Countdown
        countdown_timer(countdown_time)

        # Start the screenshot thread
        screenshot_thread = threading.Thread(target=take_screenshot)
        screenshot_thread.start()

        # Start the control thread
        control_thread = threading.Thread(target=control)
        control_thread.start()

        # Wait for threads to finish
        screenshot_thread.join()
        control_thread.join()
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
