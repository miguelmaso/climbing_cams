import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import climbing_cams
import matplotlib.pyplot as plt

cams = climbing_cams.DB.select(name="Z4", expansion_range=[0,20])
cams += climbing_cams.DB.select(name="TotemCam", expansion_range=[10,60])
cams.plot_bar_chart(ylabel='{name} [{number}]')
plt.text(.9, .1, f'Total weight: {cams.weight} {climbing_cams.Units.weight}',
         transform = plt.gca().transAxes, horizontalalignment='right',
         bbox=dict(facecolor='none', edgecolor='black', boxstyle='round,pad=1'))
plt.tight_layout()
plt.show()
