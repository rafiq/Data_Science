from matplotlib import pyplot as plt
import math
import re
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
    frequency_structure_array.append([int(x[0]),math.log10(int(x[0])),y[0]])

frequency_structure_array.sort(key=lambda x:x[1])
for line in frequency_structure_array:
    count = count + 1#I added the count on this for loop because the data is not ordered in the above for loop
    line.insert(0,count)
#############    1-index,  frequency,  log10 of frequency         structure
#frequencyArray=[11219, 364197924001, 11.561337465902943, '....................']

# create a function named the hamming_maker function which will return a hash/object which keys will be the count and the values will be an array of the hamming distance(NOTE: hamming distance is just an integer, then I may make this an integer as well and not an array/list)

def hamming_maker(start,end,array):# create a function named hammingFiguresMaker which will create figures from the hamming functions 2D list with count as the first element, and the hamming distances as the second element. The labels and title of the figures is based on the count and give the mean as well
    hash = []
    mean_array = []
    for frequencies in range(start,end):
        structure = array[frequencies][3]
        temp = []
        for line in array:
            temp.append(hamming(structure,line[3]))
        hash.append([array[frequencies][0],temp])
        temp = []
    # for line in arr1_hammings: I am trying to modify this code so that I make the hamming graphs and the scatterplots at the same time due to the fact that I need to input the same number of five smallest means as well as the log10 frequency for a RANGE of sequences. So this would be the best place to do those two things. I need to modify my scatter plot function below as well as my hamming_maker function. Also, rename this function to be hamming_scatterplot_maker
    #     smallest5 = sorted(line[1])[0:5]
    #     mean_array.append(get_mean(smallest5))
    return hash
        # print(hamming(structure,array[0][3]))
#######################   1-index  hamming distances
#hamming_maker output  =  [11219, [12, 10,...8]]

def hamming(s1,s2):
    result = 0
    if len(s1)!=len(s2):
        print("Strings are not equal")
    else:
        for x,(i,j) in enumerate(zip(s1,s2)):
            if i != j:
                # print(f'char not math{i,j}in {x}')
                result += 1
    return result


def histogram_maker(array):
    for arr in array:
        mean = get_mean(arr[1])
        plt.figure( str(arr[0]) + " Histogram")
        plt.hist(arr[1])
        plt.xlabel( "Structure Count: " + str(arr[0]) + " Hamming Distances")
        plt.ylabel("Number of Occurences      The mean:" + str(mean))

def get_mean(arr):#Modify this to take a argument for five smallest. if that is true, then return the mean of the five smallest
# create a helper function named meanMaker which will be called in the hamming_maker function to print the means of the results of the hamming_maker fucntion
    return round(sum(arr) / len(arr),2)

#Input any range you want from 0 - 11219 which correlates to the ascending order of the frequencies in the original data

# last_20 = hamming_maker(0,11219,frequency_structure_array)#######################    count  hamming distances
#hamming_maker output  =  [11219, [12, 10,...8]]
# print(histogram_maker(last_20))
# plt.show(last_20)


# create a scatter_plot_maker function which will take in any two arrays/list and make a scatter plot of them. Again using the count variable to set the title and labels.

# x axis = log10 of frequenciies frequency_structure_array[2]Y
# y axis = the mean of the five smallest hamming distances (sort and last 5)
def log10_list_maker (arr):
    log10_frequencies = []
    for line in arr:
        log10_frequencies.append(line[2])
    return log10_frequencies

def scatterplot_maker (arr1_hammings,arr2_log10_freq):
    log10_frequency_array = log10_list_maker(arr2_log10_freq)
    # mean_array = []
    # for line in arr1_hammings:
    #     smallest5 = sorted(line[1])[0:5]
    #     mean_array.append(get_mean(smallest5))
    plt.figure( "Count:" + str(line[0]) + "Scatter Plot")
    plt.xlabel("Count:" + str(line[0]) + "Mean of the last five Hammings")
    plt.ylabel("log10 Frequencies")
    plt.scatter(mean_array,log10_frequency_array)#take the mean of the five smallest for each
    plt.show()

hamming_maker(11100,11219,frequency_structure_array)
# scatterplot_maker(last_20,frequency_structure_array)

# print(frequency_structure_array[:,1])