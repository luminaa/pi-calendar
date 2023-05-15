import datetime
import os
import pickle
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Define the scopes and credentials file path
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
CREDENTIALS_FILE = 'pi-calendar\cred.json'
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
    now = datetime.datetime.utcnow().isoformat() + 'Z'  # Get current date and time in UTC
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                          maxResults=1, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])
    if not events:
        print('No upcoming events found.')
    else:
        event = events[0]
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(f'Next event: {event["summary"]}')
        print(f'Start time: {start}')

def main():
    creds = authenticate()
    service = build('calendar', 'v3', credentials=creds)
    get_next_event(service)

if __name__ == '__main__':
    main()
