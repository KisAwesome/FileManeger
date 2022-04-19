import os
from PyQt6 import QtCore, QtGui, QtWidgets
import sys
import webbrowser
import zono.search as search

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(758, 600)
        self.current_dir = 'c:'
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(50, 140, 641, 371))
        self.listWidget.setObjectName("listWidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(210, 110, 171, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 110, 55, 16))
        self.label.setObjectName("label")
        self.last = ''
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 0, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(180, 0, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(270, 0, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.selected = ''
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 758, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def refresh(self,Dir):
        ex = os.listdir(Dir)
        self.listWidget.clear()
        for i in ex:
            elm = i
            if os.path.isdir(f'{self.current_dir}/{i}'):
                elm = f'Folder {i}'
            self.listWidget.addItem(elm)
            self.listWidget.addItem('')
    def open_(self):
        if not self.selected:
            return 0
        lo = self.selected.replace('Folder','').strip()
        hold = f'{self.current_dir}/{lo}'
        if not 'Folder' in self.selected:
            webbrowser.open(hold)
            return 0
        # self.last = self.current_dir
        self.current_dir = hold
        self.refresh(hold)
    def cut(self,oath):
        raw = '\\'
        r = list(raw)
        # print(r)

        cath = list(oath)
        for i in oath:
            var = cath.pop()
            if var == '/' or var == raw:
                break
        return ''.join(cath)

        
    def onselect(self, text):
        print(text.text())
        self.selected = text.text()
    def back(self):
        new = self.cut(self.current_dir)
        print(new)
        self.refresh(new+'/')
        # load = os.listdir(self.last)
        # self.listWidget.clear()
        # for i in load:
        #         elm = i
        #         if os.path.isdir(f'{self.current_dir}/{i}'):
        #             elm = f'Folder {i}'
        #         self.listWidget.addItem(elm)
        #         self.listWidget.addItem('')
    # def search(self):
    #     if not self.lineEdit.text():
    #         self.refresh(self.current_dir)
    #         return 0
    #     list_ = os.listdir(self.current_dir)
    #     for i in list_:
    #         if 'Folder' in i:
                





    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Search:"))
        self.pushButton.setText(_translate("MainWindow", "delete"))
        self.pushButton_2.setText(_translate("MainWindow", "open"))
        self.pushButton_3.setText(_translate("MainWindow", "copypath"))
        self.listWidget.itemClicked.connect(self.onselect)
        self.pushButton_4.setText(_translate("MainWindow", "back"))
        self.pushButton_4.clicked.connect(self.back)

        # self.lineEdit.textChanged.connect(self.search)
        self.pushButton_2.clicked.connect(self.open_)
        self.refresh(Dir='/')




app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec())
