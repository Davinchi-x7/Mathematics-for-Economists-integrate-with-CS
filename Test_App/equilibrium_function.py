import numpy as np
import matplotlib.pyplot as plt 

# define linear function
def linear_demand_function(p):
    return 3 - 0.5 * p
def linear_supply_function(p):
    return -1 + 1/6 * p

# to generate x values
x_values = np.linspace(0, 10, 100)

# calculate corresponding y values
y1_values = linear_demand_function(x_values)
y2_values = linear_supply_function(x_values)



#plotting the linear function
plt.plot(x_values, y1_values, label='Linear Demand Function: 3 - 0.5 * p')
plt.plot(x_values, y2_values, label='Linear Supply Function: -1 + 1/6 * p')

# Add labels and tittle
plt.xlabel('Q')
plt.ylabel('P')
plt.title('Linear function plot')
plt.legend()

# Show the plot
plt.show()