from design import Ui_MainWindow

from PyQt6.QtWidgets import QApplication, QMainWindow

class Langas(QMainWindow, Ui_MainWindow) :
    data = []

    def __init__(self) :
        super().__init__()

        self.setupUi(self)

        print("Langas atidarytas")

        # Įvykių registravimas
        self.pliusas.clicked.connect(self.prideti)

        self.minusas.clicked.connect(self.atimti)

    # Įvykiai (Events)
    
    def prideti(self) :
        senas_kiekis = int(self.kiekis.text())

        if senas_kiekis >= 0 :
            self.zinute.setText("")

        if senas_kiekis <= 0 :
            return self.kiekis.setText("1")

        self.kiekis.setText(str(senas_kiekis + 1))
    
    def atimti(self) :
        senas_kiekis = int(self.kiekis.text())
        
        if senas_kiekis <= 0 :
            self.kiekis.setText("0")
            return self.zinute.setText('Kiekis negali būti mažesnis nei 0!')
            
        self.kiekis.setText(str(senas_kiekis - 1))


# Aplikacijos iniciavimas
app = QApplication([])

langas = Langas()

langas.show()

app.exec()