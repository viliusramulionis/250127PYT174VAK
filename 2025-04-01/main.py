# Reikalingi paketai:
# pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib

# Norint terminale atspausdinti formatuotus žodynus
from pprint import pprint
from service.google_mail import GoogleMail

# Patikrinimas ar failas yra paleidžiamas ne importo būdu
if __name__ == "__main__" :
    gmail = GoogleMail()

    messages = gmail.search_messages("from:viliusramulionisvcs@gmail.com")

    for message in messages : 
        data = gmail.read_message(message)

        # Duomenų ištraukimas iš laiško:
        email_data = {}
        email_data["body"] = data["snippet"]

        for header in data["payload"]["headers"] :
            if header["name"] == "From" :
                email_data["from"] = header["value"]
                
            if header["name"] == "Subject" :
                email_data["subject"] = header["value"]

    # Žinutės siuntimo iniciavimas
    gmail.send_message("nifeje8325@motivue.com", "Laiškas išsiųstas iš kodo", "Labas Pasauli")

    # Žinutės ištrynimo iniciavimas
    gmail.delete_message({'id': '195f2460ead5dc3b', 'threadId': '195f2460ead5dc3b'})

    

