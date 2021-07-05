# # App with WebMap of Volcanos and Population
import folium
from folium.features import GeoJson
import pandas

# # Creating map object
map = folium.Map(location = [-32.14231151903316, 115.98735476985958], zoom_start = 3, tile="Stamen Terrian")

# ====================================================
# Creating volcanoes Map layer
fgv = folium.FeatureGroup(name='Volcanoes')

#Opening 'Volcanos.txt' file by pandas and assigning lat and lon values
data = pandas.read_csv("Volcanoes.txt")
# print(data.columns)

lat = list(data["LAT"])
lon = list(data["LON"])
elevation = list(data["ELEV"])

def foo(el):
  if el > 3000:
    return 'red'
  elif el > 2000:
    return 'orange'
  elif el > 1000:
    return 'green'
  else:
    return 'blue'
#Creating for Loop to loop over coordinates  
for x, y, z in zip(lat, lon, elevation):
  fgv.add_child(folium.Marker(location = [x, y], popup = ('elevation: {} m'.format(z)), icon = folium.Icon(foo(z))))
# ===================================================================

# Adding population layer map
fgp = folium.FeatureGroup(name="population")
fgp.add_child(folium.GeoJson(data = open('world.json', 'r', encoding='utf-8-sig').read(), 
style_function = lambda x:{'fillColor': 'green' if x ['properties']['POP2005'] <1000000 else 'orange' if 1000000 <= x ['properties']
['POP2005'] < 2000000 else 'red'}))
# =========================================================================================

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map1.html")
