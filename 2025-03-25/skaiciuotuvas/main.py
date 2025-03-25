from design import Ui_MainWindow

from PyQt6.QtWidgets import QApplication, QMainWindow

class Langas(QMainWindow, Ui_MainWindow) :
    pirmas_skaicius = None
    antras_skaicius = None
    norimas_veiksmas = None
    galutinis_rezultatas = None

    def __init__(self) :
        super().__init__()

        self.setupUi(self)

        print("Langas atidarytas")

        for n in range(10) :
            # clicked = mygtukas paspaustas ir atleistas
            # pressed = mygtukas paspaustas
            # released = mygtukas atleistas

            getattr(self, "skaicius_" + str(n)).pressed.connect(lambda reiksme = n: self.skaiciaus_paspaudimas(reiksme))
            # getattr(self, "skaicius_" + str(n)).clicked.connect(self.skaiciaus_paspaudimas)

        for n in range(4) :
            el = getattr(self, "veiksmas_" + str(n))

            el.pressed.connect(lambda reiksme = el.text(): self.veiksmo_paspaudimas(reiksme))

        self.isvesti.clicked.connect(self.rezultato_isvedimas)

    def skaiciaus_paspaudimas(self, skaicius) :
        # Priskyrimas prie pirmo arba antro skaiciaus

        if self.norimas_veiksmas :
            self.antras_skaicius = skaicius
        else :
            self.pirmas_skaicius = skaicius

        self.atvaizdavimas()

    def veiksmo_paspaudimas(self, veiksmas) :
        self.norimas_veiksmas = veiksmas

        self.atvaizdavimas()

    def rezultato_isvedimas(self) :
        # if self.norimas_veiksmas == "/" :
        #     self.galutinis_rezultatas = self.pirmas_skaicius / self.antras_skaicius

        # if self.norimas_veiksmas == "*" :
        #     self.galutinis_rezultatas = self.pirmas_skaicius * self.antras_skaicius

        # if self.norimas_veiksmas == "+" :
        #     self.galutinis_rezultatas = self.pirmas_skaicius + self.antras_skaicius

        # if self.norimas_veiksmas == "-" :
        #     self.galutinis_rezultatas = self.pirmas_skaicius - self.antras_skaicius


        self.galutinis_rezultatas = eval(f"{self.pirmas_skaicius} {self.norimas_veiksmas} {self.antras_skaicius}")

        self.atvaizdavimas()

    def atvaizdavimas(self) :
        stringas = ""

        if self.pirmas_skaicius :
            stringas += f"{self.pirmas_skaicius}"

        if self.norimas_veiksmas :
            stringas += f" {self.norimas_veiksmas} "

        if self.antras_skaicius :
            stringas += f"{self.antras_skaicius}"

        if self.galutinis_rezultatas :
            stringas += f" = {self.galutinis_rezultatas}"

        self.vaizdas.setText(stringas)

    
# Aplikacijos iniciavimas
app = QApplication([])

langas = Langas()

langas.show()

app.exec()