import pandas
import folium
import json

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elevetion):
    if elevetion < 1000:
        return  'green'
    elif 1000 <= elevetion < 3000:
        return 'orange'
    else:
        return 'red'	

#map = folium.Map(location=[lat, lon], zoom_start=6, tiles="Stamen Terrain")
#map = folium.Map(location=[lat[0], lon[0]], zoom_start=5, tiles="Stamen Terrain")

map = folium.Map(location=[38.58,-99.09], zoom_start=5, tiles="Mapbox Bright")

#map = folium.Map(location=[0, 0], zoom_start=6)

fg = folium.FeatureGroup(name="My Map")

#for lt,ln,el in zip(lat,lon,elev):
 #    fg.add_child(folium.Marker(location=[lt, ln],popup=str(el)+" m",icon=folium.Icon(color=color_producer(el)))
	 
for lt,ln,el in zip(lat,lon,elev):
     fg.add_child(folium.CircleMarker(location=[lt, ln],popup=str(el)+" m",
	 fill_color=color_producer(el),color = 'grey',fill_opacity=0.7))
	 #icon=folium.Icon(color=color_producer(el))))	 
     # 	 

with open('world.json','r',encoding='utf-8-sig') as json_file:
    worldJSON = json.load(json_file)


fg.add_child(folium.GeoJson(worldJSON,
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 
else 'orange' if 1000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))
	 
map.add_child(fg)
map.save("map092.html")	