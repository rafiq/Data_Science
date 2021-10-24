# The original code worked for what is it was made for, but after talking with the lead researcher, I see that the code needs to be a lot more robust in order to print out various graphs of various parts of the RNA structures in order to try and find patterns. To accomplish this, I will not hard code everything, but rather use some more flexible functions, data structures, and algorithms that would, for example, be able to quickly and easily input a few numbers and look at the top twenty frequencies and their corresponding hamming distances graphs, the lowest twenty frequencies and their hamming distances, or a random set of frequencies and look at their hamming distances. In addition, this code needs to be able to quickly plot scatterplots using any of the above examples.

# create a count variable (primary key) that will keep track of where the particular frequency is from the original data which has a total around 11K strings

# create a main structure a list to hold the original clean data that will be sorted in ascending order by the frequency

# create a function named the hammingMaker function which will return a hash/object which keys will be the count and the values will be an array of the hamming distance(NOTE: hamming distance is just an integer, then I may make this an integer as well and not an array/list)

# create a function named hammingFiguresMaker which will create figures from the hamming functions object/hash and will label and title the figures based on the count

# create a helper function named meanMaker which will be called in the hammingMaker function to print the means of the results of the hammingMaker fucntion

# create a scatterPlotMaker function which will take in any two arrays/list and make a scatter plot of them. Again using the count variable to set the title and labels.