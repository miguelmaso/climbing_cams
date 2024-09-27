import csv
from .cam import Cam
from .rack import Rack

cams = []


def load(path: str):
    global cams
    with open(path) as file:
        reader = csv.reader(file)
        next(reader)
        data = [Cam(*row) for row in reader]
    new_data = [cam for cam in data if cam not in cams]
    cams += new_data


def select(brand="", name="", number="", color="", expansion_range=[]):
    rack = Rack()
    for cam in cams:
        if ( (cam.brand == brand if brand else True) and
             (cam.name == name if name else True) and
             (cam.number == number if number else True) and
             (cam.color == color if color else True) and
             (expansion_range[0] < cam.min < cam.max < expansion_range[1] if len(expansion_range) == 2 else True)):
            rack.append(cam)
    return rack
