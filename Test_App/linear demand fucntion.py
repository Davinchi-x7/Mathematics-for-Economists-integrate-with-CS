import numpy as np
import matplotlib.pyplot as plt 

# define linear function
def linear_function(p):
    return 3 - 0.5 * p

# to generate x values
x_values = np.linspace(0, 10, 100)

# calculate corresponding y values
y_values = linear_function(x_values)

#plotting the linear function
plt.plot(x_values, y_values, label='Linear Function: 3 - 0.5 * p')

# Add labels and tittle
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear function plot')
plt.legend()

# Show the plot
plt.show()

