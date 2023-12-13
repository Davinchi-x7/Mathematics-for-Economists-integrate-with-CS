import numpy as np 
import matplotlib.pyplot as plt

#define tax function i.e T = t0 +t1Y
def Tax_Function(Y):
    return 70 + 0.2 * Y

#independent variable
x_values = np.linspace(0, 10, 100)
#dependent variable
y_values = Tax_Function(x_values)

plt.plot(x_values,y_values, label='Tax function: 70 + 0.2Y')

plt.xlabel('Y')
plt.ylabel('T')
plt.title('Consumption function')
plt.legend()

plt.show()
