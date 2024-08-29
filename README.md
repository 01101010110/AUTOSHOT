# AUTOSHOT
<img src="https://github.com/01101010110/AUTOSHOT/blob/main/Pictures/AUTOSHOT_icon.jpg?raw=true" alt="Screenshot App Icon" width="200" />
A simple automatic screenshot app for Windows.

## Features 
- **Customizable Interval**: 
  - Takes a screenshot every *x* number of seconds, where *x* can be a whole number or a decimal (e.g., 0.5 for half a second).
- **Automatic Folder Creation**: 
  - Automatically creates a folder named `screenshots` or adds to an existing folder in the directory where the app is run.
- **Visual Countdown**: 
  - You are able to select the number of seconds for your countdown, giving you time to prepare. 
- **Pause and Stop Controls**:
  - Press `F8` to pause the screenshot capture.
  - Press `F9` to stop the app.

## Main Menu
<img src="https://github.com/01101010110/AUTOSHOT/blob/main/Pictures/AUTOSHOT_main_menu.png?raw=true" alt="AUTOSHOT Main Menu" width="400" />

## Countdown Timer
<img src="https://github.com/01101010110/AUTOSHOT/blob/main/Pictures/AUTOSHOT_countdown.png?raw=true" alt="Countdown Timer" width="200" />

## F8 Paused
<img src="https://github.com/01101010110/AUTOSHOT/blob/main/Pictures/AUTOSHOT_paused.png?raw=true" alt="Paused" width="200" />

## Capturing
<img src="https://github.com/01101010110/AUTOSHOT/blob/main/Pictures/AUTOSHOT_save_screenshots.png?raw=true" alt="Capturing" width="200" />

## Backend
Compiled using `pyinstaller --onefile --icon="AUTOSHOT_icon.ico" AUTOSHOT.py` in cmd.
