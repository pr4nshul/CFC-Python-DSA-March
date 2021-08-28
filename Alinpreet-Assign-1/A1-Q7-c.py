# Print triangle shape counting

n = 5
row = 1
while row <= n:
    col = 1
    col_mirror = 0
    spaces = n - row
    value = 1
    while col_mirror < 2 * n - 1:
        if col <= n - row:
            print('  ', end="")
        else:
            print(value, end=" ")
        #to reverse the space and value
        if col_mirror < n - 1:
            if col > n - row:
                value += 1
            col += 1
        else:
            if col > n - row:
                value -= 1
            col -= 1
        col_mirror += 1
    print()
    row += 1
