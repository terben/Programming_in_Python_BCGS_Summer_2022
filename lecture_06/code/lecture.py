import numpy as np
import matplotlib.pyplot as plt

print("Hello to all my students!")

a = 1
print(a)

x = np.linspace(0.0, 2.0 * np.pi, 100)
y = np.sin(x)

plt.plot(x, y)
plt.show()
