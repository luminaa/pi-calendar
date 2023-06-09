# Google Calendar Display

This project retrieves the next upcoming event from your Google Calendar and displays it on an external screen via a serial connection. It consists of two files: lcd.ino and main.py. The Arduino code (lcd.ino) is responsible for setting up the LCD and receiving event data from the Python script. The Python script (main.py) utilizes the Google Calendar API to access upcoming event information and communicates with the serial device (e.g., an Arduino board) to show the event details.

## Prerequisites

Before running the script, ensure that you have the following:

- Python 3.x installed on your system
- The required Python libraries installed. You can install them using the following command:
```bash
pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client pyserial python-dateutil
```

## Setup

1. Clone the repository or download the script files.

2. Obtain the Google Calendar API credentials:
 - Go to the [Google Cloud Console](https://console.cloud.google.com/).
 - Create a new project or select an existing one.
 - Enable the Google Calendar API for your project.
 - Create credentials (OAuth client ID) and download the credentials file (JSON format).
 - Rename the credentials file to `cred.json` and place it in the project directory.

3. Connect your Grove LCD to your computer via a serial connection.

4. Adjust the baudrate if necessary:
 - Open the `output()` function in the `main.py`.
 - Modify the `screen = serial.Serial(portVar, 9600)` line to match the baudrate of your serial device.
 - Open `lcd.ino` and adjust the baudrate accordingly in line `Serial.begin(9600);`

5. Run the script:
```bash
python main.py
```

6. Follow the on-screen instructions to select the appropriate serial port where your external screen is connected.

7. This will continuously check for the next event in your Google Calendar and display it on the external screen. The event details will update every minute.

## Acknowledgments

This project utilizes the following libraries:

- [Google APIs Client Library for Python](https://github.com/googleapis/google-api-python-client)
- [python-serial](https://python-serial.readthedocs.io/)
- [Grove - LCD RGB Backlight](https://github.com/Seeed-Studio/Grove_LCD_RGB_Backlight)