import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

__all__ = [
    "ServiceBuilder",
]

class ServiceBuilder(object):
    def __init__(self):
        self.SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']
        self.creds = self.get_credentials()

    def get_credentials(self):
        creds = None
        # The file config/token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first time.
        if os.path.exists('config/token.pickle'):
            with open('config/token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'config/credentials.json', self.SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('config/token.pickle', 'wb') as token:
                pickle.dump(creds, token)
        return creds

    def build_service(self):
        if not self.creds:
            raise AttributeError("No credentials exist")
        return build('drive', 'v3', credentials=self.creds)
