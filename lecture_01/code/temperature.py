import numpy as np
import matplotlib.pyplot as plt

# read the data
data = np.loadtxt("../data/munich_temperatures.txt")

# get rid of bad data (temperatures over 50 or smaller than -50)
mask = (data[:,1] < 50) & (data[:,1] > -50)
data = data[mask]

# make two 1d-arrays for convenience:
day = data[:,0]
temperature = data[:,1]

# make the plot of the temperatures vs. the day:
plt.plot(day, temperature)
plt.savefig("temperature.png")

# mean temperature over overything
mean_all = temperature.mean()
print('mean temperature over all years/days: %f' % (mean_all))

# The first three months are a quarter of a year
# (fraction <= 0.25)
mask_jan_march = (day%1 <= 0.25)

mean_jan_mar = temperature[mask_jan_march].mean()
print('mean temperature from January to March: %f' % \
      (mean_jan_mar))

# get min, max and mean temperatures per year:
print('year   min_temp   max_temp   mean_temp')

for year in range(1995, 2013):
    # The np.floor function gets rid of the fractional part
    # from the years but it keeps them as float numbers.
    # We therefore use np.isclose to compare to the years:
    mask_year = (np.isclose(np.floor(day), year))
    temp_year = temperature[mask_year]
    print("%4d %10.4f %10.4f %10.4f" % \
          (year, temp_year.min(), temp_year.max(),
           temp_year.mean()))

# make the plot of the temperatures vs. the day
# (all years on top of each other):

# We need to start a new plot and hence the 'plt.clf()' command.
# If we do not do this the old plot from above is continued to
# be worked on
plt.clf()
plt.plot(day%1, temperature, '.')
plt.savefig("temperature_day.png")
