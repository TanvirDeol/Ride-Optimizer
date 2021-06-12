import gspread
import folium
import random
import webview
import pandas as pd
import streamlit as st
from pandas import DataFrame
import requests
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
from client_class import Client
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]


creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json",scope)

client = gspread.authorize(creds)

sheet = client.open("test").worksheet("Clients")


data = sheet.get_all_records()


def getLastIndex():
    ids = sheet.col_values(1)
    print(len(ids))
    return len(ids)

def willing_talk():
    talk = input("Also, would you like to socialize on this trip or do you prefer a quite ride? Yes or no? ").lower()
    if talk == "yes":
        return True
    if talk == "no":
        return False
        
def getClientInfo():
    name = input("Hi, what is your name? ")
    age = input("If you dont mind us asking, how old are you? ")


    destination = input("Where are you looking to go today? Please enter full address")


    client_1 = Client(name, age, willing_talk(), destination)

    if client_1.talk == True:
        print("You have been paired with driver 1")
    elif client_1.talk == False:
        print("You have been paired with driver 2")

    api_key = open("api_key.txt", "r")
    API_KEY = api_key.read()
    api_key.close()
    address = client_1.destination

    params = {
        'key':API_KEY,
        'address': address

    }

    base_url = 'https://maps.googleapis.com/maps/api/geocode/json?'

    response = requests.get(base_url, params=params).json()
    response.keys()
    lat = ''
    lon = ''
    if response['status'] == 'OK':
        geometry= response['results'][0]['geometry']
        lat = geometry['location']['lat']
        lon = geometry['location']['lng']

    print(lat, lon)
    return [lat, lon]

[lat, lon]= getClientInfo()

m = folium.Map(location=[43.7315, -79.7624], tiles="OpenStreetMap", zoom_start=12)
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

df = DataFrame({'Latitude':[newLat], 'Longitude':[newLon]})
for i in dict.items():
    print (i[1][0], i[1][1])
    a = float(i[1][0])
    b = float(i[1][1])
    folium.Marker(location = [a, b], popup='city').add_to(m)
    #print(a,b)

 
print (df)
m.save('x.html')
file = open("x.html", "r")
code = file.read()

webview.create_window('Hello world', html=code)
webview.start()