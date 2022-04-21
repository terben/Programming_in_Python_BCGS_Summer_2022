# very short script to demonstarte matplotlib usage

# In constrast to notebooks, DO NOT put the line
# '%matplotlib inline' within a script!
import matplotlib.pyplot as plt
import numpy as np

# matplotlib plots two arrays against each other:
x = np.array([ 0.0, 1.0, 2.0, 3.0, 4.0, 5.0 ])
y = np.array([ 0, 0.5, 1.0, 1.5, 2.0, 2.5 ])

# a simple x-y plot
#plt.plot(x, y)
plt.plot(x, y, 'o')
plt.xlabel('x')
plt.ylabel('y')

# In contrast to Jupyter notebooks, it is explicitely necessary within
# a script to 'show' the plot (a separate window opens and the program
# is stopped until you close it)
plt.show()

# Instead of showing a plot, you can also save it to disk:
# For PS/PDF-plots you should choose bbox='tight'
# to not have borders around the figure (inclusion
# into LaTeX). For pixel formats such as jpg,
# you can give the image resolution with the dpi
# option.
#plt.savefig('test.png', bbox='tight', dpi=200)
