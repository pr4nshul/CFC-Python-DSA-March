Assignment 1

#Q1
def badge(credits):
    if 7500 <= credits:
        print ("Tera leader")
    elif 6000 <= credits and credits < 7500 :
        print("Gega leader")
    elif 4500 <= credits and credits < 6000 :
        print("Mega leader")
    else:
        print("Rising Star")

credits = int(input("Enter credits: "))
badge(credits)

#Q2
def calculateSI(a,r,t):
    return (a*r*t)/100

a = float(input("enter amount: "))
r = float(input("enter rate: "))
t = float(input("enter time: "))
print(calculateSI(a,r,t))

#Q3

gcd(A,B) if A > B = gcd(B, A%B) ( till A%B > 0)

def gcd(A, B):
    if B > A:
        A,B = B,A

    while( B > 0):
        A, B = B, A%B
    return A


num1 = int(input('Enter First Num: '))
num2 = int(input('Enter Second Num: '))

print('The GCD of',num1,'and',num2,'is',gcd(num1, num2))

#Q4

def printEvenAfterOddSeries(limit):
    start = 2
    difference = 4
    while start <= limit:
        print(start, end=" ")
        start +=  difference
        difference += 4
    return

limit = int(input(""))
printEvenAfterOddSeries(limit)

#Q5
def countdig(num):
    count = 0
    while(num > 0):
        num //= 10
        count += 1
    return count

num = int(input("enter num : "))
print(countdig(num))

#Q6

def reversenum(num):
    temp = 0
    while num > 0:
        temp = temp*10 + num % 10
        num //= 10
    return temp

num = int(input("enter the num: "))
print(reversenum(num))

#Q7

n = 5
i = 1
while i <= 5:
    j = 1
    while j<= i:
        print("*", end=" ")
        j += 1
    print()
    i += 1

#Q7(b)
n = 5
i = 1
while i <= 5:
    j = 1
    while j<= i:
        print(j, end=" ")
        j += 1
    print()
    i += 1

#Q7(c)

n = 5
i = 1
while i <= n:
    j = 1
    while j <= n - i:
        print(" ", end=" ")
        j += 1

    j = 1
    p = 1
    while j<=i:
        print(j, end=" ")
        j += 1

    j = 1
    p = i - 1
    while j <= i -1:
        print( p , end=" ")
        j += 1
        p -= 1


    print()
    i += 1

#Q7(d)
n = 5
i = 1
while i<=n:
    j = 1
    while j <= n-i:
        print(" ", end=" ")
        j += 1

    j = 1
    p = i
    while j<=i:
        print(p, end=" ")
        p += 1
        j += 1

    j = 1
    p = 2*(i-1)
    while j<= i-1:
        print(p, end=" ")
        p -= 1
        j += 1

    print()
    i += 1

#Q7(e)
n = 5
i = 0
list1 = []
while i<n:
    temp_li = []
    j = 0
    while j<=i:
        if j == 0 or j == i:
            print("1", end= "  ")
            temp_li.append(1)
        else:
            num = list1[i-1][j-1] + list1[i-1][j]
            print(num,end=" ")
            temp_li.append(num)
        j += 1
    list1.append(temp_li)
    i += 1
    print()

#Q7(h)
n = int(input())
i = 0
rmirror = 1
space = 1
print("* "*(2*n-1))
while rmirror <= 2*n - 3:
    print("* " * (n - 1 - i) + "  " * space + "* " * (n - 1 - i))
    if rmirror < n-1:
        space += 2
        i += 1
    else:
        space -= 2
        i -= 1
    rmirror += 1
print("* "*(2*n-1))

# Q7 g
n=5
for i in range(1,2*n):
    if i<n:
        for j in range(1,2*n+1):
            if j<=i or j>2*n-i:
                print("*",end=" ")
            else:
                print(" ", end=" ")
    elif i==n:
        for j in range(1,2*n+1):
            print("*",end=" ")
    else:
        for j in range(1,2*n+1):
            if j<=(2*n-i) or j>i:
                print("*",end=" ")
            else:
                print(" ",end=" ")
    print()

# Q7 h
n = 5

row_mirr=0
row = n-1
while row_mirr < 2 * n - 1:
    col = 0
    while col < 2 * n - 1:
        if (col > row and col < (2*n - 1) - (row + 1)):
            print(" ",end=" ")
        else:
            print("*",end=" ")
        col = col + 1
    print()
    if (row_mirr < n - 1):
        row = row - 1
    else:
        row = row + 1
    row_mirr = row_mirr + 1
print()
print()


