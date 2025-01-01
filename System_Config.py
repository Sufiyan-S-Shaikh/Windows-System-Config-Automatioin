import screen_brightness_control as sbc
from pycaw.pycaw import AudioUtilities
from ctypes import cast, POINTER
from pycaw.pycaw import IAudioEndpointVolume
import subprocess
import logging
import time
import pyautogui
from plyer import notification


# Configure logging
logging.basicConfig(
    filename="system_config_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def set_brightness(brightness):
    try:
        # Check if brightness is in a valid range
        if not (0 <= brightness <= 100):
            raise ValueError("Brightness must be between 0 and 100.")

        sbc.set_brightness(brightness)
        logging.info(f"Brightness set to {brightness}%.")
        send_notification("Brightness Update", f"Brightness set to {brightness}% successfully.")
    except Exception as e:
        logging.error(f"Failed to set brightness: {e}")
        send_notification("Brightness Update Failed", str(e))


def set_volume(level):
    try:
        # Check if volume level is in a valid range
        if not (0.0 <= level <= 1.0):
            raise ValueError("Volume level must be between 0.0 and 1.0.")

        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, 0, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        volume.SetMasterVolumeLevelScalar(level, None)
        logging.info(f"Volume set to {int(level * 100)}%.")
        send_notification("Volume Update", f"Volume set to {int(level * 100)}% successfully.")
    except Exception as e:
        logging.error(f"Failed to set volume: {e}")
        send_notification("Volume Update Failed", str(e))


def is_wifi_off():
    try:
        # Run the netsh command to check Wi-Fi status
        result = subprocess.run(
            ["netsh", "interface", "show", "interface"],
            capture_output=True, text=True
        )
        # Look for a specific line indicating Wi-Fi status
        output = result.stdout
        for line in output.splitlines():
            if "Wi-Fi" in line:
                if "Disconnected" in line:
                    return True
                elif "Connected" in line:
                    return False
    except Exception as e:
        logging.error(f"Error checking Wi-Fi status: {e}")
        return False


def click_coordinates(coords, delay=2):
    try:
        logging.info(f"Moving to coordinates: {coords}")
        time.sleep(delay)  # Wait before clicking
        pyautogui.moveTo(coords)  # Move to the specified coordinates
        pyautogui.click()  # Perform the click
        logging.info(f"Clicked at: {coords}")
    except Exception as e:
        logging.error(f"Failed to click at coordinates {coords}: {e}")


def enable_wifi():
    try:
        logging.info("Checking Wi-Fi status...")
        if is_wifi_off():
            logging.info("Wi-Fi is off. Proceeding with click operations.")
            time.sleep(3)  # Wait for 3 seconds before starting

            coords_1 = (1701, 1049)  # Replace with your actual coordinates
            coords_2 = (1519, 981)  # Replace with your actual coordinates

            # First click
            click_coordinates(coords_1)

            # Second click
            click_coordinates(coords_2)

            logging.info("Wi-Fi has been turned on.")
            send_notification("Wi-Fi Update", "Wi-Fi has been turned on successfully.")
        else:
            logging.info("Wi-Fi already turned on. No actions needed.")
            send_notification("Wi-Fi Update", "Wi-Fi is already on. No actions needed.")
    except Exception as e:
        logging.error(f"Failed to enable Wi-Fi: {e}")
        send_notification("Wi-Fi Update Failed", str(e))


def launch_program(program_path):
    try:
        subprocess.Popen([program_path], shell=True)
        logging.info(f"Launched program: {program_path}")
    except Exception as e:
        logging.error(f"Failed to launch program: {e}")


def send_notification(title, message):
    try:
        notification.notify(
            title=title,
            message=message,
            app_name="System Config Script",
            timeout=10
        )
        logging.info(f"Notification sent: {title} - {message}")
    except Exception as e:
        logging.error(f"Failed to send notification: {e}")


def main():
    logging.info("Starting system configuration script.")

    # Set screen brightness to 75%
    set_brightness(75)

    # Set volume to 30%
    set_volume(0.3)

    # Turn on Wi-Fi
    enable_wifi()

    # Launch a program (example: Web Browser)
    launch_program(r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe")

    # Send a notification
    send_notification("Startup Configuration", "Brightness, volume, and Wi-Fi settings applied.")

    logging.info("System configuration completed.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logging.critical(f"Critical error in main execution: {e}")
