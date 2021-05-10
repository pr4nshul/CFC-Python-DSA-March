# Q1
credits = int(input("Enter the credits received: "))

if credits >= 7500:
    print("Badge earned: Tera Leader!")
elif 6000 <= credits < 7500:
    print("Badge earned: Gega Leader!")
elif 4500 <= credits < 6000:
    print("Badge earned: Mega Leader!")
else:
    print("Badge earned: Rising star!")

# Q2
amount = int(input("Enter the total amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time period: "))

si = amount*rate*time / 100

print("Simple interest earned is: ", si)

# Q3
def gcd_num(num1, num2):
    if num1 > num2:
        temp = num2
    else:
        temp = num1
    i = 1
    gcd = 1
    while (i < temp + 1):
        if (num1 % i == 0 and num2 % i == 0):
            gcd = i
        i = i + 1
    return gcd


n1 = int(input("Enter first no.: "))
n2 = int(input("Enter second no.: "))
num = gcd_num(n1, n2)
print("GCD of two numbers is: ", end = "")
print(num)

#Q5
num = int(input("Enter a number: "))
count = 0

while(num>0):
    count = count + 1
    num = num // 10

print("Number of digits: ", count)

# Q6
n = int(input("Enter the number: "))

rev_num = 0
rem = 0

while n > 0:
    rem = n % 10
    rev_num = (rev_num*10) + rem
    n = n // 10

print("Reverse number is: ", rev_num)

# Q7 a
n = 5

row = 0
while row < n:
    col = 0
    while(col<=row):
        print("*", end=" ")
        col = col+1
    print()
    row = row+1

# Q7 b

n = 5
row = 0
while row <= n:
    col = 1
    while(col<=row):
        print(col, end=" ")
        col = col+1
    print()
    row = row+1

# Q 7 c

n = 5
row = 0
while row < n:
    col = 0
    count = 1
    while col < n + row:
        if col + row < n - 1:
            print(" ", end=" ")
        else:
            print(count, end=" ")
            if col < n - 1:
                count = count + 1
            else:
                count = count - 1
        col = col + 1
    print()
    row = row + 1

print()
print()


# Q7 e
n=5
j = 1
for i in range(1,n+2):
    if i==1:
        j=i
        print(j,end="")
    else:
        j=j*11
        print(j,end="")
    print()

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
