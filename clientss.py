import gspread
import folium
import random
from numpy import add
from pyasn1_modules.rfc2459 import StreetAddress
import webview
import pandas as pd
import streamlit as st
from pandas import DataFrame
import requests
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
from client_class import Client
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

#Set up Google Sheets API
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json",scope)
client = gspread.authorize(creds)
sheet = client.open("test").worksheet("Clients")
data = sheet.get_all_records()
api_key = open("api_key.txt", "r")
API_KEY = api_key.read()
api_key.close()


#Get the length of the dataset
def getLastIndex():
    ids = sheet.col_values(1)
    print(len(ids))
    return len(ids)

#See if a client is willing to talk
def willing_talk():
    talk = input("Talk? (Yes/No)").lower()
    if talk == "yes":
        return True
    if talk == "no":
        return False

#Select an optimal driver for a client, push the client info to the Database    
def getClientInfo(name, age,talk,smoke,lang, startAddress, endAddress):
    client_1 = Client(name, age, talk,smoke,lang, startAddress, endAddress)

    driver = ''
    if client_1.lang.lower() != "english":
        driver = "Driver5"
    elif client_1.talk == True and client_1.smoke == True:
        driver = "Driver1"
    elif client_1.talk == False and client_1.smoke == False:
        driver = "Driver2"
    elif client_1.talk == True and client_1.smoke == False:
        driver = "Driver3"
    elif client_1.talk == False and client_1.smoke == True:
        driver = "Driver4"

    address = client_1.address

    params = {
        'key':API_KEY,
        'address': address
    }

    base_url = 'https://maps.googleapis.com/maps/api/geocode/json?'

    response = requests.get(base_url, params=params).json()
    response.keys()
    sLat = ''
    sLon = ''
    if response['status'] == 'OK':
        geometry= response['results'][0]['geometry']
        sLat = geometry['location']['lat']
        sLon = geometry['location']['lng']
    print(sLat, sLon)

    address = client_1.destination
    params = {
        'key':API_KEY,
        'address': address
    }

    response = requests.get(base_url, params=params).json()
    response.keys()
    eLat = ''
    eLon = ''
    if response['status'] == 'OK':
        geometry= response['results'][0]['geometry']
        eLat = geometry['location']['lat']
        eLon = geometry['location']['lng']
    print(eLat, eLon)

    length = len(sheet.col_values(1)[1:])
    t = "Yes"
    if talk== False: t = "No"
    sm = "Yes"
    if smoke == False: sm= "No"
    l = "Client"+str(length)
    clientData = [l,name,age,t,lang,str(sLat),str(sLon),startAddress,driver,"No",str(eLat),str(eLon),endAddress,sm]
    sheet.insert_row(clientData,length)
    return [sLat,sLon,eLat,eLon]

map_plot_route = folium.Map(location=[38, -98], zoom_start=4)

#Plot an array of locations on a interactive map
def markersView():
    global map_plot_route
    lat = sheet.col_values(6)[1:]
    lon = sheet.col_values(7)[1:]
    print (lat, lon)
    newLat = []
    newLon = []
    for i in range(0,len(lat)):
        newLat.append(float(lat[i]))
        print(float(lat[i]))
    for i in range(0,len(lon)):
        newLon.append(float(lon[i]))
        print(float(lon[i]))

    dict = {}
    for i in range (0,len(lat)):
        dict[i] = [newLat[i],newLon[i]]


    print(dict)
    for i in dict.items():
        print (i[1][0], i[1][1])
        a = float(i[1][0])
        b = float(i[1][1])
        folium.Marker(location = [a, b], popup='city').add_to(map_plot_route)
        #print(a,b)

    #print (df)
    map_plot_route.save('x.html')
    file = open("x.html", "r")
    code = file.read()

    webview.create_window('Hello world', html=code)
    webview.start()

#Plot a route made up of locations on the interactive map
def plotEntireRoute(pickRoute,dropRoute,lat,long,destLat,destLong):
    for i in range(1,len(pickRoute)):
        plotLine(float(lat[pickRoute[i-1]]),float(long[pickRoute[i-1]]),float(lat[pickRoute[i]]),float(long[pickRoute[i]]))
    markersView()
    #file = open("x.html", "r")
    #code = file.read()
    #webview.create_window('Hello world', html=code)
    #webview.start()
    
#Plot a line between 2 locations on the map
def plotLine(firstLat,firstLong,secLat,secLong):
    global map_plot_route
    route_lats_longs = [[firstLat,firstLong],
                        [secLat,secLong]]

    # add route to map
    folium.PolyLine(route_lats_longs).add_to(map_plot_route)

    # display map
    #map_plot_route
    map_plot_route.save('x.html')
    
#Plot blue markers representing location on the map
def plotMarkers(latArr,lonArr):
    dict = {}
    for i in range(0,len(latArr)):
        dict[i] = [float(latArr[i]),float(lonArr[i])]

    map = folium.Map(location=[dict[1][0], dict[1][1]], zoom_start=12)
    for i in dict.items():
        a = i[1][0]
        b = i[1][1]
        folium.Marker(location = [a,b], popup='point').add_to(map)
    
    map.save('map.html')
    file = open("map.html", "r")
    code = file.read()
    return code

    


    

    