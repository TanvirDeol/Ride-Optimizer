import requests
import smtplib 
from sheets import *
from MST import *


#use Google Maps API to find time required to travel between 2 points
def getDist(startP,endP):
    # API key
    api_key = 'AIzaSyAd1VhpgrWABL3Zmc_goQDIVaQBPF7dgdc'
    # base url
    url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&"
    # get response
    r = requests.get(url + "origins=" + startP + "&destinations=" + endP + "&key=" + api_key) 
    # return time as text and as seconds
    time = r.json()["rows"][0]["elements"][0]["duration"]["text"]       
    seconds = r.json()["rows"][0]["elements"][0]["duration"]["value"]
    return [time,seconds]
    

def main():
    driverName = input("Enter your Driver Name\n");
    initSheets()
    [long,lat,address] = getClients(driverName)


if __name__ == "__main__":
    main()