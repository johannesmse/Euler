fib = [1, 2]
new_value = 0
sum = 2

while new_value < 4000000 :
    new_value =  fib[-1] + fib[-2]
    fib.append(new_value)
    if new_value % 2 == 0 :
        sum += new_value
print(sum)
