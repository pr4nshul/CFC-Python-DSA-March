# Print left column count pattern for n == 5

n = 5
row = 1

while row <= n:
    col = 1
    while col <= row:
        print(col, end=" ")
        col += 1
    print()
    row += 1
