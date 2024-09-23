import os
import csv
from .cam import Cam
from .rack import Rack

_data = []

def _load():
    global _data
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),'cams.csv')) as file:
        reader = csv.reader(file)
        next(reader)
        data = [Cam(*row) for row in reader]
    _data += data

def select(brand="", name="", number="", color="", expansion_range=[]):
    rack = Rack()
    for cam in _data:
        if ((cam.brand == brand if brand else True) and
            (cam.name == name if name else True) and
            (cam.number == number if number else True) and
            (cam.color == color if color else True) and
            (expansion_range[0] < cam.min < cam.max < expansion_range[1] if len(expansion_range)==2 else True)):
            rack.append(cam)
    return rack
