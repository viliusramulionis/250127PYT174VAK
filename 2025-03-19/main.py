from design import Ui_Dialog

from PyQt6.QtWidgets import QDialog, QApplication

class Langas(QDialog, Ui_Dialog) :
    def __init__(self) :
        # Aktyvuojame QDialog klasės konstruktorių
        super().__init__()
        
        self.setupUi(self)

        print("Langas aktyvuotas")

        # Paspaudimo įvykio registravimas
        # self.mygtukai.clicked.connect(self.paspaudimo_ivykis)

        # Ok mygtuko ivykis
        self.mygtukai.accepted.connect(self.duomenys_priimti)
        # Cancel mygtuko ivykis
        self.mygtukai.rejected.connect(self.atmesta)

    # Funkcija kuri bus aktyvuota po mygtuko ok paspaudimo
    def duomenys_priimti(self) :
        print("Laukelyje įvesta:", self.laukelis.text())

        # Aprašomi įvykio veiksmai
        print("Mygtukas paspaustas") 

    # Funkcija kuri aktyvuojama paspaudus ant mygtuko cancel
    def atmesta(self) :
        print("Vartotojas nesutiko pateikti duomenų")

# Aplikacijos registravimas
app = QApplication([])

# Lango registravimas
langas = Langas()

# Lango atidarymas
langas.show()

# Aplikacijos iniciavimas
app.exec()