from PyQt5 import QtCore, QtGui, QtWidgets
from clientss import *

#This is the client side app
#PyQt5 GUI set up. This initilizes all the buttons and labels in the app
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(305, 849)
        font = QtGui.QFont()
        font.setPointSize(9)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.txtName = QtWidgets.QLineEdit(self.centralwidget)
        self.txtName.setGeometry(QtCore.QRect(40, 170, 221, 31))
        self.txtName.setStyleSheet("border-radius:10px;\n"
"")
        self.txtName.setObjectName("txtName")
        self.txtAge = QtWidgets.QLineEdit(self.centralwidget)
        self.txtAge.setGeometry(QtCore.QRect(40, 250, 221, 31))
        self.txtAge.setStyleSheet("border-radius:10px;\n"
"")
        self.txtAge.setObjectName("txtAge")
        self.txtTalk = QtWidgets.QLineEdit(self.centralwidget)
        self.txtTalk.setGeometry(QtCore.QRect(40, 330, 221, 31))
        self.txtTalk.setStyleSheet("border-radius:10px;\n"
"")
        self.txtTalk.setObjectName("txtTalk")
        self.txtHomeAddress = QtWidgets.QLineEdit(self.centralwidget)
        self.txtHomeAddress.setGeometry(QtCore.QRect(40, 570, 221, 31))
        self.txtHomeAddress.setStyleSheet("border-radius:10px;\n"
"")
        self.txtHomeAddress.setObjectName("txtHomeAddress")
        self.txtDestAddress = QtWidgets.QLineEdit(self.centralwidget)
        self.txtDestAddress.setGeometry(QtCore.QRect(40, 650, 221, 31))
        self.txtDestAddress.setStyleSheet("border-radius:10px;\n"
"")
        self.txtDestAddress.setObjectName("txtDestAddress")
        self.lblName = QtWidgets.QLabel(self.centralwidget)
        self.lblName.setGeometry(QtCore.QRect(40, 140, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(14)
        self.lblName.setFont(font)
        self.lblName.setStyleSheet("color:rgb(35, 35, 35);")
        self.lblName.setObjectName("lblName")
        self.lblAge = QtWidgets.QLabel(self.centralwidget)
        self.lblAge.setGeometry(QtCore.QRect(40, 220, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(14)
        self.lblAge.setFont(font)
        self.lblAge.setStyleSheet("color:rgb(35, 35, 35);")
        self.lblAge.setObjectName("lblAge")
        self.lblTalk = QtWidgets.QLabel(self.centralwidget)
        self.lblTalk.setGeometry(QtCore.QRect(40, 300, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(14)
        self.lblTalk.setFont(font)
        self.lblTalk.setStyleSheet("color:rgb(35, 35, 35);")
        self.lblTalk.setObjectName("lblTalk")
        self.lblHomeAddress = QtWidgets.QLabel(self.centralwidget)
        self.lblHomeAddress.setGeometry(QtCore.QRect(40, 540, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(14)
        self.lblHomeAddress.setFont(font)
        self.lblHomeAddress.setStyleSheet("color:rgb(35, 35, 35);")
        self.lblHomeAddress.setObjectName("lblHomeAddress")
        self.lblDestAddress = QtWidgets.QLabel(self.centralwidget)
        self.lblDestAddress.setGeometry(QtCore.QRect(40, 620, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(14)
        self.lblDestAddress.setFont(font)
        self.lblDestAddress.setStyleSheet("color:rgb(35, 35, 35);")
        self.lblDestAddress.setObjectName("lblDestAddress")
        self.btnSubmit = QtWidgets.QPushButton(self.centralwidget)
        self.btnSubmit.setGeometry(QtCore.QRect(40, 720, 221, 61))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(12)
        self.btnSubmit.setFont(font)
        self.btnSubmit.setStyleSheet("background-color:#286fc7;\n"
"color:whitesmoke;\n"
"border-radius: 25px;")
        self.btnSubmit.setObjectName("btnSubmit")
        self.btnSubmit.clicked.connect(self.submitClientInfo)
        self.txtSmoke = QtWidgets.QLineEdit(self.centralwidget)
        self.txtSmoke.setGeometry(QtCore.QRect(40, 410, 221, 31))
        self.txtSmoke.setStyleSheet("border-radius:10px;\n"
"")
        self.txtSmoke.setObjectName("txtSmoke")
        self.lblSmoke = QtWidgets.QLabel(self.centralwidget)
        self.lblSmoke.setGeometry(QtCore.QRect(40, 380, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(14)
        self.lblSmoke.setFont(font)
        self.lblSmoke.setStyleSheet("color:rgb(35, 35, 35);")
        self.lblSmoke.setObjectName("lblSmoke")
        self.txtLang = QtWidgets.QLineEdit(self.centralwidget)
        self.txtLang.setGeometry(QtCore.QRect(40, 490, 221, 31))
        self.txtLang.setStyleSheet("border-radius:10px;\n"
"")
        self.txtLang.setObjectName("txtLang")
        self.lblLang = QtWidgets.QLabel(self.centralwidget)
        self.lblLang.setGeometry(QtCore.QRect(40, 460, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(14)
        self.lblLang.setFont(font)
        self.lblLang.setStyleSheet("color:rgb(35, 35, 35);")
        self.lblLang.setObjectName("lblLang")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 10, 171, 61))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Logo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.lblName_2 = QtWidgets.QLabel(self.centralwidget)
        self.lblName_2.setGeometry(QtCore.QRect(30, 80, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(18)
        self.lblName_2.setFont(font)
        self.lblName_2.setStyleSheet("color:rgb(35, 35, 35);")
        self.lblName_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lblName_2.setObjectName("lblName_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 305, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    #Part of the automatic GUI setup
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RideOptimizer Client "))
        self.lblName.setText(_translate("MainWindow", "Name"))
        self.lblAge.setText(_translate("MainWindow", "Age"))
        self.lblTalk.setText(_translate("MainWindow", "Talk (Yes/No)?"))
        self.lblHomeAddress.setText(_translate("MainWindow", "Home Address"))
        self.lblDestAddress.setText(_translate("MainWindow", "Destination"))
        self.btnSubmit.setText(_translate("MainWindow", "Submit"))
        self.lblSmoke.setText(_translate("MainWindow", "Smoke (Yes/No)?"))
        self.lblLang.setText(_translate("MainWindow", "Primary Language"))
        self.lblName_2.setText(_translate("MainWindow", "Client Application"))

    #Submits client info to DB and shows start and end points on map
    def submitClientInfo(self):
        name = self.txtName.text()
        age = self.txtAge.text()
        talk = False
        if self.txtTalk.text().lower()[0]=='y':
            talk = True
        smoke = False
        if self.txtSmoke.text().lower()[0]=='y':
            smoke=True
        lang = self.txtLang.text()
        homeAdd = self.txtHomeAddress.text()
        destAdd = self.txtDestAddress.text()
        print(name,age,talk,homeAdd,destAdd)

        [sLat,sLon,eLat,eLon] = getClientInfo(name,age,talk,smoke,lang,homeAdd,destAdd)

        code = plotMarkers([sLat,eLat],[sLon,eLon])
        webview.create_window('Home to Destination', html=code)
        webview.start()
        #make a window with the markers of driver and client


#GUI Main method
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
