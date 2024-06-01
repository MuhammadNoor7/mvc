from scipy.optimize import minimize_scalar
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#Define the function
def f(x,y):

   return np.square(x) + 4 *np.square(y) - 2*x + 8*y

#Define the constraint function
def g(x,y) :
  return x + 2*y

#Define the constraint equation
def constraint_eq(x,y) :
  return g(x,y) - 7

#Define the Langrange function
def lagrange_func(x,y,l):
    return f(x,y) - l * constraint_eq(x,y)



#Create a meshgrid for x and y
x = np.linspace(-5,5,1200)
y = np.linspace(-5,5,1200)
x,y = np.meshgrid(x,y)
Z = lagrange_func(x,y,1)

#Calculate the function values
z = np.square(x) + 4 *np.square(y) - 2*x + 8*y



#Create a 3D plot using matplotlib
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

#Plot the 3D function surface
surf = ax.plot_surface(x,y,z , cmap = 'viridis' , alpha = 1)



#Set the Z-axis limits
ax.set_zlim(0,100)



#Add colourbar
cbar = fig.colorbar(surf,  ax= ax , pad=0.3, shrink=0.5, aspect = 10)
#Add labels

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
plt.title('Langrange Function' , loc='right')


#Show the Plot
plt.show()
