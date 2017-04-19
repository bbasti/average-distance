import random
import math

#Number of unique distances between random points to compute
dist_amount = 1000000
#Initialize the sum of all computed distances with 0
dist_sum = 0

#This loop computes the sum of multiple distances between random points in the unit square
for x in range(1, dist_amount):
    print "Distance", x, "/", dist_amount, "\r",
    #Add the distance between two random points in the unit square to the sum of all distances
    dist_sum += math.sqrt(((random.random()-random.random()) ** 2) + ((random.random()-random.random()) ** 2))

#Print out the average distance by dividing the sum of all distances by the number of computed distances
print "Average Distance: ", (dist_sum/dist_amount)
