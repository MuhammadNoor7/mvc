import numpy as np
import matplotlib .pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


#Define the function
def f(x,y) :
  return (np.exp(x)  * np.cos(y))

# Create a meshgrid for x and y values
x = np.linspace(-5,5,100)
y = np.linspace(-5,5,100)

x , y = np.meshgrid(x,y)

#Calculate z values
z = np.exp(x) * np.cos(y)

#Calculate a 3d PLOT using matplotlib
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

#Plot the  3D surface
surf = ax.plot_surface (x , y,z , cmap = 'viridis' , alpha = 1)

#Add colourbar
fig.colorbar( surf ,  ax=ax , shrink = 0.5 , aspect = 10)


#Set labels for the axes
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title(r'$f(x,y)=e^x cosy$')


#Display the plot
plt.show()
