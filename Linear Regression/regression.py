import numpy 
import pandas as pd 



'''
A manufacturer has recorded the sizes and corresponding prices of a specific product. The data is as follows:

A product with a size of 6 inches is priced at $600.
A product with a size of 8 inches is priced at $800.
A product with a size of 12 inches is priced at $1200.
A product with a size of 14 inches is priced at $1400.
A product with a size of 18 inches is priced at $1800.
Using linear regression, estimate the price of a product that is 15 inches in size.
'''

x = numpy.array([6,8,12,14,18])
y = numpy.array([600,800,1200,1400,1800])
x_and_y = numpy.array([])

data = pd.DataFrame({'x': x, 'y': y})
data['xy'] = data['x'] * data['y'] 

data['x^2'] = data['x'] ** 2

print(data)

# let's find mean of x and y and xy and x^2

x_mean = numpy.mean(data['x'])
y_mean = numpy.mean(data['y'])
xy = numpy.mean(data['xy'])
x_sqaured_mean = numpy.mean(data['x^2'])




# calculate m and c
m = (x_mean * y_mean - xy) / (x_mean**2 - x_sqaured_mean)
c = y_mean - m * x_mean

# calculate y value for the 15 inch product
y_predicted = m * 15 + c

print("The estimated price of a product with a size of 15 inches is: ${}".format(y_predicted))
