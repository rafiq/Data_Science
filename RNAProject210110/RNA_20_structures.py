#!/usr/bin/env python
# from matplotlib import pyplot as plt
# import numpy as np
# import re
# x = np.array(range(100))

# plt.hist(x,bins = np.logspace(start=np.log10(10), stop = np.log10(15), num = 10))
# plt.gca().set_xscale("log")
# plt.show()

# count = 0
# f = open("/Users/rafiqkamal/Desktop/Data_Science/RNAProject210110/RNAL20StructuresGSSizes.txt")
# contents = f.readlines()

# def count_elements(str) -> dict:
#     hist = {}
#     for line in str:
#         hist[line] = hist.get(line,0) + 1
#     return hist


# def ascii_histogram(seq):
#     counted = count_elements(seq)
#     for k in sorted(counted):
#         print('{0:5d} {1}'.format(k,'+' * counted[k]))

# ascii_histogram(contents)

# f.close()

# contents = f.readlines()

# count = 0
# a = []

# for line in contents:
#     count += 1
#     x = re.sub("\D","",line)
#     a.append(x)
#     # print(f'line {count}: {x}')

# print(a)

# print(count_elements(a))
# a = (0, 1, 1, 1, 2, 3, 7, 7, 23)

# def count_elements(seq) -> dict:
#     """Tally elements from `seq`."""
#     hist = {}
#     for i in seq:
#         hist[i] = hist.get(i, 0) + 1
#     return hist

# counted = count_elements(a)
# counted

# def hamming_distance(s1, s2):
#     if len(s1) != len(s2):
#         raise ValueError("Strand lengths are not equal!")
#     return sum(ch1 != ch2 for ch1,ch2 in zip(s1,s2))

from matplotlib import pyplot as plt
import math
import re
import heapq
from scipy.spatial.distance import hamming
import statistics

f = open("/Users/rafiqkamal/Desktop/Data_Science/RNAProject210110/RNAL20StructuresGSSizes.txt")#Read in the RNA Data which is a 20 Char abreviated RNA structure of parenthesis and the frequency an int that ranges from 1 to the millions
contents = f.readlines()

frequencyStructureArray = []#This is the main structure for this code that holds a 2D array(list) with the first element of each nested array being the structure string and the second element being the frequency number
histogramArray = []#this will hold the histogram data after they are calculated

for line in contents:
    x = re.findall("\d+",line)#parsing the original data to neatly put it into the main structure
    y = re.findall("[()\.]+",line)#same as above
    frequencyStructureArray.append([int(x[0]),y[0]])#putting the new strings in the main structure
    histogramArray.append(math.log10(int(x[0])))#same as above but this is the log of the frequency in order for the resulting graphs to not seem so skewed
frequencyStructureArray.sort()#this is to optimize the speed of the program


#Plot the histogram of the largest frequency
plt.figure("RNA Histogram")
plt.hist(histogramArray,bins = 5, ec="black")
plt.xlabel("log10 of Frequencies")
plt.ylabel("Number of Occurences")

#Find the highest and lowest three frequencies and print them
threeLargest = heapq.nlargest(3,frequencyStructureArray)#Used this method, but using the sorted array would be faster.
threeSmallest = heapq.nsmallest(3,frequencyStructureArray)

print("The three largest frequencies are", threeLargest)
print("The three smallest frequencies are ", threeSmallest)

theLargest = threeLargest[0]
theSmallest = threeSmallest[0]
theSecondLargest = threeLargest[1]
theThirdLargest = threeLargest[2]
theSecondSmallest = threeSmallest[1]
theThirdSmallest = threeSmallest[2]

highestFreqHammingDistances = []
smallestFreqHammingDistances = []
secondLargestFreqHammingDistances = []
thirdLargestFreqHammingDistances = []
secondSmallestFreqHammingDistances = []
thirdSmallestFreqHammingDistances = []

