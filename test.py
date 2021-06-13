import folium
from numpy import datetime64
from pyasn1_modules.rfc2459 import PrivateDomainName
import webview
import folium.plugins as plugins
import datetime
import pprint

def drawRoute(travelRoute,lat,long):
    x = datetime.datetime.now()
    lines = []
    for i in range(1,len(travelRoute)):
        a = x.strftime("%Y-%m-%d %H:%M:%S")
        x+=datetime.timedelta(minutes=1)
        b = x.strftime("%Y-%m-%d %H:%M:%S")
        lines.append({
            "coordinates":[
                [float(long[travelRoute[i-1]]),float(lat[travelRoute[i-1]])],
                [float(long[travelRoute[i]]),float(lat[travelRoute[i]])],
            ],
            "dates": [a,b],
            "color":"red",
        })

    #pprint(lines)
    m = folium.Map(location=[43,-80], zoom_start=16)
    # Lon, Lat order.
    '''lines = [
        {
            "coordinates": [
                [139.76451516151428, 35.68159659061569],
                [139.75964426994324, 35.682590062684206],
            ],
            "dates": [times[0], times[1]],
            "color": "red",
        },
        {
            "coordinates": [
                [139.75964426994324, 35.682590062684206],
                [139.7575843334198, 35.679505030038506],
            ],
            "dates": [times[1], times[2]],
            "color": "blue",
        },
        {
            "coordinates": [
                [139.75964426994324, 35.682590062684206],
                [139.7575843334198, 35.679505030038506],
            ],
            "dates": [times[2], times[3]],
            "color": "blue",
        }
    ]'''

    features = [
        {
            "type": "Feature",
            "geometry": {
                "type": "LineString",
                "coordinates": line["coordinates"],
            },
            "properties": {
                "times": line["dates"],
                "style": {
                    "color": line["color"],
                    "weight": line["weight"] if "weight" in line else 5,
                },
            },
        }
        for line in lines
    ]
    print()
    #lines[i]['coordinates'][0] = [lat,long]
    #lines[i]['color']= 'red'
    #lines[i]['dates'][0/1] = '2017-06-02T00:00:00'
    plugins.TimestampedGeoJson(
        {
            "type": "FeatureCollection",
            "features": features,
        },
        period="PT1M",
        add_last_point=True,
    ).add_to(m)

    m.save('x.html')
    file = open("x.html", "r")
    code = file.read()

    webview.create_window('Hello world', html=code)
    webview.start()
