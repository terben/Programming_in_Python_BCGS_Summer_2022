import lpf

# Demonstration for numeric problems in computing with 'low-precision-floats
# (lpf)'
# The file 'lpf.py' must be in teh same folder as this script.

# Note that all problems demonstrated in this script also occur with the
# Python-float types. They only difference is that lpf does all
# float-calculations with four significant digits, while the Python-float type
# uses 15.

# show failure of associative and commutative laws:
u, v, w = lpf.LPF(1113), lpf.LPF(-1111), lpf.LPF(7.511)

print((u + v) + w, u + (v + w))
print(u + v + w, v + w + u)

# Show failure of the distributive law
u, v, w = lpf.LPF(2000), lpf.LPF(-6), lpf.LPF(6.003)

print(u * v, u * w, v + w)
print(u * v + u * w, u * (v + w))

# show that the relation 'eps > 0' is not equaivalent to 'a + eps > a':
a = lpf.LPF(1.0)

eps = 0.0001

print(eps > 0, a + eps > a)
