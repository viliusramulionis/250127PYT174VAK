import sqlite3

class Database  :
    def __init__(self) :
        self.db = sqlite3.connect("database.db")
        self.cursor = self.db.cursor()

        self.sukurti_lentele()

       
    def sukurti_lentele(self) :
        self.cursor.execute("CREATE TABLE IF NOT EXISTS produktai (id INTEGER PRIMARY KEY AUTOINCREMENT, pavadinimas TEXT, kaina DECIMAL(10,2), kiekis INTEGER, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")


    def ikelti_eilute(self, data : list) :
        reiksmes = []

        for val in data :
            if isinstance(val, str) :
                reiksmes.append(f"'{val}'")

            if isinstance(val, int) or isinstance(val, float) :
                reiksmes.append(f"{val}")

        # print(reiksmes)

        self.cursor.execute(f"INSERT INTO produktai (pavadinimas, kaina, kiekis) VALUES ({",".join(reiksmes)})")
        self.db.commit()

        # print(self.prisijungimas.lastrowid)


    def paimti_eilutes(self, stulpeliai = [], pavadinimas = None, kaina_nuo = None, kaina_iki = None, kiekis = None) :
        where = ""

        if pavadinimas :
            where += f"pavadinimas LIKE '%{pavadinimas}%'"

        if kaina_nuo and kaina_iki :
            where += f"kaina > {kaina_nuo} AND kaina < {kaina_iki}"

        if kiekis :
            where += f"kiekis = {kiekis}"

        if where != "" :
            where = "WHERE " + where

        return self.cursor.execute(f"SELECT {",".join(stulpeliai)} FROM produktai {where}").fetchall()
    
    def atnaujinti_eilute(self, stulpelis, reiksme, id) :
        self.cursor.execute(f"UPDATE produktai SET {stulpelis} = '{reiksme}' WHERE id = {id}")
        
        self.db.commit()
        
    def istrinti_eilute(self, id) :
        self.cursor.execute(f"DELETE FROM produktai WHERE id = {id}")