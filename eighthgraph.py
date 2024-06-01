from scipy.optimize import minimize_scalar
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#Define the Function
def parabola(x):
 return np.square(x)

#Define the distance function
def distance(x) :
  return np.sqrt(x**2 + (parabola(x)-3)**2)

#Define a function to find minimum distance
def min_distance() :
  result = minimize_scalar(distance)
  return result.fun

#Calculate the minimum distance
min_dist = min_distance()


#Plot a Parabola for values of x
x = np.linspace(-5,5,100)
y = np.linspace(-5,5,100)
X,Y = np.meshgrid(x,y)




#Create a 3D plot using matplotlib
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

#Plot the 3D function surface
surf = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)

# Plot the point (0,3)
ax.scatter(0, 3, parabola(0), color='red', label='Point (0,3)')



#Set the Z-axis limits
ax.set_zlim(0,100)

# Add colourbar
cbar = fig.colorbar(surf , ax=ax , pad = 0.3 , shrink = 0.5 , aspect = 10)

#Add labels
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('Parabola and Point(0,3)')

#Show the Plot
plt.legend()
plt.show()

print("Minimum distance:", min_dist)
