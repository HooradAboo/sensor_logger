import pandas as pd
import folium


def plot_coordinates(data_frame, zoom_start=10):
    # Create a map centered on the first coordinate
    map = folium.Map(location=[data_frame['latitude'][0],
                    data_frame['longitude'][0]], zoom_start=zoom_start)

    # Add markers to the map for each coordinate
    for index, row in data_frame.iterrows():
        folium.Marker([row['latitude'], row['longitude']]).add_to(map)

    # Display and save the map
    map
    map.save('map.html')


dir = './2023-03-25_20-14-03/Location.csv'

# Read CSV file with latitudes and longitudes
df = pd.read_csv(dir)

plot_coordinates(df)
