import climbing_cams as cams
import matplotlib.pyplot as plt

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
families = [cams.DB.select(**spec) for spec in family_specifications]
cams.Plots.plot_ranges(families)
cams.Plots.scatter_average(families, 'expansion_rate', 'specific_weight')
fig, ax = plt.subplots(2,1)
cams.Plots.scatter_individual(families, 'avg', 'weight', ax[0])
cams.Plots.scatter_individual(families, 'avg', 'specific_weight', ax[1])
ax[0].set_yscale('log')
ax[0].set_xscale('log')
ax[1].set_yscale('log')
ax[1].set_xscale('log')
ax[1].get_legend().remove()
plt.show()
