import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import climbing_cams as cams
import matplotlib.pyplot as plt

data = cams.load_data()
family_specifications = [
    {'brand':'Metolius',     'name':'UL'},
    {'brand':'Metolius',     'name':'SuperCam'},
    {'brand':'Totem',        'name':'TotemCam'},
    {'brand':'Alien',        'name':'X'},
    {'brand':'BD',           'name':'Z4'},
    {'brand':'BD',           'name':'C4'},
    {'brand':'DMM',          'name':'Dragon'},
    {'brand':'Wild Country', 'name':'Friend'}
]
families = [cams.select_cams(data, **spec) for spec in family_specifications]
cams.Plot.plot_ranges(families, smart_ylabels=True, numbers_inside=True)
cams.Plot.scatter_average(families, 'expansion_rate', 'specific_weight')
fig, ax = plt.subplots(2,1)
cams.Plot.scatter_individual(families, 'avg', 'weight', ax[0])
cams.Plot.scatter_individual(families, 'avg', 'specific_weight', ax[1])
ax[0].set_yscale('log')
ax[0].set_xscale('log')
ax[1].set_yscale('log')
ax[1].set_xscale('log')
ax[1].get_legend().remove()
plt.show()
