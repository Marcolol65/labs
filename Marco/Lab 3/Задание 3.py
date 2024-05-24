import matplotlib.pyplot as plt
import numpy as np

# graph 1
x = np.linspace(-10, 10, 100)


y_neg_x = -x
y_3 = np.ones_like(x) * 3


plt.plot(x, y_neg_x, color='blue', label='y = -x')
plt.plot(x, y_3, color='green', label='y = 3', linestyle='--')

# Plot the line x = 4
plt.axvline(x=4, color='red', linestyle='--', label='x = 4')

#plot axis
plt.axvline(x=0, color='black')
plt.axhline(0, color = 'black')

# Shade the areas where y < -x, x < 4, and y < 3
plt.fill_between(x, y_neg_x, y_3, where=(y_neg_x < y_3) & (x < 4), facecolor='yellow', label = 'y<-x', alpha=0.5)
# I'am having issues shading the right area of the graph here!

# Shade the areas where y > 3 and x > 4
plt.fill_between(x, y_3, 10, where=(x > 4), facecolor='orange', label = 'y > 3 & x > 4', alpha=0.5)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph 1')
plt.legend()

plt.grid(True)

plt.show()


# Graph 2

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

# Graph 3

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