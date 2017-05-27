import geoplotlib
from geoplotlib.colors import colorbrewer
from geoplotlib.utils import epoch_to_str, BoundingBox, read_csv


data = read_csv('agentTest.csv')
plot points
geoplotlib.dot(data, 'b')
# plot the heatmap
#geoplotlib.hist(data, colorscale='sqrt', binsize=4)
# geoplotlib.show()
