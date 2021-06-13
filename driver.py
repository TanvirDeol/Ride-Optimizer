from PyQt5 import QtCore, QtGui, QtWidgets
from main import *
from sheets import *
from MST import *
from test import *
from clientss import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(359, 607)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblDriverName = QtWidgets.QLabel(self.centralwidget)
        self.lblDriverName.setGeometry(QtCore.QRect(30, 20, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(16)
        self.lblDriverName.setFont(font)
        self.lblDriverName.setAlignment(QtCore.Qt.AlignCenter)
        self.lblDriverName.setObjectName("lblDriverName")
        self.txtDriverName = QtWidgets.QLineEdit(self.centralwidget)
        self.txtDriverName.setGeometry(QtCore.QRect(40, 70, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtDriverName.setFont(font)
        self.txtDriverName.setStyleSheet("border-radius:10px;")
        self.txtDriverName.setObjectName("txtDriverName")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 140, 271, 61))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color:#4287f5;\n"
"border-radius: 25px;\n"
"color: white;\n")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.submitDriverInfo)
        self.lblKmDriven = QtWidgets.QLabel(self.centralwidget)
        self.lblKmDriven.setGeometry(QtCore.QRect(30, 330, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(14)
        self.lblKmDriven.setFont(font)
        self.lblKmDriven.setObjectName("lblKmDriven")
        self.lblTimeElapsed = QtWidgets.QLabel(self.centralwidget)
        self.lblTimeElapsed.setGeometry(QtCore.QRect(30, 380, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(14)
        self.lblTimeElapsed.setFont(font)
        self.lblTimeElapsed.setObjectName("lblTimeElapsed")
        self.lblGoingFrom = QtWidgets.QLabel(self.centralwidget)
        self.lblGoingFrom.setGeometry(QtCore.QRect(30, 430, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(14)
        self.lblGoingFrom.setFont(font)
        self.lblGoingFrom.setObjectName("lblGoingFrom")
        self.lblGoingTo = QtWidgets.QLabel(self.centralwidget)
        self.lblGoingTo.setGeometry(QtCore.QRect(30, 480, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(14)
        self.lblGoingTo.setFont(font)
        self.lblGoingTo.setObjectName("lblGoingTo")
        self.lblDashboard = QtWidgets.QLabel(self.centralwidget)
        self.lblDashboard.setGeometry(QtCore.QRect(30, 260, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lblDashboard.setFont(font)
        self.lblDashboard.setScaledContents(False)
        self.lblDashboard.setAlignment(QtCore.Qt.AlignCenter)
        self.lblDashboard.setObjectName("lblDashboard")
        self.showKmDriven = QtWidgets.QLabel(self.centralwidget)
        self.showKmDriven.setGeometry(QtCore.QRect(190, 330, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(14)
        self.showKmDriven.setFont(font)
        self.showKmDriven.setStyleSheet("background-color: #4287f5;\n"
"color: white;\n"
"border-radius:10px;")
        self.showKmDriven.setAlignment(QtCore.Qt.AlignCenter)
        self.showKmDriven.setObjectName("showKmDriven")
        self.showTimeElapsed = QtWidgets.QLabel(self.centralwidget)
        self.showTimeElapsed.setGeometry(QtCore.QRect(190, 380, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(14)
        self.showTimeElapsed.setFont(font)
        self.showTimeElapsed.setStyleSheet("background-color: #4287f5;\n"
"color: white;\n"
"border-radius:10px;")
        self.showTimeElapsed.setAlignment(QtCore.Qt.AlignCenter)
        self.showTimeElapsed.setObjectName("showTimeElapsed")
        self.showGoingFrom = QtWidgets.QLabel(self.centralwidget)
        self.showGoingFrom.setGeometry(QtCore.QRect(190, 430, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(14)
        self.showGoingFrom.setFont(font)
        self.showGoingFrom.setStyleSheet("background-color: #4287f5;\n"
"color: white;\n"
"border-radius:10px;")
        self.showGoingFrom.setAlignment(QtCore.Qt.AlignCenter)
        self.showGoingFrom.setObjectName("showGoingFrom")
        self.showGoingTo = QtWidgets.QLabel(self.centralwidget)
        self.showGoingTo.setGeometry(QtCore.QRect(190, 480, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(14)
        self.showGoingTo.setFont(font)
        self.showGoingTo.setStyleSheet("background-color: #4287f5;\n"
"color: white;\n"
"border-radius:10px;")
        self.showGoingTo.setAlignment(QtCore.Qt.AlignCenter)
        self.showGoingTo.setObjectName("showGoingTo")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 359, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Driver Side Client"))
        self.lblDriverName.setText(_translate("MainWindow", "Enter your Driver Name"))
        self.pushButton.setText(_translate("MainWindow", "Submit"))
        self.lblKmDriven.setText(_translate("MainWindow", "KM Driven:"))
        self.lblTimeElapsed.setText(_translate("MainWindow", "Time Elapsed:"))
        self.lblGoingFrom.setText(_translate("MainWindow", "Going From:"))
        self.lblGoingTo.setText(_translate("MainWindow", "Going From:"))
        self.lblDashboard.setText(_translate("MainWindow", "Dashboard"))
        self.showKmDriven.setText(_translate("MainWindow", "0 km"))
        self.showTimeElapsed.setText(_translate("MainWindow", "0 m"))
        self.showGoingFrom.setText(_translate("MainWindow", "TBD"))
        self.showGoingTo.setText(_translate("MainWindow", "TBD"))

    def submitDriverInfo(self):
        driverName = self.txtDriverName.text()
        initSheets()
        [long,lat,address,destLat,destLong,destAddress] = getClients(driverName)
        lat.insert(0,'43.45324');
        long.insert(0,'-80.56395');
        address.insert(0,'104 McCrae Pl, Waterloo, ON N2T 1C6');
        destLat.insert(0,'43.45324');
        destLong.insert(0,'-80.56395');
        destAddress.insert(0,'104 McCrae Pl, Waterloo, ON N2T 1C6');

        pickUpGraph = createGraph(address)
        pickUpMst = minSpanningTree(pickUpGraph,len(address))
        pickUpRoute = getTravelRoute(pickUpMst,len(address))
        mstClear()
        print()

        dropOffGraph = createGraph(destAddress)
        dropOffMst = minSpanningTree(dropOffGraph,len(destAddress))
        dropOffRoute = getTravelRoute(dropOffMst,len(destAddress))
        mstClear()

        print(lat,"\n",long)

        drawRoute(pickUpRoute,lat,long)

        #plotEntireRoute(pickUpRoute,dropOffRoute,lat,long,destLat,destLong)

        #initDistances(address,destAddress)





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
