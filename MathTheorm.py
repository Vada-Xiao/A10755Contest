import math

# A certain number is a prime or not. 
def prime(num):
    for i in range(2, math.sqrt(num) + 1):
        if (num % i) == 0:
            return False
    return True

# Set a prime table that less than num and return it.
def getPrimesUpTo(num):
    Numbers = [True for i in range(0, num)]
    Numbers[0] = Numbers[1] = False
    i = 2
    while math.pow(i, 2) < num:
        if Numbers[i]:
            j = i
            while j * i < num:
                Numbers[j * i] = False
                j += 1
        i += 1
    Primes = [i for i in range(0, num) if(Numbers[i])]
    return Primes

def gcd(a, b):
    if(a % b == 0):
        return b
    return gcd(b, a % b)

def Fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return Fib(n - 1) + Fib(n - 2)

# Quick Power method
def QuickPow(a, b):
    PowSum = 1
    while b:
        if b & 1:
            PowSum = PowSum * a
        b = b >> 1
        a = a * a
    return PowSum


Arr = getPrimesUpTo(100)
print(Arr)
print(QuickPow(2,3))
print(Fib(8))