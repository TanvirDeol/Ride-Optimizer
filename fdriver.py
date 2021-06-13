
from PyQt5 import QtCore, QtGui, QtWidgets
from main import *
from sheets import *
from MST import *
from clientss import *
import folium
from numpy import add, datetime64
from pyasn1_modules.rfc2459 import PrivateDomainName
import webview
import folium.plugins as plugins
import datetime
from fclient import *
import threading

pickDistUpdate=[]
pickTimeUpdate=[]
pickFromToUpdate=[]
dropDistUpdate=[]
dropTimeUpdate=[]
dropFromToUpdate=[]
address =[]

cnt =0
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(858, 858)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblDriverName = QtWidgets.QLabel(self.centralwidget)
        self.lblDriverName.setGeometry(QtCore.QRect(110, 30, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(16)
        self.lblDriverName.setFont(font)
        self.lblDriverName.setAlignment(QtCore.Qt.AlignCenter)
        self.lblDriverName.setObjectName("lblDriverName")
        self.txtDriverName = QtWidgets.QLineEdit(self.centralwidget)
        self.txtDriverName.setGeometry(QtCore.QRect(120, 80, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtDriverName.setFont(font)
        self.txtDriverName.setStyleSheet("border-radius:10px;")
        self.txtDriverName.setObjectName("txtDriverName")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 150, 271, 61))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color:#4287f5;\n"
"border-radius: 25px;\n"
"color: white;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.submitDriverInfo)
        self.lblKmDriven = QtWidgets.QLabel(self.centralwidget)
        self.lblKmDriven.setGeometry(QtCore.QRect(30, 390, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(14)
        self.lblKmDriven.setFont(font)
        self.lblKmDriven.setObjectName("lblKmDriven")
        self.lblTimeElapsed = QtWidgets.QLabel(self.centralwidget)
        self.lblTimeElapsed.setGeometry(QtCore.QRect(30, 440, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(14)
        self.lblTimeElapsed.setFont(font)
        self.lblTimeElapsed.setObjectName("lblTimeElapsed")
        self.lblGoingFrom = QtWidgets.QLabel(self.centralwidget)
        self.lblGoingFrom.setGeometry(QtCore.QRect(30, 490, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(14)
        self.lblGoingFrom.setFont(font)
        self.lblGoingFrom.setObjectName("lblGoingFrom")
        self.lblGoingTo = QtWidgets.QLabel(self.centralwidget)
        self.lblGoingTo.setGeometry(QtCore.QRect(30, 540, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(14)
        self.lblGoingTo.setFont(font)
        self.lblGoingTo.setObjectName("lblGoingTo")
        self.lblDashboard = QtWidgets.QLabel(self.centralwidget)
        self.lblDashboard.setGeometry(QtCore.QRect(110, 310, 281, 41))
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
        self.showKmDriven.setGeometry(QtCore.QRect(190, 390, 311, 41))
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
        self.showTimeElapsed.setGeometry(QtCore.QRect(190, 440, 311, 41))
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
        self.showGoingFrom.setGeometry(QtCore.QRect(190, 490, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(8)
        self.showGoingFrom.setFont(font)
        self.showGoingFrom.setStyleSheet("background-color: #4287f5;\n"
"color: white;\n"
"border-radius:10px;")
        self.showGoingFrom.setAlignment(QtCore.Qt.AlignCenter)
        self.showGoingFrom.setObjectName("showGoingFrom")
        self.showGoingTo = QtWidgets.QLabel(self.centralwidget)
        self.showGoingTo.setGeometry(QtCore.QRect(190, 540, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(8)
        self.showGoingTo.setFont(font)
        self.showGoingTo.setStyleSheet("background-color: #4287f5;\n"
"color: white;\n"
"border-radius:10px;")
        self.showGoingTo.setAlignment(QtCore.Qt.AlignCenter)
        self.showGoingTo.setObjectName("showGoingTo")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(540, 40, 291, 751))
        self.textBrowser.setStyleSheet("background-color:black;\n"
"color:white;")
        self.textBrowser.setObjectName("textBrowser")
        self.lblResults = QtWidgets.QLabel(self.centralwidget)
        self.lblResults.setGeometry(QtCore.QRect(130, 620, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(16)
        self.lblResults.setFont(font)
        self.lblResults.setObjectName("lblResults")
        self.lblGasSaved = QtWidgets.QLabel(self.centralwidget)
        self.lblGasSaved.setGeometry(QtCore.QRect(30, 690, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(14)
        self.lblGasSaved.setFont(font)
        self.lblGasSaved.setObjectName("lblGasSaved")
        self.lblTimeSaved = QtWidgets.QLabel(self.centralwidget)
        self.lblTimeSaved.setGeometry(QtCore.QRect(30, 750, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(14)
        self.lblTimeSaved.setFont(font)
        self.lblTimeSaved.setObjectName("lblTimeSaved")
        self.showGasSaved = QtWidgets.QLabel(self.centralwidget)
        self.showGasSaved.setGeometry(QtCore.QRect(190, 690, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(14)
        self.showGasSaved.setFont(font)
        self.showGasSaved.setStyleSheet("background-color: #4287f5;\n"
"color: white;\n"
"border-radius:10px;")
        self.showGasSaved.setAlignment(QtCore.Qt.AlignCenter)
        self.showGasSaved.setObjectName("showGasSaved")
        self.showTimeSaved = QtWidgets.QLabel(self.centralwidget)
        self.showTimeSaved.setGeometry(QtCore.QRect(190, 750, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(14)
        self.showTimeSaved.setFont(font)
        self.showTimeSaved.setStyleSheet("background-color: #4287f5;\n"
"color: white;\n"
"border-radius:10px;")
        self.showTimeSaved.setAlignment(QtCore.Qt.AlignCenter)
        self.showTimeSaved.setObjectName("showTimeSaved")
        self.btnUpdate = QtWidgets.QPushButton(self.centralwidget)
        self.btnUpdate.setGeometry(QtCore.QRect(120, 230, 271, 61))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(16)
        self.btnUpdate.setFont(font)
        self.btnUpdate.setStyleSheet("background-color:#4287f5;\n"
"border-radius: 25px;\n"
"color: white;")
        self.btnUpdate.setObjectName("btnUpdate")
        self.btnUpdate.clicked.connect(self.updateInfo)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 858, 26))
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
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.lblResults.setText(_translate("MainWindow", "Sustainability Results:"))
        self.lblGasSaved.setText(_translate("MainWindow", "Gas Saved:"))
        self.lblTimeSaved.setText(_translate("MainWindow", "Time Saved:"))
        self.showGasSaved.setText(_translate("MainWindow", "0"))
        self.showTimeSaved.setText(_translate("MainWindow", "0"))
        self.btnUpdate.setText(_translate("MainWindow", "Update"))

    def submitDriverInfo(self):
        global pickDistUpdate
        global pickTimeUpdate
        global pickFromToUpdate
        global dropDistUpdate
        global dropTimeUpdate
        global dropFromToUpdate
        global address
        driverName = self.txtDriverName.text()
        initSheets()
        [long,lat,address,destLat,destLong,destAddress] = getClients(driverName)
        lat.insert(0,'43.578842');
        long.insert(0,'-79.683668');
        address.insert(0,'1240 Eglinton Ave W, Mississauga, ON L5V 1N3');
        destLat.insert(0,'43.578842');
        destLong.insert(0,'-79.683668');
        destAddress.insert(0,'1240 Eglinton Ave W, Mississauga, ON L5V 1N3');

        initDistances(address,destAddress)
        pickUpGraph = createGraph(address,0)
        pickUpMst = minSpanningTree(pickUpGraph,len(address))
        [pickUpRoute,pickDistUpdate,pickTimeUpdate,pickFromToUpdate] = getTravelRoute(pickUpMst,len(address),address,0)
        mstClear()
        print()

        dropOffGraph = createGraph(destAddress,1)
        dropOffMst = minSpanningTree(dropOffGraph,len(destAddress))
        [dropOffRoute,dropDistUpdate,dropTimeUpdate,dropFromToUpdate] = getTravelRoute(dropOffMst,len(destAddress),destAddress,1)
        mstClear()

        
        #print(lat,"\n",long)
        print(pickUpRoute,"\n",pickDistUpdate,"\n",pickTimeUpdate,"\n",pickFromToUpdate)
        self.drawRoute(lat = lat,long = long,travelRoute = pickUpRoute)

    def updateInfo(self):
        #threading.Timer(2.0, self.updateInfo).start()
        global pickDistUpdate
        global pickTimeUpdate
        global pickFromToUpdate
        global dropDistUpdate
        global dropTimeUpdate
        global dropFromToUpdate
        global cnt
        
        curDist = float(self.showKmDriven.text()[:-2])
        curTime = float(self.showTimeElapsed.text()[:-1])
        if cnt >=len(dropDistUpdate):
            [slowDist,slowTime] = calculateSlowCost(len(address))
            timeSaved = abs(curTime-slowTime)
            distSaved = abs(curDist-slowDist)
            self.showTimeSaved.setText(str("{:.2f}".format(timeSaved))+" min")
            self.showGasSaved.setText(str("{:.2f}".format(distSaved))+" km")
            return 0
        
        curDist += pickDistUpdate[cnt]
        curTime += float(pickTimeUpdate[cnt][:-4])
        curFrom = pickFromToUpdate[cnt][0]
        curTo = pickFromToUpdate[cnt][1]

        self.showKmDriven.setText(str("{:.2f}".format(curDist))+" km")
        self.showTimeElapsed.setText(str("{:.2f}".format(curTime))+" m")
        self.showGoingFrom.setText(curFrom)
        self.showGoingTo.setText(curTo)

        cnt+=1

    def drawRoute(self,lat,long,travelRoute):
        x = datetime.datetime.now()
        lines = []
        colors = ["red","blue","yellow","green","orange"]
        for i in range(1,len(travelRoute)):
                s = ""
                idx = i%5
                s = colors[idx]
                a = x.strftime("%Y-%m-%d %H:%M:%S")
                x+=datetime.timedelta(minutes=10)
                b = x.strftime("%Y-%m-%d %H:%M:%S")
                lines.append({
                "coordinates":[
                        [float(long[travelRoute[i-1]]),float(lat[travelRoute[i-1]])],
                        [float(long[travelRoute[i]]),float(lat[travelRoute[i]])],
                ],
                "dates": [a,b],
                "color":s,
                })

        #pprint(lines)
        m = folium.Map(location= [float(lat[travelRoute[0]]),float(long[travelRoute[0]])], zoom_start=12)
        # Lon, Lat order.
       
        features = [
                {
                "type": "Feature",
                "geometry": {
                        "type": "LineString",
                        "coordinates": line["coordinates"],
                },
                "properties": {
                        "times": line["dates"],
                        "style": {
                        "color": line["color"],
                        "weight": line["weight"] if "weight" in line else 5,
                        },
                },
                }
                for line in lines
        ]
        print()
        #lines[i]['coordinates'][0] = [lat,long]
        #lines[i]['color']= 'red'
        #lines[i]['dates'][0/1] = '2017-06-02T00:00:00'
        plugins.TimestampedGeoJson(
                {
                "type": "FeatureCollection",
                "features": features,
                },
                period="PT1M",
                add_last_point=True,
        ).add_to(m)

        m.save('x.html')
        file = open("x.html", "r")
        code = file.read()
        webview.create_window('Hello world', html=code)
        webview.start()
        #threading.Timer(2.0, self.updateInfo).start()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
