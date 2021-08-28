# Write a program to reverse a number (9735 -> 5379)

Input = int(input('Enter number : '))
number = abs(Input)
result = 0
while number > 0:
    rem = number % 10
    result = result * 10 + rem
    number //= 10
if Input < 0:
    result = - result
print(result)
