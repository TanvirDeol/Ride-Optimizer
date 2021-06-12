import gspread
import requests
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
from client_class import Client
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]


creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json",scope)

client = gspread.authorize(creds)

sheet = client.open("test").sheet1

data = sheet.get_all_records()

pprint(data)


name = input("Hi, what is your name? ")
age = input("If you dont mind us asking, how old are you? ")
def willing_talk():
    talk = input("Also, would you like to socialize on this trip or do you prefer a quite ride? Yes or no? ").lower()
    if talk == "yes":
        return True
    if talk == "no":
        return False

destination = input("Where are you looking to go today? Please enter full address")


client_1 = Client(name, age, willing_talk(), destination)

if client_1.talk == True:
    print("You have been paired with driver 1")
elif client_1.talk == False:
    print("You have been paired with driver 2")

API_KEY = 'AIzaSyAd1VhpgrWABL3Zmc_goQDIVaQBPF7dgdc'
address = client_1.destination

params = {
    'key':API_KEY,
     'address': address

}

base_url = 'https://maps.googleapis.com/maps/api/geocode/json?'

response = requests.get(base_url, params=params).json()
response.keys()

if response['status'] == 'OK':
   geometry= response['results'][0]['geometry']
   lat = geometry['location']['lat']
   lon = geometry['location']['lng']


print(lat, lon)


#commitsssss