# Write a program to print even numbers after odd times jump. E.g: 2, 6, 14, 26
# 1,2,3,4,5,6,7,8,10,11,12,13,14,15,16,17,18,
# ANS:: 2,6,14,26
n = int(input('Total number required: '))
skip = 0
skip_counter = 0
digit = 1
arr = []

while n > 0:
    if digit % 2 == 0 and skip_counter != 0:
        skip_counter -= 1
    elif digit % 2 == 0 and skip_counter == 0:
        print(digit, end=" ")
        n -= 1
        if skip == 0:
            skip += 1
        else:
            skip += 2
        skip_counter = skip

    digit += 1
