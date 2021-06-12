import requests
import smtplib 
from sheets import *
from MST import *
from clientss import *

    
def main():
    #driverName = input("Enter your Driver Name\n");
    driverName = "Driver1"
    initSheets()
    [long,lat,address] = getClients(driverName)
    address.insert(0,'104 McCrae Pl, Waterloo, ON N2T 1C6');
    graph = createGraph(address)
    mst = minSpanningTree(graph,len(address))
    getTravelRoute(mst,len(address))
    

    #print(long,lat,address)
    #getLastIndex()



if __name__ == "__main__":
    main()