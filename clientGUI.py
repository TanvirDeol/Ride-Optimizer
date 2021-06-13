from PyQt5 import QtCore, QtGui, QtWidgets
from clientss import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(319, 621)
        font = QtGui.QFont()
        font.setPointSize(9)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.txtName = QtWidgets.QLineEdit(self.centralwidget)
        self.txtName.setGeometry(QtCore.QRect(40, 90, 221, 31))
        self.txtName.setStyleSheet("border-radius:10px;\n"
"")
        self.txtName.setObjectName("txtName")
        self.txtAge = QtWidgets.QLineEdit(self.centralwidget)
        self.txtAge.setGeometry(QtCore.QRect(40, 170, 221, 31))
        self.txtAge.setStyleSheet("border-radius:10px;\n"
"")
        self.txtAge.setObjectName("txtAge")
        self.txtTalk = QtWidgets.QLineEdit(self.centralwidget)
        self.txtTalk.setGeometry(QtCore.QRect(40, 250, 221, 31))
        self.txtTalk.setStyleSheet("border-radius:10px;\n"
"")
        self.txtTalk.setObjectName("txtTalk")
        self.txtHomeAddress = QtWidgets.QLineEdit(self.centralwidget)
        self.txtHomeAddress.setGeometry(QtCore.QRect(40, 330, 221, 31))
        self.txtHomeAddress.setStyleSheet("border-radius:10px;\n"
"")
        self.txtHomeAddress.setObjectName("txtHomeAddress")
        self.txtDestAddress = QtWidgets.QLineEdit(self.centralwidget)
        self.txtDestAddress.setGeometry(QtCore.QRect(40, 410, 221, 31))
        self.txtDestAddress.setStyleSheet("border-radius:10px;\n"
"")
        self.txtDestAddress.setObjectName("txtDestAddress")
        self.lblName = QtWidgets.QLabel(self.centralwidget)
        self.lblName.setGeometry(QtCore.QRect(40, 60, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(14)
        self.lblName.setFont(font)
        self.lblName.setStyleSheet("color:rgb(35, 35, 35);")
        self.lblName.setObjectName("lblName")
        self.lblAge = QtWidgets.QLabel(self.centralwidget)
        self.lblAge.setGeometry(QtCore.QRect(40, 140, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(14)
        self.lblAge.setFont(font)
        self.lblAge.setStyleSheet("color:rgb(35, 35, 35);")
        self.lblAge.setObjectName("lblAge")
        self.lblTalk = QtWidgets.QLabel(self.centralwidget)
        self.lblTalk.setGeometry(QtCore.QRect(40, 220, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(14)
        self.lblTalk.setFont(font)
        self.lblTalk.setStyleSheet("color:rgb(35, 35, 35);")
        self.lblTalk.setObjectName("lblTalk")
        self.lblHomeAddress = QtWidgets.QLabel(self.centralwidget)
        self.lblHomeAddress.setGeometry(QtCore.QRect(40, 300, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(14)
        self.lblHomeAddress.setFont(font)
        self.lblHomeAddress.setStyleSheet("color:rgb(35, 35, 35);")
        self.lblHomeAddress.setObjectName("lblHomeAddress")
        self.lblDestAddress = QtWidgets.QLabel(self.centralwidget)
        self.lblDestAddress.setGeometry(QtCore.QRect(40, 380, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(14)
        self.lblDestAddress.setFont(font)
        self.lblDestAddress.setStyleSheet("color:rgb(35, 35, 35);")
        self.lblDestAddress.setObjectName("lblDestAddress")
        self.btnSubmit = QtWidgets.QPushButton(self.centralwidget)
        self.btnSubmit.setGeometry(QtCore.QRect(40, 480, 221, 61))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(12)
        self.btnSubmit.setFont(font)
        self.btnSubmit.setStyleSheet("background-color:#286fc7;\n"
"color:whitesmoke;\n"
"border-radius: 25px;")
        self.btnSubmit.setObjectName("btnSubmit")
        self.btnSubmit.clicked.connect(self.submitClientInfo)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 319, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RideOptimizer Client "))
        self.lblName.setText(_translate("MainWindow", "Name"))
        self.lblAge.setText(_translate("MainWindow", "Age"))
        self.lblTalk.setText(_translate("MainWindow", "Talk (Yes/No)?"))
        self.lblHomeAddress.setText(_translate("MainWindow", "Home Address"))
        self.lblDestAddress.setText(_translate("MainWindow", "Destination"))
        self.btnSubmit.setText(_translate("MainWindow", "Submit"))

    def submitClientInfo(self):
        name = self.txtName.text()
        age = self.txtAge.text()
        talk = False
        if self.txtTalk.text().lower()[0]=='y':
            talk = True
        homeAdd = self.txtHomeAddress.text()
        destAdd = self.txtDestAddress.text()
        print(name,age,talk,homeAdd,destAdd)

        [sLat,sLon,eLat,eLon] = getClientInfo(name,age,talk,homeAdd,destAdd)

        code = plotMarkers([sLat,eLat],[sLon,eLon])
        webview.create_window('Home to Destination', html=code)
        webview.start()
        #make a window with the markers of driver and client
        



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
