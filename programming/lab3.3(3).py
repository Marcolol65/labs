import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 2*np.pi, 100)
circle_x = 5 + 5 * np.cos(theta)
circle_y = 5 + 5 * np.sin(theta)


# Create the plot
plt.figure(figsize=(8, 8))

# Plot the circle
plt.plot(circle_x, circle_y, label='Circle')

# Set axis limits and labels
plt.xlim(0, 10)
plt.ylim(0, 10)
plt.xlabel('x')
plt.ylabel('y')

# Add a title and legend
plt.title('Circle and Shaded Area')
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
