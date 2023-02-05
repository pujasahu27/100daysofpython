#Map,Filter and reduce in python
def cube(x):
    return x*x*x
print(cube(2))
#Map
l=[1,2,4,6,4,3]
newl=list(map(cube,l))
print(newl)

l=[1,2,4,6,4,3]
newl=list(map(lambda x: x*x*x,l))
print(newl)

#Filter
def filter_function(a):
    return a>2
l=[1,2,4,6,4,3]
newnewl = list(filter(filter_function,l))
print(newnewl)

#Reduce
from functools import reduce
numbers = [1, 2, 3, 4, 5]

# Calculate the sum of the numbers using the reduce function
sum = reduce(lambda x, y: x + y, numbers)

# Print the sum
print(sum)
