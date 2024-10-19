import matplotlib.pyplot as plt
import matplotlib.lines as mlines

x_red = [0.009, 0.12, 0.18, 0.35, 0.47, 0.55, 0.61, 0.8, 0.93]
y_red = [0.77, 0.83, 0.32, 0.69, 0.36, 0.63, 0.47, 0.49, 0.63]
x_green = [0.13, 0.27, 0.36, 0.43, 0.56, 0.78, 0.86, 0.99,0.96, 0.98]
y_green = [0.11, 0.6, 0.25, 0.66, 0.97, 0.52, 0.6, 0.06, 0, 0.39]
x_blue = [0.05, 0.24, 0.352, 0.39, 0.62, 0.69, 0.57, 0.77, 0.875]
y_blue = [0.99, 0.18, 0.31, 0.7, 0.47, 0.11, 0.26, 0.09, 0.78]

plt.scatter(x_red, y_red, color='red', s=10, edgecolors='black', label='_nolegend_')
plt.scatter(x_green, y_green, color='green', s=10, edgecolors='black', label='_nolegend_')
plt.scatter(x_blue, y_blue, color='blue', s=10, edgecolors='black', label='_nolegend_')

red_dot = mlines.Line2D([], [], color='red', marker='o', linestyle='None', markersize=5, markeredgecolor='black', label='red')
green_dot = mlines.Line2D([], [], color='green', marker='o', linestyle='None', markersize=5, markeredgecolor='black', label='green')
blue_dot = mlines.Line2D([], [], color='blue', marker='o', linestyle='None', markersize=5, markeredgecolor='black', label='blue')

legend = plt.legend(handles=[red_dot, green_dot, blue_dot], loc='upper right', numpoints=3)

for text, color in zip(legend.get_texts(), ['red', 'green', 'blue']):
    text.set_color(color)

plt.xlim(-0.2, 1.2)
plt.ylim(-0.2, 1.2)

plt.show()

print('1')