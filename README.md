
# Windows System Configuration Automation

This project is a Python script designed to automate system configuration tasks on a Windows machine. The script provides a seamless way to adjust system settings, launch essential applications, and monitor system health—all automatically at startup.

## Overview

Modern workflows demand efficiency, and repetitive tasks such as adjusting system settings or ensuring the system is in an optimal state can waste valuable time. This script was created to eliminate such inefficiencies by automating common tasks performed at system startup.

## Features

1. **Brightness and Volume Adjustment**
   - Automatically adjusts the screen brightness and volume to predefined levels to ensure a comfortable environment right from the start.

2. **Wi-Fi Enabling**
   - Checks the current Wi-Fi status and, if disabled, uses GUI automation to enable it. This ensures you're always connected without manual intervention.

3. **Program Launcher**
   - Launches essential applications (e.g., Web browser) immediately after startup. This feature can be customized to include any program you frequently use.

4. **Custom Notifications**
   - Sends notifications after each significant task to confirm whether it was completed successfully or encountered any issues.

5. **Break Reminder**
   - Reminds you to take a break every 45 minutes, promoting better health and productivity during extended work sessions.

6. **System Health Monitoring**
   - Monitors CPU and memory usage and sends alerts if their usage exceeds safe thresholds, helping you identify potential performance bottlenecks.

## Installation

To get started with the script, follow these steps:

1. **Clone the Repository**:
   Clone this repository to your local machine:
   ```bash
   git clone https://github.com/Sufiyan-S-Shaikh/Windows-System-Config-Automation.git
   cd Windows-System-Config-Automation
   ```

2. **Install Dependencies**:
   Install the required Python libraries listed in `requirements.txt` using pip:
   ```bash
   pip install -r requirements.txt
   ```

3. **Customize Settings**:
   - Modify the predefined brightness and volume levels in the script to suit your preferences.
   - Adjust the coordinates in the Wi-Fi automation logic (`coords_1` and `coords_2`) based on your screen setup.

4. **Set the Script to Run at Startup**:
   - Place the script in your system's startup folder, or use Task Scheduler to execute it automatically when the system starts.

## Usage

Run the script using the following command:
```bash
python System_Config.py
```
Ensure you have Python 3.7 or above installed on your system.

Once executed, the script will perform the following tasks sequentially:
1. Adjust screen brightness and system volume.
2. Enable Wi-Fi if it’s turned off.
3. Launch predefined programs.
4. Send success or failure notifications for each task.
5. Monitor system health continuously.
6. Remind you every 45 minutes to take a break.

## How It Works

### 1. **Brightness and Volume Adjustment**
   - The script uses Windows-specific APIs to programmatically set brightness and volume levels.

### 2. **Wi-Fi Enabling**
   - Utilizes `pyautogui` to click on specific screen coordinates (e.g., Wi-Fi icon) to enable Wi-Fi. 
   - The script first checks the Wi-Fi status using a `netsh` command to avoid unnecessary actions.

### 3. **Program Launcher**
   - Launches specific applications by providing their executable paths. You can add or modify the programs to launch by editing the script.

### 4. **Custom Notifications**
   - Uses the `plyer` library to send desktop notifications indicating the status of each task.

### 5. **Break Reminder**
   - The script employs the `schedule` library to send reminders every 45 minutes, encouraging you to step away from the screen for a short break.

### 6. **System Health Monitoring**
   - Leverages the `psutil` library to continuously monitor CPU and memory usage.
   - Sends alerts if resource usage exceeds user-defined thresholds.

## Notes

- **Break Reminder Customization**:
  Modify the interval for break reminders by adjusting the `schedule.every(45).minutes.do(remind_break)` line in the script.

- **Wi-Fi Automation**:
  Ensure `pyautogui` coordinates match your screen layout. Use `pyautogui.position()` to find exact coordinates.

- **Error Handling**:
  The script includes robust logging to identify and debug issues if any task fails.

---

Feel free to use and modify the script as per your needs. If you encounter any issues, check the logs generated in the script directory for detailed error information.
