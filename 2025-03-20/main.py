from dizainas import Ui_MainWindow

from PyQt6.QtWidgets import QApplication, QMainWindow

class Langas(QMainWindow, Ui_MainWindow) :
    data = []

    def __init__(self) :
        super().__init__()

        self.setupUi(self)

        print("Langas atidarytas")

        # Įvykių registravimas
        self.mygtukas.clicked.connect(self.paspaudimas)

    # Įvykiai (Events)
    
    def paspaudimas(self) :
        # print(self.pavadinimas.text())
        tekstas = self.pavadinimas.text()

        self.data.append(tekstas)
        self.sarasas.addItem(tekstas)

        # Grąžina label elemento tekstą
        # self.kiekis.text()

        self.kiekis.setText(str(len(self.data)))


# Aplikacijos iniciavimas
app = QApplication([])

langas = Langas()

langas.show()

app.exec()