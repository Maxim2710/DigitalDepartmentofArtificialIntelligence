import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import PchipInterpolator

angles = np.linspace(0, 360, 500)

points = np.array([[0, 0], [30, 2], [90, 5.1], [185, 0], [200, -1.1], [270, -2.4], [300, -2.2], [330, -1.3], [360, 0]])

coefficients = np.polyfit(points[:, 0], points[:, 1], 7)

position = np.polyval(coefficients, angles)

additional_points_x = [0, 25, 50, 90, 100, 155, 250, 300, 360]
additional_points_y = [155, 180, 155, 0, -48, -170, -20, 33, 160]

interp_func_velocity = PchipInterpolator(additional_points_x, additional_points_y)
velocity = interp_func_velocity(angles)

acceleration = 4000 * np.sin(np.radians(angles))

new_points = np.array([[0, 0], [0.0001, 4050], [10, 2500], [75, -8000], [90, -8450], [150, -1000], [190, 4600], [225,3000], [250, 2150], [270, 2050], [290, 2300], [325, 4000], [345, 4600], [360, 4050], [105, -8000]])
new_points = new_points[np.argsort(new_points[:, 0])]

interp_func_new = PchipInterpolator(new_points[:, 0], new_points[:, 1])
new_data = interp_func_new(angles)

fig, axs = plt.subplots(1, 3, figsize=(15, 7))

axs[0].plot(angles, position)
axs[0].set_title('Position vs Angle')
axs[0].set_xlabel('Angle (degrees)')
axs[0].set_ylabel('Position (in)')
axs[0].set_ylim(-3, 6)
axs[0].set_yticks(np.arange(-2, 6, 1))
axs[0].grid(True)

axs[1].plot(angles, velocity, label='True Speed')
axs[1].axhline(y=50, color='orange', label='Mean Piston Speed')
axs[1].scatter([90], [0], color='black', s=15, label='Top Dead Center', zorder=5)
axs[1].scatter([268], [0], color='black', marker='*', label='Bottom Dead Center', zorder=5)
axs[1].set_title('Piston Speed vs Angle')
axs[1].set_xlabel('Angle (degrees)')
axs[1].set_ylabel('Piston Velocity (mph)')
axs[1].set_ylim(-200, 200)
axs[1].grid(True)
axs[1].legend(loc='lower right', fontsize='small')

axs[2].plot(angles, new_data, label='New Data')
axs[2].set_title('Piston Net Force vs Angle')
axs[2].set_xlabel('Angle (degrees)')
axs[2].set_ylabel('Piston Acceleration (g)')
axs[2].grid(True)

plt.tight_layout()
plt.show()

print('1')