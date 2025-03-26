from design import Ui_MainWindow

from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QPushButton

import sqlite3

class Langas(QMainWindow, Ui_MainWindow) :
    data = [
        ["Televizorius", "199.99", "1"],
        ["Kompiuteris", "2000", "14"],
        ["Klaviatūra", "39.99", "5"]
    ]

    def __init__(self) :
        super().__init__()

        self.setupUi(self)

        print("Langas atidarytas")


        # Duomenų paėmimas iš duomenų bazės
        self.data = self.paimti_eilutes()
        # Lentelės atnaujinimas
        self.paisyti_eilutes()

        # Įvykių registravimas
        self.prideti.clicked.connect(self.prideti_eilute)
        self.filtras_pavadinimas.textChanged.connect(self.filtruoti_pagal_pavadinima)
        self.filtras_kaina_nuo.textChanged.connect(self.filtruoti_pagal_kaina)
        self.filtras_kaina_iki.textChanged.connect(self.filtruoti_pagal_kaina)
        self.filtras_kiekis.textChanged.connect(self.filtruoti_pagal_kieki)

        # Lentelės stulpelių praplėtimas
        self.lentele.setColumnCount(4)

    # Duomenu registravimo ivykis
    def prideti_eilute(self) :
        pavadinimas = self.pavadinimas.text()
        kaina = self.kaina.text()
        kiekis = self.kiekis.text()

        self.ikelti_eilute([pavadinimas, kaina, kiekis])

        self.data = self.paimti_eilutes()

        self.paisyti_eilutes()

    # Filtro pagal pavadinima ivykis
    def filtruoti_pagal_pavadinima(self) :
        tekstas = self.filtras_pavadinimas.text()
        self.data = self.paimti_eilutes(pavadinimas = tekstas)
        self.paisyti_eilutes()

    # Filtro pagal kaina ivykis
    def filtruoti_pagal_kaina(self) :
        nuo = self.filtras_kaina_nuo.text()
        iki = self.filtras_kaina_iki.text()
        
        self.data = self.paimti_eilutes(kaina_nuo = nuo, kaina_iki = iki)
        self.paisyti_eilutes()
        

    # Filtro pagal kieki ivykis
    def filtruoti_pagal_kieki(self) :
        kiekis = self.filtras_kiekis.text()
        
        self.data = self.paimti_eilutes(kiekis = kiekis)
        self.paisyti_eilutes()
        

    # Perpaisome eilutes kurios priskirtos prie data atrributo
    def paisyti_eilutes(self) :
        # Eilučių kiekio nurodymas:
        self.lentele.setRowCount(len(self.data))

        for eilutes_nr, stulpeliai in enumerate(self.data) :

            for stulpelio_nr, reiksme in enumerate(stulpeliai) :

                item = QTableWidgetItem()
                
                self.lentele.setItem(eilutes_nr, stulpelio_nr, item)
                
                item.setText(str(reiksme))

            
            button = QPushButton(parent=self.centralwidget)

            button.setText("Trinti")

            self.lentele.setCellWidget(eilutes_nr, 4, button)
            
            



    # Duomenų bazės funkcijos
    
    def sukurti_lentele(self) :
        with sqlite3.connect("database.db") as prisijungimas :
            prisijungimas = prisijungimas.cursor()

            prisijungimas.execute("CREATE TABLE IF NOT EXISTS produktai (id INTEGER PRIMARY KEY AUTOINCREMENT, pavadinimas TEXT, kaina DECIMAL(10,2), kiekis INTEGER, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")


    def ikelti_eilute(self, data : list) :
        reiksmes = []

        for val in data :
            if isinstance(val, str) :
                reiksmes.append(f"'{val}'")

            if isinstance(val, int) or isinstance(val, float) :
                reiksmes.append(f"{val}")

        # print(reiksmes)

        with sqlite3.connect("database.db") as prisijungimas :
            prisijungimas = prisijungimas.cursor()

            prisijungimas.execute(f"INSERT INTO produktai (pavadinimas, kaina, kiekis) VALUES ({",".join(reiksmes)})")

        # print(self.prisijungimas.lastrowid)


    def paimti_eilutes(self, pavadinimas = None, kaina_nuo = None, kaina_iki = None, kiekis = None) :
        with sqlite3.connect("database.db") as prisijungimas :
            prisijungimas = prisijungimas.cursor()
            where = ""

            if pavadinimas :
                where += f"pavadinimas LIKE '%{pavadinimas}%'"

            if kaina_nuo and kaina_iki :
                where += f"kaina > {kaina_nuo} AND kaina < {kaina_iki}"

            if kiekis :
                where += f"kiekis = {kiekis}"

            if where != "" :
                where = "WHERE " + where

            return prisijungimas.execute(f"SELECT pavadinimas, kaina, kiekis FROM produktai {where}").fetchall()
    
# Aplikacijos iniciavimas
app = QApplication([])

langas = Langas()

langas.show()

app.exec()