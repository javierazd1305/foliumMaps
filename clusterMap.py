import folium
import pandas as pd
andorra = pd.read_csv("andorraCities.csv")
path = "/Users/javierzarate/Desktop/andorra/projects/maps/2016-07-27/2016-07-27_0_hour.csv"
path_1 = "prueba.csv"
agent = pd.read_csv(path_1)
map_1 = folium.Map(location=[42.5, 1.5], zoom_start=12,
                   tiles='Stamen Terrain')
andorraCitiesCluster = []
andorraCities = []
for each in andorra.iterrows():
    andorraCitiesCluster.append(
        folium.MarkerCluster(each[1]["name"]).add_to(map_1))
    andorraCities.append([each[1]["name"], each[1]["lat"], each[1]["lon"]])
# print andorraCitiesCluster[0], andorraCities[0]

for each in agent.iterrows():
    folium.Marker([each[1]["lat"], each[1]["lon"]],
                  popup=each[1]["name"]).add_to(andorraCitiesCluster[1])
map_1.save('cluterMap.html')
