from folium.plugins import HeatMap
import numpy as np
import folium
import pandas as pd
path = "/Users/javierzarate/Desktop/andorra/projects/maps/2016-07-27/2016-07-27_0_hour.csv"
path_1 = "agentTest.csv"
path_2 = "prueba.csv"
agent = pd.read_csv(path_2)
data = []
for each in agent.iterrows():
    data.append([each[1]["lat"], each[1]["lon"]])
m = folium.Map([42.5, 1.5], tiles='stamentoner', zoom_start=12)
HeatMap(data).add_to(m)
m.save('heatmap.html')
