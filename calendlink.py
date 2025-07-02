import os.path
import datetime as dt

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from Parser import Parser

SCOPES = ['https://www.googleapis.com/auth/calendar', 'https://www.googleapis.com/auth/userinfo.profile'
]

class CalendLink:
    def __init__(self, credentials_file='credentials.json', token_file='token.json'):
        self.creds = None
        self.token_file = token_file
        self.credentials_file = credentials_file
        self.service = None
        self.authenticate()

    def authenticate(self):
        if os.path.exists(self.token_file):
            self.creds = Credentials.from_authorized_user_file(self.token_file, SCOPES)

        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    self.credentials_file, SCOPES)
                # Force Google to return a refresh_token by using 'consent' prompt
                # This is useful if the user has already granted access but we need a refresh token
                self.creds = flow.run_local_server(
                port=8080,
                access_type='offline', 
                prompt='consent')

            # Save refreshed or new credentials
            with open(self.token_file, 'w') as token:
                token.write(self.creds.to_json())

        try:
            self.service = build('calendar', 'v3', credentials=self.creds)
        except HttpError as error:
            print(f'An error occurred: {error}')
            self.creds = None

    def create_calendar_event(self, event_text):
        parser = Parser(event_text)
        parsed_event = parser.parse()

        if not parsed_event:
            print("Failed to parse the event. Please check the input.")
            return
        if not self.service:
            print("Service not initialized. Please authenticate first.")
            return

        # Create the event body
        event_body = {
            'summary': parsed_event.get('Event Title', 'No Title'),
            'location': parsed_event.get('Event Location', ''),
            'description': parsed_event.get('Event Description', ''),
            'start': {
                'dateTime': parsed_event.get('Start time'),
                'timeZone': 'UTC',
            },
            'end': {
                'dateTime': parsed_event.get('End Time'),
                'timeZone': 'UTC',
            },
        }
        try:
            event = self.service.events().insert(calendarId='primary', body=event_body).execute()
            print(f"Event created: {event.get('htmlLink')}")
        except HttpError as error:
            print(f'An error occurred while creating the event: {error}')

    def delete_calendar_event(self, event_text):
        parser = Parser(event_text)
        parsed_event = parser.parse()

        if not parsed_event:
            print("Failed to parse the event. Please check the input.")
            return
        if not self.service:
            print("Service not initialized. Please authenticate first.")
            return
        # Create the event body
        event_body = {
            'summary': parsed_event.get('Event Title', 'No Title'),
            'location': parsed_event.get('Event Location', ''),
            'description': parsed_event.get('Event Description', ''),
            'start': {
                'dateTime': parsed_event.get('Start time'),
                'timeZone': 'UTC',
            },
            'end': {
                'dateTime': parsed_event.get('End Time'),
                'timeZone': 'UTC',
            },
        }
        try:
            event = self.service.events().insert(calendarId='primary', body=event_body).execute()
            print(f"Event created: {event.get('htmlLink')}")
        except HttpError as error:
            print(f'An error occurred while creating the event: {error}')

        




    def get_profile_photo_url(self):
        try:
            people_service = build('people', 'v1', credentials=self.creds)
            profile = people_service.people().get(
                resourceName='people/me',
                personFields='photos'
            ).execute()

            photos = profile.get("photos", [])
            if photos:
                return photos[0].get("url")
            return None
        except Exception as e:
            print("Failed to fetch profile photo:", e)
            return None

    

