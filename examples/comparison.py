import sys, os
sys.path.append(os.path.join(sys.path[0], '..'))

import climbing_cams as cams
import matplotlib.pyplot as plt

data = cams.load_data()
families_specifications = [
    {'brand':'Alien',        'name':'X'},
    {'brand':'Metolius',     'name':'UL'},
    {'brand':'BD',           'name':'UL'},
    {'brand':'BD',           'name':'C4'},
    {'brand':'Totem',        'name':'TotemCam'},
    {'brand':'DMM',          'name':'Dragon'},
    {'brand':'Wild Country', 'name':'Friend'},
    {'brand':'Rock Empire',  'name':'Axel'}
]
families = [cams.select_cams(data, **spec) for spec in families_specifications]
cams.plot_ranges(families, smart_ylabels=True)
cams.scatter_average(families, 'expansion_rate', 'specific_weight')
cams.scatter_individual(families, 'expansion_rate', 'weight')
plt.show()

