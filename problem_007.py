# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?

import math

def sieveOfEratosthenes(n) :
    primes = [True for i in range(n + 1)]
    i = 2
    while i <= math.sqrt(n) :
        if primes[i] :
            j = i**2
            k = 0
            while j <= n :
                primes[j] = False
                k += 1
                j = i**2 + k * i
        i += 1

    n_primes = []
    for i in range(2, n+1) :
        if primes[i] :
            n_primes.append(i)
    print(n_primes[10000])

sieveOfEratosthenes(150000)
