import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 1000)

theta = np.linspace(0, 2*np.pi, 100)
circle_x = 3 * np.cos(theta)
circle_y = 3 * np.sin(theta)


square_x = [-3, 3, 3, -3, -3]
square_y = [-3, -3, 3, 3, -3]

# Create the plot
plt.figure(figsize=(6, 6))

# Plot the circle
plt.plot(circle_x, circle_y, label='Circle')

# Plot the square
plt.plot(square_x, square_y, label='Square')

# Having problems jus changing the required shaded part
plt.fill_between(circle_x, circle_y, where=(circle_x ), facecolor='orange', label = 'y > 3 & x > 4', alpha=0.5)

plt.xlabel('x')
plt.ylabel('y')

plt.grid(True)

plt.legend()

plt.show()