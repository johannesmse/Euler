# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a^2 + b^2 = c2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
import sys
for i in range(1, 997) :
    for j in range(i + 1, 996) :
        k = 1000 - i - j
        if i**2 + j**2 == k**2 :
            print(i, j, k)
            sys.exit(0)
