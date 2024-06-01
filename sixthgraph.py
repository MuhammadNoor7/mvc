import numpy as np
import matplotlib.pyplot as plt

# Define the function
def f(x, y):
    return ((np.sin(x*y))/(x*2+y*2))

length = 4
amount = 1500
# Create a meshgrid for x and y
x = np.linspace(-length, length, amount)
y = np.linspace(-length, length, amount)
x, y = np.meshgrid(x, y)

# Calculate the function values
z = f(x, y)

# Create a mask to exclude points outside the specified Z-axis range
z_min, z_max = -3, 3
mask = (z >= z_min) & (z <= z_max)

# Apply the mask to the function values
z[~mask] = np.nan

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the function surface
ax.plot_surface(x, y, z, cmap='viridis', alpha=0.8)

# Set the Z-axis limits
ax.set_zlim(z_min, z_max)

# Add labels
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

# Show the plot
plt.show()
