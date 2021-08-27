n = 5
row = n
row_mirror = 1
is_row_done = 0
while(row_mirror<=((n*2)-1)):
    col = 1
    col_mirror = 1
    is_done = 0
    while(col_mirror<=((n*2)-1)):
        if(col<row):
            print('   ',end="")
        else:
            print('  *',end="")
        if(col==n):
            is_done=1
        if(is_done==1):
            col-=1
        else:
            col+=1
        col_mirror+=1

    print()
    if(row==1):
        is_row_done=1
    if (is_row_done == 1):
        row += 1
    else:
        row -= 1

    row_mirror += 1

