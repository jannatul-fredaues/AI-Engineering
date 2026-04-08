import numpy as np
x = np.linspace(0, 10, 100)
y = x**2
dydx = np.gradient(y, x) # Estimates slope at each point
