# Google Calendar Display

Google Calendar Display is a Python script that retrieves the next upcoming event from your Google Calendar and displays it on an external screen via a serial connection. The script utilizes the Google Calendar API to access event information and communicates with the serial device (e.g., an Arduino board) to show the event details.

## Prerequisites

Before running the script, ensure that you have the following:

- Python 3.x installed on your system
- The required Python libraries installed. You can install them using the following command:

```bash
pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client pyserial
```

## Setup

1. Clone the repository or download the script files.

2. Obtain the Google Calendar API credentials:
 - Go to the [Google Cloud Console](https://console.cloud.google.com/).
 - Create a new project or select an existing one.
 - Enable the Google Calendar API for your project.
 - Create credentials (OAuth client ID) and download the credentials file (JSON format).
 - Rename the credentials file to `cred.json` and place it in the project directory.

3. Connect your external screen (e.g., an Arduino with an LCD display) to your computer via a serial connection.

4. Adjust the baud rate if necessary:
 - Open the `output()` function in the Python script.
 - Modify the `screen = serial.Serial(portVar, 9600)` line to match the baud rate of your serial device.

5. Run the script:
```bash
python script.py
```

6. Follow the on-screen instructions to select the appropriate serial port where your external screen is connected.

7. The script will continuously check for the next event in your Google Calendar and display it on the external screen. The event details will update every 10 minutes.

## Acknowledgments

This project utilizes the following libraries:

- [Google APIs Client Library for Python](https://github.com/googleapis/google-api-python-client)
- [python-serial](https://python-serial.readthedocs.io/)