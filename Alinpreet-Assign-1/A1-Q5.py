# Write a program to count the number of digits in a number.
inputDigit = int(input('Enter input : '))
count = 0
while inputDigit > 0:
    count += 1
    inputDigit = inputDigit // 10
print(count)
