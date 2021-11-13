# Finding prime numbers is a common coding interview task.
# The given code defines a function isPrime(x), which returns True if x is prime.
# You need to create a generator function primeGenerator(), that will take two numbers as arguments, and use the isPrime() function to output the prime numbers in the given range (between the two arguments).
#
# Sample Input
# 10
# 20
#
# Sample Output
# [11, 13, 17, 19]

def isPrime(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    for n in range(2, x):
        if x % n == 0:
            return False
    return True

def primeGenerator(a, b):
    for i in range(a,b):
        if isPrime(i):
            yield i

f = int(input())
t = int(input())

print(list(primeGenerator(f, t)))