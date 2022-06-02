#!/usr/bin/env python3

# Just call the script to obtain a help and usage message

import sys
import argparse

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import scipy.odr as sodr

# Function definitions:

# The function lin_finc is internally used by the ODR fitting procedure.
# It is probably not useful to call it in other curcumstances.
def lin_func(p, x):
     """
     The function is internally used by the ODR-fit procedure

     function arguments:
     p: a numpy-array of two elements (slope and y-intersection of a line)
     x: value for which you want to evaluate the function

     The function calculates p[0] * x + p[1] and returns that value.
     """

     m, c = p
     return m * x + c

# main script tasks start here:

# read command line arguments:
parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
    epilog="""
DESCRIPTION:
  The script performs a line-fit for data that contain errors in
  the x- and y-coordinates!

  Input is a file (command line option -i) with four columns:
  x, error_x, y, error_y.

  The input file may contaion comment lines starting with a hash (#).

  The program fits a two-parameter line (y = a * x + b) to approximate
  the data. The used algorithm, the orthogonal-distance regression
  is thoroughly documented at
  http://docs.scipy.org/doc/scipy/reference/odr.html.

  Program output are the ebst fit line-parameters a und b together with
  their estimated errors. In addition, the uise can ask for a plot
  of the data points together with the best fit-line (command line option
  '-h').

EXAMPLES:

  - ./chi2FitXYErr.py -i dataxy.txt
    Fits a line to the data in 'dataxy.txt' and print the fit results to
    screen

  - ./chi2FitXYErr.py -i dataxy.txt -o ergebnis.png
    The same as above. In addition, data points and best-fit line
    are shown in the plot 'result.png'.

AUTHOR:
  Thomas Erben (terben@astro.uni-bonn.de)
"""
)
parser.add_argument('-i', '--input_file', nargs=1,
                    required=True, help='Name der Datendatei')
parser.add_argument('-o', '--output_file', nargs=1,
                    help='Name des Ausgabeplots (OPTIONAL)')

args = parser.parse_args()

input_file = args.input_file[0]

# Read data:
data = np.loadtxt(input_file)

# Rough sanity check: Does the input file have 4 columns?
if data.shape[1] != 4:
     print("Datei %s hat keine 4 Spalten!" % (input_file), file=sys.stderr)
     sys.exit(1)

# Give meaningful variable names to input data columns:
x = data[:,0]
x_error = data[:,1]
y = data[:,2]
y_error = data[:,3]

# Perform the fitting procedure. For an explanation of the following
# four code lines consult the help of the scipy.odr module:
lin_model = sodr.Model(lin_func)
fit_data = sodr.RealData(x, y, sx=x_error, sy=y_error)
odr = sodr.ODR(fit_data, lin_model, beta0=[0., 1.])
out = odr.run()

# We give meaningful names to the best-fit parameters and errors
# returned by 'odr.run':
a = out.beta[0]
b = out.beta[1]
err_a = out.sd_beta[0] # error on a
err_b = out.sd_beta[1] # error ob b


print("result of fit:\n")
print("y = a * x + b with\n")
print("a = %f +/- %f" % (a, err_a))
print("b = %f +/- %f" % (b, err_b))

# create a plot with data points and fit-line if the user asked for it:
if args.output_file != None:
     # font size of labels etc,
     matplotlib.rcParams['font.size'] = 18
     # line width of coordinate axes
     matplotlib.rcParams['axes.linewidth'] = 2.0

     y_fit = a * x + b

     plt.figure()
     plt.errorbar(x, y, xerr=x_error, yerr=y_error,
                  lw=2, fmt='.', label="data points")
     plt.plot(x, y_fit, lw=2, label="y=%.2f * x + %.2f" % (a, b))
     plt.xlabel('x')
     plt.ylabel('y')
     plt.title("%d data points and line-fit" % (x.shape[0]))
     plt.legend()

     plt.savefig(args.output_file[0], bbox_inches='tight')
