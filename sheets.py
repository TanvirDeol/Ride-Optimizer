import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
#change
client = ''
scope = ''
creds = ''

#initialize spreadsheet database
def initSheets():
    global client
    global creds
    global scope
    scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json",scope)
    client = gspread.authorize(creds)

#get information of clients that are matched with driver X
def getClients (driverName):
    long =[]
    lat =[]
    address =[]
    sheet = client.open("test").worksheet('Clients')
    data = sheet.get_all_records()
    drivers = sheet.col_values(9)[1:]
    for i in range (0,len(drivers)):
        cell = sheet.cell(i+2,9).value
        if cell == driverName:
            long.append(sheet.cell(i+2,6).value)
            lat.append(sheet.cell(i+2,7).value)
            address.append(sheet.cell(i+2,8).value)
    #print(drivers)
    #print(long)
    #print(lat)
    #print(address)
    return [long,lat,address]


