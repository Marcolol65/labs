import matplotlib.pyplot as plt
import numpy as np


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
