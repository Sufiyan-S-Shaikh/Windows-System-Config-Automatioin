import screen_brightness_control as sbc
from pycaw.pycaw import AudioUtilities
from ctypes import cast, POINTER
from pycaw.pycaw import IAudioEndpointVolume
import subprocess


def set_brightness(brightness):
    sbc.set_brightness(brightness)
    print(f"Brightness set to {brightness}%.")


def set_volume(level):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, 0, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevelScalar(level, None)
    print(f"Volume set to {int(level * 100)}%.")


def enable_wifi():
    subprocess.run("netsh interface set interface \"Wi-Fi\" enable", shell=True)
    print("Wi-Fi enabled successfully.")


def main():
    # Set screen brightness to 50%
    set_brightness(50)

    # Set volume to 50%
    set_volume(0.5)

    # Turn on Wi-Fi
    enable_wifi()


if __name__ == "__main__":
    main()
