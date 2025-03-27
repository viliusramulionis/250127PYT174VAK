from design import Ui_MainWindow
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QPushButton
from model.database import Database

# CRUD :
# CREATE
# READ
# UPDATE
# DELETE

class Langas(QMainWindow, Ui_MainWindow) :
    data = []
    keys = ["id", "pavadinimas", "kaina", "kiekis"]
    current = (None, None)

    def __init__(self) :
        super().__init__()

        self.setupUi(self)

        self.database = Database()

        print("Langas atidarytas")

        # Duomenų paėmimas iš duomenų bazės
        self.data = self.database.paimti_eilutes(self.keys)
        # Lentelės atnaujinimas
        self.paisyti_eilutes()

        # Įvykių registravimas
        self.prideti.clicked.connect(self.prideti_eilute)
        self.filtras_pavadinimas.textChanged.connect(self.filtruoti_pagal_pavadinima)
        self.filtras_kaina_nuo.textChanged.connect(self.filtruoti_pagal_kaina)
        self.filtras_kaina_iki.textChanged.connect(self.filtruoti_pagal_kaina)
        self.filtras_kiekis.textChanged.connect(self.filtruoti_pagal_kieki)

        self.lentele.cellDoubleClicked.connect(self.redaguojamo_stulpelio_fiksavimas)
        self.lentele.cellChanged.connect(self.stulpelio_atnaujinimas)
        

    # Duomenu registravimo ivykis
    def prideti_eilute(self) :
        pavadinimas = self.pavadinimas.text()
        kaina = self.kaina.text()
        kiekis = self.kiekis.text()

        self.database.ikelti_eilute([pavadinimas, kaina, kiekis])

        self.data = self.database.paimti_eilutes(self.keys)

        self.paisyti_eilutes()

    # Filtro pagal pavadinima ivykis
    def filtruoti_pagal_pavadinima(self) :
        tekstas = self.filtras_pavadinimas.text()
        self.data = self.database.paimti_eilutes(self.keys, pavadinimas = tekstas)
        self.paisyti_eilutes()

    # Filtro pagal kaina ivykis
    def filtruoti_pagal_kaina(self) :
        nuo = self.filtras_kaina_nuo.text()
        iki = self.filtras_kaina_iki.text()
        
        self.data = self.database.paimti_eilutes(self.keys, kaina_nuo = nuo, kaina_iki = iki)
        self.paisyti_eilutes()
        

    # Filtro pagal kieki ivykis
    def filtruoti_pagal_kieki(self) :
        kiekis = self.filtras_kiekis.text()
        
        self.data = self.database.paimti_eilutes(self.keys, kiekis = kiekis)
        self.paisyti_eilutes()
        

    # Perpaisome eilutes kurios priskirtos prie data atrributo
    def paisyti_eilutes(self) :
        # Lentelės stulpelių praplėtimas
        self.lentele.setColumnCount(5)
        # Eilučių kiekio nurodymas:
        self.lentele.setRowCount(len(self.data))

        # Lentelės stulpelio pločio nustatymas:
        self.lentele.setColumnWidth(0, 40)  
        self.lentele.setColumnWidth(1, 350)  

        for eilutes_nr, stulpeliai in enumerate(self.data) :

            for stulpelio_nr, reiksme in enumerate(stulpeliai) :

                item = QTableWidgetItem()
                
                self.lentele.setItem(eilutes_nr, stulpelio_nr, item)
                
                item.setText(str(reiksme))

            
            # Mygtuko objekto sukūrimas
            button = QPushButton(parent=self.centralwidget)

            # Teksto priskyrimas mygtukui
            button.setText("Trinti")

            button.pressed.connect(lambda id = stulpeliai[0] : self.eilutes_trynimas(id))

            # Mygtuko priskyrimas į lentelę
            self.lentele.setCellWidget(eilutes_nr, 4, button)
            

    # Eilutės ištrynimo įvykis
    def eilutes_trynimas(self, id) :
        print("Bandoma istrinti įrašą:", id)

        self.database.istrinti_eilute(id)
        self.data = self.database.paimti_eilutes(self.keys)
        self.paisyti_eilutes()

    
    # Stulpelio reikšmės atnaujinimo įvykis
    def stulpelio_atnaujinimas(self, eilutes_nr, stulpelio_nr) :
        if self.current[0] != eilutes_nr or self.current[1] != stulpelio_nr :
            return None
        
        print(self.current, eilutes_nr, stulpelio_nr)
        
        redaguojamas_laukelis = self.lentele.item(eilutes_nr, stulpelio_nr)
        id_laukelis = self.lentele.item(eilutes_nr, 0)

        # print(item.text())

        # print(self.keys[stulpelio_nr])

        self.database.atnaujinti_eilute(self.keys[stulpelio_nr], redaguojamas_laukelis.text(), id_laukelis.text())
        
        self.current = (None, None)

    def redaguojamo_stulpelio_fiksavimas(self, eilutes_nr, stulpelio_nr) :
        self.current = (eilutes_nr, stulpelio_nr)
    
# Aplikacijos iniciavimas
app = QApplication([])

langas = Langas()

langas.show()

app.exec()