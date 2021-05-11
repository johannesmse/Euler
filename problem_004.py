# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.


# Returns true if number is palindromic
def isPalindromic(number) :
    number_str = str(number)
    reverse = ""
    for digit in number_str :
        reverse = digit + reverse

    return number_str == reverse

largest_pal = 0
for i in range(100, 1000) :
    for k in range(100, 1000) :
        if isPalindromic(i * k) and (i * k) > largest_pal :
            largest_pal = i * k

print(largest_pal)
