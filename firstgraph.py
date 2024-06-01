import numpy as np
import matplotlib .pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#Define the function
def f(x,y) :
  return  ( x**2 + y**2 )

# Create a Meshgrid for x and y values

x = np.linspace (-5 , 5 , 100)
y = np.linspace (-5 , 5 , 100)

x_grid , y_grid =  np.meshgrid(x,y)

# Calculate z values using function z = x^2 + y^2
z = np.sqrt (x_grid **2  + y_grid **2 )

#Create a 3D plot using matplotlib
fig  = plt.figure()
ax = fig.add_subplot(111,projection='3d')

#Plot the surface
ax.plot_surface (x_grid , y_grid , z , cmap ='viridis')

#Set labels for the axes
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

#Display the plot
plt.show()
