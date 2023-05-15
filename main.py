import datetime
import os
import pickle
import serial.tools.list_ports
import serial
import time
import sys
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Define the scopes and credentials file path
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
CREDENTIALS_FILE = 'cred.json'
TOKEN_FILE = 'token.pickle'

def authenticate():
    creds = None
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(TOKEN_FILE, 'wb') as token:
            pickle.dump(creds, token)
    return creds

def get_next_event(service):
    now = datetime.datetime.utcnow().isoformat() + 'Z'
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                          maxResults=1, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])
    if not events:
        return False, None, None, None
    else:
        event = events[0]
        start = event['start'].get('dateTime', event['start'].get('date'))
        end = event['end'].get('dateTime', event['end'].get('date'))
        start_time = datetime.datetime.fromisoformat(start).strftime('%H:%M')
        end_time = datetime.datetime.fromisoformat(end).strftime('%H:%M')
        return True, event['summary'], start_time, end_time

def findport():
    ports = serial.tools.list_ports.comports()
    portsList = []

    for i in ports: # make a list of ports
        portsList.append(str(i))
    print('Found ports: {}'.format(portsList))

    if not portsList: # if no ports are available
        print("No ports available")
        return None

    val = str(input("\nSelect PORT: COM "))

    for x in range(0, len(portsList)):
        if portsList[x].startswith("COM" + val):
            portVar = "COM" + val
            return portVar
    print("Port not found")

def output(portVar, summary, start, end):
    screen = serial.Serial(portVar, 9600)
    time.sleep(2)
    display_text = f"{start} - {end}\n{summary}\n"

    if screen.is_open:
        screen.write(display_text.encode())

    screen.close()

def main():
    creds = authenticate()
    service = build('calendar', 'v3', credentials=creds)
    
    while True:
        boole, summary, start, end = get_next_event(service)
        portVar = findport()
        output(portVar, summary, start, end)
        
        # Delay for 10 minutes
        time.sleep(10 * 60)

if __name__ == '__main__':
    main()
