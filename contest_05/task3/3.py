import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D

months = ['January', 'February', 'March', 'April', 'May', 'November', 'December']
hornberg = [320, 264, 192, 150, 147, 120, 275]
strick = [300, 257, 203, 200, 157, 279, 155]
huetten = [298.7, 240, 189, 178, 161, 231, 144]

x = np.arange(len(months))
width = 0.3

fig, ax = plt.subplots(figsize=(12, 6))
rects1 = ax.bar(x - width, hornberg, width, label='Hornberg', color='#F8756D')
rects2 = ax.bar(x, strick, width, label='Strick', color='#00BA39')
rects3 = ax.bar(x + width, huetten, width, label='Huetten', color='#609BFF')

ax.set_ylabel('Monthly Precipitation [mm]', fontsize=15)
ax.set_xticks(x)
ax.set_xticklabels(months)
ax.set_xlabel('Month')

ax.yaxis.set_major_locator(plt.MultipleLocator(100))
ax.xaxis.set_major_locator(plt.MultipleLocator(1))

ax.grid(which='major', linestyle='-', linewidth=0.7)
ax.grid(which='minor', linestyle=':', linewidth=0.5)

ax.yaxis.set_minor_locator(plt.MultipleLocator(50))

ax.set_ylim(bottom=-20)

legend_elements = [
    Line2D([0], [0], marker='s', color='w', label='Hornberg',
           markerfacecolor='#F8756D', markersize=30),
    Line2D([0], [0], marker='s', color='w', label='Strick',
           markerfacecolor='#00BA39', markersize=30),
    Line2D([0], [0], marker='s', color='w', label='Huetten',
           markerfacecolor='#609BFF', markersize=30)
]

legend = ax.legend(handles=legend_elements, title='Variable', loc='center left', bbox_to_anchor=(1, 0.5),
                   fontsize=14, title_fontsize=13, borderaxespad=1, shadow=True, frameon=True)

legend.get_title().set_fontweight('bold')

fig.tight_layout()
plt.show()

print('1')
