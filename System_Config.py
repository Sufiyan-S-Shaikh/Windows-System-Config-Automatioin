import screen_brightness_control as sbc
from pycaw.pycaw import AudioUtilities
from ctypes import cast, POINTER
from pycaw.pycaw import IAudioEndpointVolume
import subprocess
import logging

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
    except Exception as e:
        logging.error(f"Failed to set brightness: {e}")


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
    except Exception as e:
        logging.error(f"Failed to set volume: {e}")

def enable_wifi():
    try:
        result = subprocess.run(
            "netsh interface set interface \"Wi-Fi\" enable",
            shell=True,
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            logging.info("Wi-Fi enabled successfully.")
        else:
            logging.error(f"Failed to enable Wi-Fi: {result.stderr}")
    except Exception as e:
        logging.error(f"Error enabling Wi-Fi: {e}")


def main():
    logging.info("Starting system configuration script.")

    # Set screen brightness to 75%
    set_brightness(75)

    # Set volume to 30%
    set_volume(0.3)

    # Turn on Wi-Fi
    enable_wifi()

    logging.info("System configuration completed.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logging.critical(f"Critical error in main execution: {e}")
