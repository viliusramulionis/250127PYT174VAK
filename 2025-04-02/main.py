# Reikalingi paketai:
# pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib

# Norint terminale atspausdinti formatuotus žodynus
from pprint import pprint
from service.google_mail import GoogleMail
from service.google_drive import GoogleDrive
from googleapiclient.http import MediaFileUpload

# Patikrinimas ar failas yra paleidžiamas ne importo būdu
if __name__ == "__main__" :
    # gmail = GoogleMail()

    # messages = gmail.search_messages("from:viliusramulionisvcs@gmail.com")

    # for message in messages : 
    #     data = gmail.read_message(message)

    #     # Duomenų ištraukimas iš laiško:
    #     email_data = {}
    #     email_data["body"] = data["snippet"]

    #     for header in data["payload"]["headers"] :
    #         if header["name"] == "From" :
    #             email_data["from"] = header["value"]
                
    #         if header["name"] == "Subject" :
    #             email_data["subject"] = header["value"]

    # # Žinutės siuntimo iniciavimas
    # gmail.send_message("nifeje8325@motivue.com", "Laiškas išsiųstas iš kodo", "Labas Pasauli")

    # # Žinutės ištrynimo iniciavimas
    # gmail.delete_message({'id': '195f2460ead5dc3b', 'threadId': '195f2460ead5dc3b'})


    drive = GoogleDrive()

    # Visų failų paėmimas:
    # drive.service.files().list().execute()

    # pprint(drive.service.files().list().execute())

    # Failų paėmimas iš direktorijos

    response = drive.service.files().list(q = "parents = '1iNfe3_S_KLIkdN6hjVjWncDm_588hXvP'").execute()

    pprint(response.get('files'))
    
    # Failo įkėlimas
    # Nurodome kaip failas vadinsis įkėlus
    body = { "name" : "failas_kuris_yra_ikeltas.txt", "parents" : [ "1iNfe3_S_KLIkdN6hjVjWncDm_588hXvP" ]}
    # Failo paėmimas iš esamos direktorijos
    media_body = MediaFileUpload('failas_kuri_noriu_ikelti.txt')
    # Failo perkėlimo iniciavimas
    drive.service.files().create(body = body, media_body = media_body).execute()

