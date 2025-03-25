from design import Ui_MainWindow

from PyQt6.QtWidgets import QApplication, QMainWindow

class Langas(QMainWindow, Ui_MainWindow) :
    data =  [
        'what time is it',
        'what is today',
        'when does school start',
        'what day is it',
        'where am i',
        'what is my ip',
        'what is ai',
        'how to tie a tie',
        'what year is it',
        'how to delete instagram account',
        'what is the weather today',
        'how to deactivate facebook',
        'how to screenshot on windows',
    ]

    def __init__(self) :
        super().__init__()

        self.setupUi(self)

        print("Langas atidarytas")

        self.mygtukas.clicked.connect(self.veiksmas)

    def veiksmas(self) :
        tekstas = self.tekstas.text()

        self.sarasas.clear()

        if tekstas == "" :
            return

        for fraze in self.data :
            if tekstas in fraze :
                self.sarasas.addItem(fraze)

    
# Aplikacijos iniciavimas
app = QApplication([])

langas = Langas()

langas.show()

app.exec()