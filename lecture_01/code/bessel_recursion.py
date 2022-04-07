# Verification of scipys Bessel function implementation
# - recursion relation

import scipy.special as ss
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# for nicer plots, make fonts larger and lines thicker
matplotlib.rcParams['font.size'] = 12
matplotlib.rcParams['axes.linewidth'] = 2.0


# Now, let's verify numerically the recursion relation
# J(n+1,x) = (2n/x)J(n,x)-J(n-1,x), n = 5

# We choose here to consider x-values  between 0.1 and 50.
# We exclude 0 because the recursion relation contains a
# formal division by it.
x = np.linspace(0.1, 50, 500)

# construct both sides of the recursion relation, these should be equal
n = 5

# the scipy implementation of jn(5);
j_n = ss.jn(5, x)

# The recursion relation:
j_n_rec = (2.0 * (n - 1) / x) * ss.jn(n - 1, x) - ss.jn(n - 2, x)

# We now plot the difference between the two formulas
# (j_n and j_n_rec above).  Note that to
# properly display the errors, we want to use a logarithmic y scale.
plt.semilogy(x, abs(j_n - j_n_rec), 'r+-', linewidth=2.0)

plt.title('Error in recursion for $J_%s$' % n)
plt.xlabel('x')
plt.ylabel('$|J_n(5) - J_{n,rec}(5)|$')
plt.grid()

# Don't forget a show() call at the end of the script
# Not necessary for an interactive Jupyter notebook session.
plt.show()
