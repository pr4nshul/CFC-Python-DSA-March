# Question -7-d

n = 5
row = 1
while row <= n:
    val = row
    col = n
    col_mirror = 0
    while col_mirror < 2 * n - 1:
        if (col > row):
            print('  ', end="")
        else:
            print(val, end=" ")
            if (col_mirror < n - 1):
                val += 1
            else:
                val -= 1
        if (col_mirror < n - 1):
            col -= 1
        else:
            col += 1

        col_mirror += 1

    print()
    row += 1
