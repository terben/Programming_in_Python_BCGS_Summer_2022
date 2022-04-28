# estimate the square root of a positive float-number

import numpy # we need numpy for the fabs-function

x = 5.0  # the number from which to estimate the square root
eps = 1.0e-06 # The accuracy epsilon to which we want to estimate
              # the square root

# the first estimate for sqrt(x). We need to estimate
# it outside the loop to enter our while-construct at all
y_n = 1.0  # We always start with y_0 = 1.0
y_np1 = 0.5 * (y_n + x / y_n)

while numpy.fabs(y_np1 - y_n) > eps:
    y_n = y_np1
    y_np1 = 0.5 * (y_n + x / y_n)

print(f"An estimate for sqrt({x}) is {y_np1}.")
print(f"The square of the estimate is {y_np1 * y_np1}.")
