import os
from . import db
from . import plots
from . import cam
from . import rack

__version__ = "0.0.2"

db.load(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data/cams.csv'))
