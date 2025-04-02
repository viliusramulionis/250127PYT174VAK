import os
import pickle
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

class GoogleApi() :
    def __init__(self, scopes, api, version) :
        print("Google API")
        self.scopes = scopes
        self.api = api
        self.version = version
        self.token_file = api + version + ".pickle"
        self.service = self.google_authenticate()


    def google_authenticate(self):
        creds = None
        
        # Tikriname ar egizstuoja failas pavadinimu token.pickle
        # Po sėkmingos autentifikacijos Google servisas išduoda raktą angliškai token
        # Raktą išssaugome specifiniu formatu .pickle
        if os.path.exists(self.token_file):
            with open(self.token_file, "rb") as token:
                creds = pickle.load(token)
        
        # Jeigu nėra rasta jokio registruoto rakto:
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file('credentials.json', self.scopes)
                creds = flow.run_local_server(port=0)

            # save the credentials for the next run
            with open(self.token_file, "wb") as token:
                pickle.dump(creds, token)

        return build(self.api, self.version, credentials=creds)