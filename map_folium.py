import folium 
import webview

# multiple markers using dictionary

#markers_dict = {'Los Angeles': [34.041008, -118.246653], 
                #'Las Vegas': [36.169726, -115.143996], 
                #'Denver': [39.739448, -104.992450], 
               # 'Chicago': [41.878765, -87.643267], 
               # 'Manhattan': [40.782949, -73.969559]}

#print(markers_dict)

# create map
#map_cities = folium.Map(location=[41, -99], zoom_start=4)

# plot locations
#for i in markers_dict.items():
    #folium.Marker(location=i[1], popup=i[0]).add_to(map_cities)
   # print(i)

# display map    


# route

# map
map_plot_route = folium.Map(location=[38, -98], zoom_start=4)

# route_locs = ['Los Angeles', 'Las Vegas', 'Denver', 'Chicago', 'Manhattan']
# can use list of lists or list of tuples
route_lats_longs = [[34.041008,-118.246653],
                    [36.169726,-115.143996], 
                    [39.739448,-104.992450], 
                    [41.878765,-87.643267], 
                    [40.782949,-73.969559]]

# add route to map
folium.PolyLine(route_lats_longs).add_to(map_plot_route)

# display map
map_plot_route
map_plot_route.save('x.html')
file = open("x.html", "r")
code = file.read()

webview.create_window('Hello world', html=code)
webview.start()