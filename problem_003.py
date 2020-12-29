original = 600851475143
current = original
factors = []

# Returns the lowest prime factor of argument
def lowest_prime_factor(number):
    for i in range(2, number + 1):
        if number % i == 0:
            return i

while True:
    prime_factor = lowest_prime_factor(current)
    factors.append(prime_factor)
    current = int(current / prime_factor)

    # Breaks the loop if the product of the factors = original number
    product = 1
    for prime in factors:
        product = product * prime
    if product == original:
        print(factors[-1])
        break
