from PyQt5.QtWidgets import *
from PyQt5.QtGui import*
from PyQt5.QtCore import *
import sys

class Ui_SecondWindow(object):
    def setupUi(self, MainWindow):

        self.window = MainWindow

        self.vertikal = QVBoxLayout()
        self.tabs(MainWindow)

        self.widget = QWidget()
        self.widget.setLayout(self.vertikal)
        MainWindow.setCentralWidget(self.widget)
        MainWindow.setWindowTitle("Covid-19 Self Check Up")
        MainWindow.setGeometry(350,200,600,100)

    def tabs(self, MainWindow):
        self.font = QFont()
        self.font.setPointSize(11)
        self.font.setBold(True)

        self.font2 = QFont()
        self.font2.setPointSize(11)

        self.soal = QLabel('Apakah Anda mengalami salah satu dari yang berikut : \n\n-) Kesulitan bernafas yang parah (Bernafas dengan sangat cepat atau berbicara dalam satu kata) \n-) Nyeri dada yang parah \n-) Penurunan kesadaran')
        self.soal.setFont(self.font2)

        self.yes = QRadioButton('Ya')
        self.yes.setFont(self.font2)
        self.no = QRadioButton('Tidak')
        self.no.setFont(self.font2)

        self.radio_pilihan = QButtonGroup()
        self.radio_pilihan.addButton(self.yes)
        self.radio_pilihan.addButton(self.no)
        self.radio_pilihan.buttonClicked.connect(self.pilihan)

        self.lanjut = QPushButton('Berikutnya', objectName = 'BlueButton2')
        self.lanjut.clicked.connect(self.soal1)
        self.lanjut.setMinimumSize(QSize(600, 50))
        self.lanjut.setFont(self.font)

        self.teks = QLabel()
        self.teks.move(10, 100)

        self.vertikal.addWidget(self.soal)
        self.vertikal.addWidget(self.yes)
        self.vertikal.addWidget(self.no)
        self.vertikal.addWidget(self.lanjut)

        MainWindow.setStyleSheet("background-color: #E3F5F3;")
        MainWindow.show()

    def soal_1(self):
        self.soal.setText('Apakah Anda mengalami salah satu dari yang berikut : \n\n-) Kesulitan bernafas yang parah (Bernafas dengan sangat cepat atau berbicara dalam satu kata) \n-) Nyeri dada yang parah \n-) Sulit untuk bangun \n-) Merasa kebingungan \n-) Penurunan kesadaran')
        self.lanjut.clicked.connect(self.soal1)

        self.radio_pilihan.setExclusive(False)
        self.no.setChecked(False)
        self.radio_pilihan.setExclusive(True)

    def soal1(self):
        self.soal.setText('Apakah Anda mengalami salah satu dari yang berikut : \n\n-) Nafas yang pendek saat istirahat \n-) Ketidakmampuan untuk berbaring karena kesulitan bernafas \n-) Kondisi kesehatan kronis yang anda alami dirasakan lebih berat karena kesulitan bernapas')
        self.lanjut.clicked.connect(self.soal2)

        self.radio_pilihan.setExclusive(False)
        self.no.setChecked(False)
        self.radio_pilihan.setExclusive(True)

    def soal2(self):
        self.soal.setText('Apakah Anda memberikan perawatan atau melakukan kontak dekat dengan \nseseorang dengan COVID-19 (kemungkinan atau dikonfirmasi) saat mereka sakit \n(batuk, demam, bersin, atau sakit tenggorokan)?')
        self.lanjut.clicked.connect(self.soal3)

        self.radio_pilihan.setExclusive(False)
        self.no.setChecked(False)
        self.radio_pilihan.setExclusive(True)

    def soal3(self):
        self.soal.setText('Apakah anda pernah muncul gejala sekitar 14 hari setelah travelling ke luar negeri? \n(China, Italy, Iran, Korea Selatan, Prancis, Spanyol, Jerman, USA) \natau ke kota terjangkit ? \n(Jakarta, Bali, Solo, Yogyakarta, Pontianak, Manado, Bandung dll)')
        self.lanjut.clicked.connect(self.soal4)

        self.radio_pilihan.setExclusive(False)
        self.no.setChecked(False)
        self.radio_pilihan.setExclusive(True)

    def soal4(self):
        self.soal.setText('Apakah Anda memiliki kontak dekat dengan seseorang yang bepergian ke luar Negeri \ndalam 14 hari terakhir yang menjadi sakit \n(batuk, demam, bersin, atau sakit tenggorokan)?')
        self.lanjut.clicked.connect(self.selesai2)

        self.radio_pilihan.setExclusive(False)
        self.no.setChecked(False)
        self.radio_pilihan.setExclusive(True)

    def pilihan(self):
        if (self.yes.isChecked()):
            self.pesan = QMessageBox()
            self.pesan.setWindowTitle("Informasi")
            self.pesan.setFont(self.font2)
            self.pesan.setText('Gejala-gejala ini membutuhkan perhatian segera. Anda harus segera menelepon Rumah Sakit Terdekat, atau langsung pergi ke instalasi gawat darurat terdekat.')
            self.pesan.exec_()
            self.selesai()
        if (self.no.isChecked()):
            self.teks.setText('')

    def selesai2(self):
        self.pesan2 = QMessageBox()
        self.pesan2.setWindowTitle("Informasi")
        self.pesan2.setFont(self.font2)
        self.pesan2.setText('Anda kemungkinan besar tidak terinfeksi oleh COVID-19, namun anda disarankan untuk tetap tinggal dirumah. Hindarilah keluar rumah jika memungkinkan')
        self.pesan2.exec_()
        self.selesai()

    def selesai(self):
        self.window.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_SecondWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())