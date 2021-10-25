# from matplotlib import pyplot as plt
import math
import re
import heapq
# from scipy.spatial.distance import hamming
import statistics

f = open("/Users/rafiqkamal/Desktop/Data_Science/RNAProject210110/RNAL20StructuresGSSizes.txt")
contents = f.readlines()

# The original code worked for what is it was made for, but after talking with the lead researcher, I see that the code needs to be a lot more robust in order to print out various graphs of various parts of the RNA structures in order to try and find patterns. To accomplish this, I will not hard code everything, but rather use some more flexible functions, data structures, and algorithms that would, for example, be able to quickly and easily input a few numbers and look at the top twenty frequencies and their corresponding hamming distances graphs, the lowest twenty frequencies and their hamming distances, or a random set of frequencies and look at their hamming distances. In addition, this code needs to be able to quickly plot scatterplots using any of the above examples.
log10_frequency_array = []
frequency_structure_array = []# create a main structure a list to hold the original clean data that will be sorted in ascending order by the frequency
count = 0 # create a count variable (primary key) that will keep track of where the particular frequency is from the original data which has a total around 11K strings

for line in contents:
    x = re.findall("\d+",line)
    y = re.findall("[()\.]+",line)
    frequency_structure_array.append([int(x[0]),y[0]])

frequency_structure_array.sort(key=lambda x:x[1])
for line in frequency_structure_array:
    count = count + 1
    line.insert(0,count)
##########################      count,  frequency,      structure
#frequencyArray now looks like [11219, 364197924001, '....................']

# create a function named the hamming_maker function which will return a hash/object which keys will be the count and the values will be an array of the hamming distance(NOTE: hamming distance is just an integer, then I may make this an integer as well and not an array/list)

def hamming_maker(start,end,array):
    hash = {}
    for frequencies in range(start,end):
        print(array[frequencies])

hamming_maker(11200,11219,frequency_structure_array)
# create a function named hammingFiguresMaker which will create figures from the hamming functions object/hash and will label and title the figures based on the count

# create a helper function named meanMaker which will be called in the hamming_maker function to print the means of the results of the hamming_maker fucntion

# create a scatter_plot_maker function which will take in any two arrays/list and make a scatter plot of them. Again using the count variable to set the title and labels.