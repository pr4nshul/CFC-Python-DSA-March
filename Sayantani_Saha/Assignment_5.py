# Question 1:
def move_all_X(string,index=0,li=[],x=[]):

    if len(string)==0:
        return

    if len(string)==index:
        print("".join(li+x))
    
    ch = string[index]

    if ch== 'X':
        x.append(ch)
        move_all_X(string,index+1,li,x)
    
    li.append(ch)
    move_all_X(string,index+1,li,x)


# Question 2:
def getCheese(rows,cols,tx,ty,cx,cy,path=""):
    if (cx>rows or cy>cols):
        return
    
    if (cx==tx and cy==ty):
        print(path)
        return
    
    getCheese(rows,cols,tx,ty,cx+1,cy,path+"H")
    getCheese(rows,cols,tx,ty,cx,cy+1,path+"V")


# Question 3 :
def getCheese2(rows,cols,tx,ty,cx,cy,path=""):
    if(cx>rows or cy>cols):
        return

    if (cx==tx and cy==ty):
        print(path)
        return

    getCheese2(rows,cols,tx,ty,cx+1,cy,path+"H")
    getCheese(rows,cols,tx,ty,cx,cy+1,path+"V")
    getCheese(rows,cols,tx,ty,cx+1,cy+1,path+"D")


# Question 4 :

board =[
    'O','X','O','O',
    'O','O','O','X',
    'O','O','X','O',
    'X','O','O','O',
    'X','X','O','O'
]

def isSafe(board,rows,cols,cx,cy):
    if(cx<rows and cy<cols and board[cx][cy]='O'):
        return True
    return False

def maze(board,rows,cols,cx,cy,sol=[]):
    if(cx==rows-1 and cy==cols-1):
        sol[cx][cy]=1
        return True

    if isSafe(board,rows,cols,cx,cy):
        if maze(board,rows,cols,cx+1,cy,sol)=True:
            sol[cx][cy]=1
            return True

        if maze(board,rows,cols,cx,cy+1,sol)=True:
            sol[cx][cy]=1
            return True
        
    sol[cx][cy]=0
    return False

def solveMaze(board,n,m):
    sol=[[0 for i in range(m)]for i in range(n)]

    if maze(board,n,m,0,0,sol)==False:
        print("None")
        return False

    print(sol)
    return True


#Question 7:
def permute(unproc,proc="",sol=[]):
    if unproc=="":
        sol.append(proc)
        return

    for index in range(len(unproc)):
        ch = unproc[index]
        rem = unproc[:index]+unproc[index+1:]
        permute(rem,proc+ch,sol)

    return sol , len(sol)


# Question 8:
def equalSum(nums, index=0, left=[], right=[]):
    count = 0

    if len(nums)==index:
        if sum(left)==sum(right):
            print(left,":",right)
            return 1
        return 0

    current = nums[index]

    left.append(current)
    count += equalSum(nums,index+1,left,right)
    left.pop()

    right.append(current)
    count += equalSum(nums,index+1,left,right)
    right.pop()

    return count


# Question 9:
def SubArr(nums, target, index=0, sol =[]):
    if len(nums)==index:
        print(sol)
        return 1

    first = nums[index]

    if first < target:
        for i in range(index+1, len(nums)):
            if nums[i]<target and first + nums[i]==target:
               sol.append((first,nums[i]))
    SubArr(nums,target,index+1,sol)


# Question 12:
def isSafe(grid,row,col,value,n):
    for r in range(n):
        if grid[r][col]==value:
            return False

    for c in range(n):
        if grid[row][c]==value:
            return False

    cr = row - (row % 3)
    cc = col - (col % 3)

    for r in range(cr,cr+3):
        for c in range(cc,cc+3):
            if grid[r][c]==value:
                return False
    return True

def soduku(grid,row,col,n):
    if row==n:
        for line in grid:
            print(line)
        return

    if col==n:
        soduku(grid,row+1,col,n)

    if grid[row][col]==0:
        if isSafe(grid,row,col,value,n):
            grid[row][col]= True
            soduku(grid,row,col+1,n)
            grid[row][col]= False
    
    soduku(grid,row,col+1,n)

''' 5, 6, 10, 11 are not done yet '''