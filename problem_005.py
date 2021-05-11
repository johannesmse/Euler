# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def smallestMultiple(divisor) :
    answer = 20
    while True :
        for i in range(2, divisor + 1) :
            if answer % i != 0 :
                break
            if i == divisor :
                return answer
        answer += divisor

print(smallestMultiple(20))
