import os
from . import db
from . import plots

__version__ = "0.0.1"

db.load(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data/cams.csv'))
