n = 5
row = 1
row_mirror = 0
while(row_mirror<2*n-1):
    col = 1
    col_mirror = 0
    while(col_mirror<2*n+1):
        if(col<=row):
            print('  *',end="")
        else:
            print('   ',end="")
        if(col_mirror < n):
            col+=1
        else:
            col-=1
        col_mirror+=1

    print()
    if(row_mirror < n-1):
        row+=1
    else:
        row-=1
    row_mirror+=1