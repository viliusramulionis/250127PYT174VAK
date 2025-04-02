from service.google_api import GoogleApi
from googleapiclient.http import MediaFileUpload

class GoogleDrive(GoogleApi) :
    def __init__(self) :
        super().__init__('https://www.googleapis.com/auth/drive', 'drive', 'v3')

        print("Google Drive")

        self.service = self.google_authenticate()

    def failu_sarasas(self, query = "") :
        response = self.service.files().list(q = query).execute()

        files = response.get("files")

        next = response.get("nextPageToken")

        while next : 
            response = self.service.files().list(q = query).execute()
            
            files.extend(response.get("files"))

            next = response.get("nextPageToken")

        return files
    
    def failo_ikelimas(self, failas, failo_pavadinimas, direktorijos = []) :
        body = { "name" : failo_pavadinimas, "parents" : direktorijos}
        # Failo paėmimas iš esamos direktorijos
        media_body = MediaFileUpload(failas)
        # Failo perkėlimo iniciavimas
        return self.service.files().create(body = body, media_body = media_body).execute()
    
    def failo_pervadinimas(self, senoId, naujas) :
        return self.service.files().update(fileId = senoId, body = { "name" : naujas }).execute()
    
    def failo_istrynimas(self, id) :
        return self.service.files().update(fileId = id, body = { "trashed" : True }).execute()