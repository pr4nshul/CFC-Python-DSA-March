n = 3
row = 3
row_mirror = 2*n-1
while(row_mirror>=1):
    col=1
    val = 5
    dec_place = n-row
    col_mirror = 1
    while(col_mirror<=2*n-1):
        print('  '+str(val), end="")
        if (dec_place > 0):
            val -= 1
            dec_place -= 1
        g = 2*n-1 - col_mirror
        if(g <= n - row):
            val+=1
        col_mirror+=1
    print()
    row-=1
    row_mirror-=1