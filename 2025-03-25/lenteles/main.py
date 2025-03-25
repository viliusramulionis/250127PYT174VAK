from design import Ui_MainWindow

from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem

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

        self.prideti.clicked.connect(self.prideti_eilute)

        self.paisyti_eilutes()

    def prideti_eilute(self) :
        pavadinimas = self.pavadinimas.text()
        kaina = self.kaina.text()
        kiekis = self.kiekis.text()

        self.data.append([pavadinimas, kaina, kiekis])

        # DRY - Don't repeat yourself

        # KISS - Keep it simple stupid

        self.paisyti_eilutes()

    def paisyti_eilutes(self) :
        # Eilučių kiekio nurodymas:
        self.lentele.setRowCount(len(self.data))

        # setItem() metode, norint talpinti turini lentelėje nurodome: 
        # Pirmoje pozicijoje eilutės indeksą
        # Antroje stulpelio indeksą
        # Trečioje QTableWidgetItem() objektą
        # self.lentele.setItem(0, 0, item)

        for eilutes_nr, stulpeliai in enumerate(self.data) :

            for stulpelio_nr, reiksme in enumerate(stulpeliai) :

                item = QTableWidgetItem()
                
                self.lentele.setItem(eilutes_nr, stulpelio_nr, item)
                
                item.setText(reiksme)
    
# Aplikacijos iniciavimas
app = QApplication([])

langas = Langas()

langas.show()

app.exec()