# MAP
# MAP basically means to map the things in the shortest way.
# def cube(x):
#  return x*x*x
# print(cube(2))
# why do we need make a cube function . reality is we dont need to make it . we cn also use lamda function insted of cube

# l = [1,3,5,6,7,8]
# # now have to make cube of all numbers. 1 way is that to put loop in it and do with map its like
# newl = []

# newl = list(map(lambda x: x*x*x, l))
# print(newl)

# # FILTER(1st take function then 2nd take values)
# r
# def filter_function(a):
#    return a>3
# newl= list(filter(filter_function,l))
   
# print(newl)


# REDUCE (cant use it without import)
from functools import reduce
number = [2,3,4,5,6]

sum = reduce(lambda x, y: x + y ,number)
print(sum)


