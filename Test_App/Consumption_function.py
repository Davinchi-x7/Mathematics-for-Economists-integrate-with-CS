import numpy as np
import matplotlib.pyplot as plt

def Consumption_function(Yd):
    return 120 + 0.8 * Yd

x_values = np.linspace(0.0,5,100)

y_values = Consumption_function(x_values)

plt.plot(x_values, y_values, label='Consumption function: C = 120 + 0.8 * Yd' )

plt.xlabel('Yd')
plt.ylabel('C')
plt.title('Consumption Function')
plt.legend()

plt.show()