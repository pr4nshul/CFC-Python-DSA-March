# Print left aligned triangle for n == 5

n = 5
row = 0

while row < n:
    col = 0
    while col <= row:
        print('* ', end=" ")
        col += 1
    print()
    row += 1
