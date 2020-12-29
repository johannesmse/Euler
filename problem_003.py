original = 600851475143
current = original
prime_factors = []

# Returns the lowest prime factor of argument
def lowest_prime_factor(number):
    for i in range(2, number + 1):
        if number % i == 0:
            return i

# Returns product of factor-list given as argument
def product(factors):
    product = 1
    for factor in factors:
        product *= factor
    return product

# Loops until the product of the factors = original number
while product(prime_factors) != original:
    prime_factor = lowest_prime_factor(current)
    prime_factors.append(prime_factor)
    current = int(current / prime_factor)

print(prime_factors[-1])
