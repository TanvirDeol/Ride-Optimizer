import folium 
import webview

# multiple markers using dictionary

markers_dict = {'Los Angeles': [34.041008, -118.246653], 
                'Las Vegas': [36.169726, -115.143996], 
                'Denver': [39.739448, -104.992450], 
                'Chicago': [41.878765, -87.643267], 
                'Manhattan': [40.782949, -73.969559]}

# create map
map_cities = folium.Map(location=[41, -99], zoom_start=4)

# plot locations

for i in markers_dict.items():
    print(i[0])
    folium.Marker(location=i[1], popup=i[0]).add_to(map_cities)
    print(i)

# display map    
map_cities.save('x.html')
file = open("x.html", "r")
code = file.read()

webview.create_window('Hello world', html=code)
webview.start()