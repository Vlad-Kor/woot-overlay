woot-overlay, a key-overlay for wooting keyboards

# Installation instructions
## Windows
- Download and install [Wootility](https://wooting.io/wootility)
- Head over to [Releases](https://github.com/Vlad-Kor/woot-overlay/releases/latest) and download the latest windows.zip
- Edit the top line of the `settings.ini` if you want to adjust your keybinds (x and z are the default)
- Extract the zip and run the .exe

## Linux (run from source)
- Install python3 if you haven't already
- Install matplotlib (install with `python -m pip install -U matplotlib`)
- Clone the GitHub repository
- Follow [these instructions](https://help.wooting.io/article/147-configuring-device-access-for-wootility-under-linux-udev-rules) to set up the necessary udev rules required for the Wooting SDK
- Follow [these instructions](https://github.com/WootingKb/wooting-analog-sdk) to install the Wooting SDK
- Edit the top line of the `settings.ini` if you want to adjust your keybinds (x and z are the default)
- Run the `main.py` file

# Build instructions
woot-overlay can be built with pyinstaller:
```
pyinstaller --noconfirm --onefile --windowed  "D:\EIGENE DATEIEN\wooting\woot-overlay\main.py"
```
