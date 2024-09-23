import os
from climbing_cams import db
from climbing_cams import plots

__version__ = "0.0.1"

db.load(os.path.join(os.path.dirname(os.path.realpath(__file__)),'data/cams.csv'))
