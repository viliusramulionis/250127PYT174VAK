import os
import pickle
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from email.mime.text import MIMEText
from base64 import urlsafe_b64encode

class GoogleMail() :
    SCOPES = ['https://mail.google.com/']
    token_file = 'token.pickle'
    our_email = "pythonmokymai@gmail.com"

    def __init__(self) :
        print("Gmail")
        self.service = self.gmail_authenticate()

    def gmail_authenticate(self):
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
                flow = InstalledAppFlow.from_client_secrets_file('credentials.json', self.SCOPES)
                creds = flow.run_local_server(port=0)

            # save the credentials for the next run
            with open(self.token_file, "wb") as token:
                pickle.dump(creds, token)

        return build('gmail', 'v1', credentials=creds)
    

    def search_messages(self, query = "") :
        # Žinučių filtravimo eilutė:
        # userId - aktyvaus vartotojo el. paštas (me = dabar aktyvuotas)
        # query - Parametre query priimama reikšmė

        result = self.service.users().messages().list(userId = "me", q = query).execute()

        messages = []
        # Gauname pirmus 50 rezultatų
        if 'messages' in result:
            messages.extend(result['messages'])

        # Einame per sekančius puslapius ir susigrąžiname likusias žinutes
        while 'nextPageToken' in result:
            page_token = result['nextPageToken']
            result = self.service.users().messages().list(userId = "me", q = query, pageToken = page_token).execute()

            if 'messages' in result:
                messages.extend(result['messages'])

        return messages
    
    def read_message(self, message) :
        return self.service.users().messages().get(userId = "me", id = message["id"], format = "full").execute()
    
    # Žinutės formatavimas
    def build_message(self, to, subject, body) :
        message = MIMEText(body)
        message["to"] = to
        message["from"] = self.our_email
        message["subject"] = subject

        return {"raw" : urlsafe_b64encode(message.as_bytes()).decode()}
    
    # Žinutės siuntimas
    def send_message(self, to, subject, body) :
        self.service.users().messages().send(
            userId = "me",
            body = self.build_message(to, subject, body)
        ).execute()

    # Žinutės ištrynimas
    def delete_message(self, message) :
        self.service.users().messages().batchDelete(
            userId = "me",
            body = {
                "ids" : [ message["id"] ]
            }
        ).execute()