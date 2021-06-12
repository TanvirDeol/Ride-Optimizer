import requests
import smtplib 
from sheets import *
from MST import *
from clientss import *

    
def main():
    #driverName = input("Enter your Driver Name\n");
    driverName = "Driver1"
    initSheets()
    [long,lat,address,destLat,destLong,destAddress] = getClients(driverName)
    address.insert(0,'104 McCrae Pl, Waterloo, ON N2T 1C6');
    destAddress.insert(0,'104 McCrae Pl, Waterloo, ON N2T 1C6');

    pickUpGraph = createGraph(address)
    pickUpMst = minSpanningTree(pickUpGraph,len(address))
    pickupRoute = getTravelRoute(pickUpMst,len(address))
    mstClear()
    print()

    dropOffGraph = createGraph(destAddress)
    dropOffMst = minSpanningTree(dropOffGraph,len(destAddress))
    dropOffRoute = getTravelRoute(dropOffMst,len(destAddress))
    mstClear()

    #print(long,lat,address)
    #getLastIndex()



if __name__ == "__main__":
    main()