from InquirerPy import inquirer
from pathlib import Path
from exiftool import ExifToolHelper
import pandas as pd
from geopy.geocoders import Nominatim
import time
import os
import ast

os.system("clear")

# Images directory path
ImagesDIR = Path("./images")

# Initiate empty list to store files names 
file_names_in_dir = []


def Fill_List() -> None:

    for file in ImagesDIR.iterdir():
        if file.is_file():
            file_names_in_dir.append(file.name)


def PhotoSelection() -> str:
    photo_file = inquirer.select(
            message="Select Photo File:",
            choices = file_names_in_dir,
            ).execute()
    return photo_file

def GetExact(coordinates) -> None:
    geolocator = Nominatim(user_agent="my_unique_python_app_123")
    location = geolocator.reverse(coordinates)
    print(f"\nAddress > {location.address}")


def GetMetadata(photo) -> None:
    with ExifToolHelper() as et:
        metadata = et.get_metadata(photo)
        GpsTag = et.get_tags([photo], tags=["GPSPosition"])
    for x in metadata:
        for y, z in x.items():
            # Print all the metadata in a organized list of all the keys and values
            print(f"\n{y}: {z}")

    GpsTagStr = str(GpsTag)
    GpsTagFixed = ast.literal_eval(GpsTagStr)

    Coords = GpsTagFixed[0]['Composite:GPSPosition']

    GetExact(Coords)



if __name__ == "__main__":
    Fill_List()
    Photo = PhotoSelection()
    print(f"\nThe Photo Selected > {Photo}")
    GetMetadata(Path(f"./images/{Photo}"))
