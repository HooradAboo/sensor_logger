import pandas as pd
import folium

import argparse
import os
import sys
from pathlib import Path

FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]  # YOLOv5 root directory
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))


def plot_coordinates(data, center, zoom, project, name):
    # Read the data from CSV file
    df = pd.read_csv(data)

    # Set the map center on the first coordinate
    if center == (None, None):
        center = (df['latitude'][0], df['longitude'][0])

    # Create a map 
    map = folium.Map(location=[center[0], center[1]], zoom_start=zoom)

    # Add markers to the map for each coordinate
    for index, row in df.iterrows():
        folium.Marker([row['latitude'], row['longitude']]).add_to(map)

    # # Display the map
    # map

    # Save the map
    map.save(f'{project}/{name}')


def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', type=str, default=ROOT / 'data/2023-03-25_14-20-07/Location.csv', help='location.csv path')
    parser.add_argument('--center', type=tuple, default=(None, None), help='a tuple of latitude and longitued to set map center')
    parser.add_argument('--zoom', type=int, default=10)
    # parser.add_argument('--save_dir', type=str, default=ROOT / 'data/hyps/hyp.scratch-low.yaml', help='hyperparameters path')
    parser.add_argument('--project', default=ROOT / 'runs', help='save to project/name')
    parser.add_argument('--name', default='map.html', help='save to project/name')

    opt = parser.parse_args()
    return opt


def main(opt):
    plot_coordinates(opt.data, opt.center, opt.zoom, opt.project, opt.name)


if __name__ == "__main__":
    opt = parse_opt()
    main(opt)
