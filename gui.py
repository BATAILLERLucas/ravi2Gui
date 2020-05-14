import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QWidget, QVBoxLayout, QTabWidget, QPushButton, \
    QLineEdit, QInputDialog


class Gui(QMainWindow):

     def __init__(self):
        super().__init__()
        self.initUI()

     def initUI(self):
        self.statusBar().showMessage('Ready')

        menubar = self.menuBar()
        fichierMenu = menubar.addMenu("Fichier")

        openAct = QAction("Ouvrir", self)
        openAct.triggered.connect(self.open)
        openAct.setShortcut('ctrl+O')
        openAct.setStatusTip('Ouvrir un fichier')

        reAct = QAction("Enregistrer", self)
        openAct.triggered.connect(self.rec)
        openAct.setShortcut('ctrl+S')
        openAct.setStatusTip('Enregister un fichier')

        quitAct = QAction("Quitter", self)
        openAct.triggered.connect(self.exit)
        openAct.setShortcut('ctrl+Q')
        openAct.setStatusTip('Quitter un fichier')

        fichierMenu.addAction(openAct)
        fichierMenu.addSeparator()
        fichierMenu.addAction(reAct)
        fichierMenu.addAction(quitAct)

        self.setMinimumSize(1280, 720)
        self.setWindowTitle('fenetre speciale')
        self.myWidget = MyTableWidget
        self.setCentralWidget(self.myWidget)
        self.show()

     def open(self):
      print("open")

     def rec(self):
      print("rec")

     def exit(self):
      print("exit")


class MyTableWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tabs.resize(300, 200)

        # Add tabs
        self.tabs.addTab(self.tab1, "Onglet 1")
        self.tabs.addTab(self.tab2, "Onglet 2")

        self.tab1.layout = QVBoxLayout(self)
        openButton = QPushButton("Non?")
        openButton.clicked.connect(self.openClick)

        self.tab1.layout.addWidget(openButton)
        self.tab1.setlayout(self.tab1.layout)



        # Create first tab
        self.tab1.layout = QVBoxLayout(self)
        self.pushButton1 = QPushButton("PyQt5 button")
        self.tab1.layout.addWidget(self.pushButton1)
        self.tab1.setLayout(self.tab1.layout)

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    def openClick(self):
         print("click")
         non,reponse = QInputDialog.getText(self,"input dialog", "Votre nom ?",QLineEdit.Normal,"")
         print(nom)
