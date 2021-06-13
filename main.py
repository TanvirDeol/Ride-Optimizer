import requests
import smtplib 
from sheets import *
from MST import *
from clientss import *

    
def main():
    driverName = input("Enter your Driver Name\n");
    driverName = "Driver1"
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

    #plotEntireRoute(pickUpRoute,dropOffRoute,lat,long,destLat,destLong)

    initDistances(address,destAddress)
    
    #print(long,lat,address)
    #getLastIndex()
    getClientInfo()



if __name__ == "__main__":
    main()