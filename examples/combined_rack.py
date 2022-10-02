import sys, os
sys.path.append(os.path.join(sys.path[0], '..'))

import climbing_cams
import matplotlib.pyplot as plt

data = climbing_cams.load_data()
cams = climbing_cams.select_cams(data, name="Z4", expansion_range=[0,20])
cams += climbing_cams.select_cams(data, name="TotemCam", expansion_range=[10,60])
climbing_cams.bar_chart(cams, ylabel='{name} [{number}]')
plt.text(.9, .1, f'Total weight: {cams.weight} {climbing_cams.Units.weight}', horizontalalignment='right', transform = plt.gca().transAxes, backgroundcolor='0.9')
plt.tight_layout()
plt.show()

