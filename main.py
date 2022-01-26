from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import*
from second import Ui_SecondWindow

StyleSheet = '''
QPushButton#BlueButton {
    background-color: #DAFFFF;
    border-radius: 8px;}
QPushButton#BlueButton:hover {
    background-color: #01C9C2;
    color: #fff;}
QPushButton#BlueButton:pressed {
    background-color: #84C1BF;}
QPushButton#BlueButton2 {
    background-image: url('Tombol.jpg');
    border-radius: 8px;
    color:white;}
QPushButton#BlueButton2:hover {
    background-image: url('Tombol2.jpg');
    color: black;}
QPushButton#BlueButton2:pressed {
    background-image: url('Tombol3.jpg');}
QPushButton#BlueButton3 {
    background-image: url('menu1.jpg');
    border-radius: 8px;}
QPushButton#BlueButton3:hover {
    background-image: url('menu1_1.jpg');
    color: black;}
QPushButton#BlueButton3:pressed {
    background-image: url('menu1_2.jpg');}
QPushButton#BlueButton4 {
    background-image: url('menu2.jpg');
    border-radius: 8px;}
QPushButton#BlueButton4:hover {
    background-image: url('menu2_1.jpg');
    color: black;}
QPushButton#BlueButton4:pressed {
    background-image: url('menu2_2.jpg');}
QLabel#Judul {
    color: #FFFFFF;
    font-weight: Bold;
    font-size: 30px;}
QLabel#Judul2 {
    background-color: white;
    font-size: 20px;
    border-radius: 8px;}
QComboBox#Menu {
    background-color: #DAFFFF;
    font-size: 13px;
    font-style: italic;
    border-radius: 8px;}
QComboBox#Menu:hover {
    background-color: #01C9C2;
    color: white;}
'''

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.resize(820, 500)
        self.widget = QWidget()
        background = QImage('window.jpg')
        background2 = background.scaled(900, 550)
        pallete = QPalette()
        pallete.setBrush(QPalette.Window, QBrush(background2))

        self.font = QFont()
        self.font.setPointSize(12)
        self.font.setBold(True)

        self.font3 = QFont()
        self.font3.setPointSize(11)

        self.judul = QLabel('CISA\n(Covid-19 Information and Self Checkup Application)',objectName="Judul")
        self.judul.setFixedSize(800,80)
        self.judul.setAlignment(Qt.AlignCenter)

        self.menu = QComboBox(objectName='Menu')
        self.menu.setMinimumSize(0,30)

        self.horizontal = QHBoxLayout()
        self.horizontal.setSpacing(10)

        self.vertikal = QVBoxLayout()
        self.vertikal.addWidget(self.judul)
        self.vertikal.addLayout(self.horizontal)

        self.widget.setLayout(self.vertikal)
        self.tabs(MainWindow)

        MainWindow.setCentralWidget(self.widget)
        MainWindow.setPalette(pallete)
        MainWindow.setWindowTitle( "CISA")

    def tabs(self, MainWindow):
        self.tombol = QPushButton(objectName="BlueButton3")
        self.tombol.setMinimumSize(QSize(0, 255))
        self.tombol.clicked.connect(self.pencet)
        self.tombol2 = QPushButton(objectName="BlueButton4")
        self.tombol2.setMinimumSize(QSize(0, 255))
        self.tombol2.clicked.connect(self.pencet3)

        self.tombol3 = QPushButton('Info Covid-19',objectName="BlueButton")
        self.tombol3.setMinimumSize(QSize(100, 40))
        self.tombol3.setFont(self.font)
        self.tombol3.clicked.connect(self.pencet)
        self.tombol4 = QPushButton('No.Telp Darurat', objectName="BlueButton")
        self.tombol4.setMinimumSize(QSize(100, 40))
        self.tombol4.setFont(self.font)
        self.tombol4.clicked.connect(self.pencet4)
        self.tombol5 = QPushButton('Self Check Up', objectName="BlueButton")
        self.tombol5.setMinimumSize(QSize(100, 40))
        self.tombol5.setFont(self.font)
        self.tombol5.clicked.connect(self.pencet3)
        self.tombol6 = QPushButton('Rumah Sakit Rujukan Covid-19', objectName="BlueButton")
        self.tombol6.setMinimumSize(QSize(100, 40))
        self.tombol6.setFont(self.font)
        self.tombol6.clicked.connect(self.pencet5)

        self.label = QLabel(objectName='Judul2')
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setMinimumSize(20,30)

        self.label2 = QTextEdit()
        self.label2.setFont(self.font3)

        self.horizontal.addWidget(self.tombol)
        self.horizontal.addWidget(self.tombol2)
        self.horizontal.setSpacing(10)
        MainWindow.show()

    def pencet(self):
        self.tombol.close()
        self.tombol2.close()
        self.tombol6.close()
        self.horizontal.replaceWidget(self.tombol,self.tombol3)
        self.horizontal.replaceWidget(self.tombol2,self.tombol4)
        self.horizontal.addWidget(self.tombol5)
        self.label2.show()
        self.menu.show()
        self.menu.clear()

        self.label.setText('Info Covid-19')
        self.buka = open('file', 'r')
        self.buka1 = self.buka.read()
        self.label2.setText(self.buka1)

        self.menu.addItem('.:: Pilih Menu ::.')
        self.menu.addItem('Tips Menghindari Covid-19')
        self.menu.addItem('Gejala Covid-19')
        self.menu.addItem('Komplikasi Covid-19')
        self.menu.addItem('Penyebab Covid-19')

        self.vertikal.addWidget(self.menu)
        self.vertikal.addWidget(self.label)
        self.vertikal.addWidget(self.label2)
        self.menu.activated.connect(self.pilihan)

    def pilihan(self):
        pilihan2=self.menu.currentText()

        if (pilihan2=='Tips Menghindari Covid-19'):
            self.label.setText('Tips & Trik Menghindari Covid-19')
            self.buka2 = open('tips', 'r')
            self.buka3 = self.buka2.read()
            self.label2.setText(self.buka3)
            self.vertikal.addWidget(self.label)
            self.vertikal.addWidget(self.label2)
        if (pilihan2=='Gejala Covid-19'):
            self.label.setText('Gejala-Gejala Covid-19')
            self.buka2 = open('gejala', 'r')
            self.buka3 = self.buka2.read()
            self.label2.setText(self.buka3)
            self.vertikal.addWidget(self.label)
            self.vertikal.addWidget(self.label2)
        if (pilihan2=='Komplikasi Covid-19'):
            self.label.setText('Komplikasi Apabila Terkena Covid-19')
            self.buka2 = open('komplikasi', 'r')
            self.buka3 = self.buka2.read()
            self.label2.setText(self.buka3)
            self.vertikal.addWidget(self.label)
            self.vertikal.addWidget(self.label2)
        if (pilihan2=='Penyebab Covid-19'):
            self.label.setText('Penyebab Covid-19')
            self.buka2 = open('penyebab', 'r')
            self.buka3 = self.buka2.read()
            self.label2.setText(self.buka3)
            self.vertikal.addWidget(self.label)
            self.vertikal.addWidget(self.label2)

    def pencet3(self):
        self.window = QMainWindow()
        self.ui = Ui_SecondWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def pencet4(self):
        telp = QPixmap('telp.jpg')
        telp.scaled(400,255)
        self.label.setPixmap(telp)
        self.menu.close()
        self.label2.close()
        self.vertikal.addWidget(self.tombol6)
        self.tombol6.show()

    def pencet5(self):
        self.label2.show()
        self.tombol6.close()
        self.menu.clear()
        self.menu.show()
        self.label2.close()

        self.label.setText('Silahkan Pilih Daerah')

        self.menu.addItem('.:: Pilih Daerah ::.')
        self.menu.addItem('Kalimantan')
        self.menu.addItem('Sumatera')
        self.menu.addItem('Jawa')
        self.menu.addItem('Bali, NTB, dan NTT')
        self.menu.addItem('Sulawesi')
        self.menu.addItem('Maluku dan Papua')
        self.menu.activated.connect(self.pilihan3)

    def pilihan3(self):
        pilihan2 = self.menu.currentText()
        self.label2.show()

        if (pilihan2 == 'Kalimantan'):
            self.label.setText('Rumah Sakit Rujukan Covid-19 Kalimantan')
            self.buka2 = open('kalimantan', 'r')
            self.buka3 = self.buka2.read()
            self.label2.setText(self.buka3)
            self.vertikal.addWidget(self.label)
            self.vertikal.addWidget(self.label2)
        if (pilihan2 == 'Sumatera'):
            self.label.setText('Rumah Sakit Rujukan Covid-19 Sumatera')
            self.buka2 = open('sumatera', 'r')
            self.buka3 = self.buka2.read()
            self.label2.setText(self.buka3)
            self.vertikal.addWidget(self.label)
            self.vertikal.addWidget(self.label2)
        if (pilihan2 == 'Jawa'):
            self.label.setText('Rumah Sakit Rujukan Covid-19 Jawa')
            self.buka2 = open('jawa', 'r')
            self.buka3 = self.buka2.read()
            self.label2.setText(self.buka3)
            self.vertikal.addWidget(self.label)
            self.vertikal.addWidget(self.label2)
        if (pilihan2 == 'Bali, NTB, dan NTT'):
            self.label.setText('Rumah Sakit Rujukan Covid-19 Bali, NTB, dan NTT')
            self.buka2 = open('dll', 'r')
            self.buka3 = self.buka2.read()
            self.label2.setText(self.buka3)
            self.vertikal.addWidget(self.label)
            self.vertikal.addWidget(self.label2)
        if (pilihan2 == 'Sulawesi'):
            self.label.setText('Rumah Sakit Rujukan Covid-19 Sulawesi')
            self.buka2 = open('sulawesi', 'r')
            self.buka3 = self.buka2.read()
            self.label2.setText(self.buka3)
            self.vertikal.addWidget(self.label)
            self.vertikal.addWidget(self.label2)
        if (pilihan2 == 'Maluku dan Papua'):
            self.label.setText('Rumah Sakit Rujukan Covid-19 Maluku dan Papua')
            self.buka2 = open('mp', 'r')
            self.buka3 = self.buka2.read()
            self.label2.setText(self.buka3)
            self.vertikal.addWidget(self.label)
            self.vertikal.addWidget(self.label2)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    app.setStyleSheet(StyleSheet)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())