#Find the hamming distance for the highest and lowest frequencies
for line in frequencyStructureArray:
    lineArray = list(line[1])
    largestArray = list(theLargest[1])
    smallestArray = list(theSmallest[1])
    secondLargestArray = list(theSecondLargest[1])
    thirdLargestArray = list(theThirdLargest[1])
    secondSmallestArray = list(theSecondSmallest[1])
    thirdSmallestArray = list(theThirdSmallest[1])
    highestFreqHammingDistances.append(hamming(lineArray,largestArray) * len(lineArray))
    smallestFreqHammingDistances.append(hamming(lineArray,smallestArray) * len(lineArray))
    secondLargestFreqHammingDistances.append(hamming(lineArray,secondLargestArray) * len(lineArray))
    thirdLargestFreqHammingDistances.append(hamming(lineArray,thirdLargestArray) * len(lineArray))
    secondSmallestFreqHammingDistances.append(hamming(lineArray,secondSmallestArray) * len(lineArray))
    thirdSmallestFreqHammingDistances.append(hamming(lineArray, thirdSmallestArray) * len(lineArray))

# sorting them
highestFreqHammingDistances.sort()
smallestFreqHammingDistances.sort()
secondLargestFreqHammingDistances.sort()
thirdLargestFreqHammingDistances.sort()
secondSmallestFreqHammingDistances.sort()
thirdSmallestFreqHammingDistances.sort()

#Plot the histograms
plt.figure("Highest Frequencies Histogram")
plt.hist(highestFreqHammingDistances,bins = 5, ec="black")
plt.xlabel("Highest Frequencies Histogram")
plt.ylabel("Number of Occurences")

plt.figure("Second Highest Frequencies Histogram")
plt.hist(secondLargestFreqHammingDistances,bins = 5, ec="black")
plt.xlabel("Second Highest Frequencies Histogram")
plt.ylabel("Number of Occurences")

plt.figure("Third Highest Frequencies Histogram")
plt.hist(thirdLargestFreqHammingDistances,bins = 5, ec="black")
plt.xlabel("Third Highest Frequencies Histogram")
plt.ylabel("Number of Occurences")

plt.figure("Lowest Frequencies Histogram")
plt.hist(smallestFreqHammingDistances,bins = 5, ec="black")
plt.xlabel("Lowest Frequencies Histogram")
plt.ylabel("Number of Occurences")

plt.figure("Second Lowest Frequencies Histogram")
plt.hist(secondSmallestFreqHammingDistances,bins = 5, ec="black")
plt.xlabel("Second Lowest Frequencies Histogram")
plt.ylabel("Number of Occurences")

plt.figure("Third Lowest Frequencies Histogram")
plt.hist(thirdLargestFreqHammingDistances,bins = 5, ec="black")
plt.xlabel("Third Lowest Frequencies Histogram")
plt.ylabel("Number of Occurences")

plt.show()

# Find the mean of the hamming distances
meanOfHighestFreqHammingDistances = statistics.mean(highestFreqHammingDistances)
meanOfSecondHighestFreqHammingDistances = statistics.mean(secondLargestFreqHammingDistances)
meanOfThirdHighestFreqHammingDistances = statistics.mean(thirdLargestFreqHammingDistances)
meanOfSmallestFreqHammingDistances = statistics.mean(smallestFreqHammingDistances)
meanOfSecondSmallestFreqHammingDistances = statistics.mean(secondSmallestFreqHammingDistances)
meanOfThirdSmallestFreqHammingDistances = statistics.mean(thirdSmallestFreqHammingDistances)

print("The mean of the highest frequencies Hamming distance is " + str(round(meanOfHighestFreqHammingDistances,2)))

print("The mean of the second highest frequencies Hamming distance is " + str(round(meanOfSecondHighestFreqHammingDistances,2)))
print("The mean of the third highest frequencies Hamming distance is " + str(round(meanOfThirdHighestFreqHammingDistances,2)))

print("The mean of the smallest frequencies Hamming distance is " + str(round(meanOfSmallestFreqHammingDistances,2)))
print("The mean of the second smallest frequencies Hamming distance is " + str(round(meanOfSecondSmallestFreqHammingDistances,2)))
print("The mean of the third smallest frequencies Hamming distance is " + str(round(meanOfThirdSmallestFreqHammingDistances,2)))
