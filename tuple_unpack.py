# Tuple Unpacking

# Tuples can be used to output multiple values from a function.
# You need to make a function called calc(), that will take the side length of a square as its argument and return the perimeter and area using a tuple.
# The perimeter is the sum of all sides, while the area is the square of the side length.
#
# Sample Input
# 3
#
# Sample Output
# Perimeter: 12
# Area: 9
def calc(x):
    perimeter = x*4;
    area = x*x;
    return perimeter,area
side = int(input())
p, a = calc(side)

print("Perimeter: " + str(p))
print("Area: " + str(a))


