from InquirerPy import inquirer
from pathlib import Path
from exiftool import ExifToolHelper
from geopy.geocoders import Nominatim
from tabulate import tabulate
import os
import ast

os.system("clear")

# Images directory path
ImagesDIR = Path("./images")

# Initiate empty list to store files names 
file_names_in_dir = []


def Make_Table(address: str, image_name: str) -> None:
    headers = ["Image Name", "Address"]
    add_table = [[image_name, address]]
    print(tabulate(add_table, headers, tablefmt="rounded_grid"))



def Fill_List() -> None:
    for file in ImagesDIR.iterdir():
        if file.is_file():
            file_names_in_dir.append(file.name)



def PhotoSelection() -> str:
    image_file = inquirer.select(
            message="Select Photo File:",
            choices = file_names_in_dir,
            ).execute()
    return image_file



def GetExact(coordinates, image_name) -> None:
    geolocator = Nominatim(user_agent="my_unique_python_app_123")
    location = geolocator.reverse(coordinates)
    address = location.address
    print(f"\nAddress > {address}")
    
    Make_Table(address, image_name)


def GetMetadata(image, image_name) -> None:
    with ExifToolHelper() as et:
        GpsTag = et.get_tags([image], tags=["GPSPosition"])

    GpsTagStr = str(GpsTag)
    GpsTagFixed = ast.literal_eval(GpsTagStr)

    Coords = GpsTagFixed[0]['Composite:GPSPosition']

    GetExact(Coords, image_name)



if __name__ == "__main__":

    Fill_List()
    image = PhotoSelection()
    #print(f"\nThe Photo Selected > {image}")
    GetMetadata(Path(f"./images/{image}"), image)


