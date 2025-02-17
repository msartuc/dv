import json, requests
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline
import plotly.graph_objects as go

# Explore the structure of the data.
# filename = 'Datasets/eq_data_30_day_m1.json'
# with open(filename) as f:
#     all_eq_data = json.load(f)
all_eq_data = requests.get(
    "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_month.geojson"
).json()

# Extracting all the important key features.
all_eq_dicts = all_eq_data["features"]

# Extracting the magnitude and the locations.
mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict["properties"]["mag"]
    lon = eq_dict["geometry"]["coordinates"][0]
    lat = eq_dict["geometry"]["coordinates"][1]
    title = eq_dict["properties"]["title"]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(title)

# Map the earthquakes.
data = [
    {
        "type": "scattergeo",
        "lon": lons,
        "lat": lats,
        "text": hover_texts,
        "marker": {
            "size": mags,
            "sizeref": 0.02025,
            "symbol": "circle",
            "sizemode": "area",
            "color": mags,
            "colorscale": "Viridis",
            "reversescale": True,
            "colorbar": {"title": "Magnitude"},
        },
    }
]

my_layout = Layout(title="Global Earthquakes",margin={"l":0,"r":0,"t":0,"b":0})

fig = {"data": data, "layout": my_layout}

offline.plot(fig, filename='global_earthquakes.html')