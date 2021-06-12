#Question 1
credits = int(input("Enter the credits: ")) 

if credits>=7500:
    print("Tera Leader")
elif 6000<=credits<7500:
    print("Gega Leader")
elif 4000<=credits<6000:
    print("Mega Leader")
else:
    print("Rising Star")


#Question 2
amount=int(input("Enter amount: "))
rate=int(input("Enter rate: "))
time=int(input("Enter time: "))
interest= amount*(rate/100)*time
Total= amount+interest
print("Total amount: ", Total)


#Question 3
num_1=int(input("Enter first number: "))
num_2=int(input("Enter second number: "))

if num_1>num_2:
    while num_1!=0:
        res=num_1-num_2
        num_1=num_2
        num_2=res
    print(num_2)
else:
    while num_2!=0:
        res=num_2-num_1
        num_2=num_1
        num_1=res
    print(num_1)
    
#Question 4
n = 100
nums = [i for i in range(2, n+1, 2)]
i = 0
count = 0

while i < len(nums):
    print(nums[i], end=" ")
    count += 1
    i = i + 2*count

#Question 5
num=int(input("Enter the number: "))  #Question 5
count=0
while num>0:
    res=num//10
    count+=1
    num=res
print(count)


#Question 6
num=int(input("Enter number: "))
count=0
while num>0:
    digit= num%10
    res=res*10+digit
    num=num//10
print(res)


#Question 7 a
n=5
row=1
while row<=n:
    col=1
    while col<=row:
        print("*", end= " ")
        col +=1
    print()
    row+=1


#Question 7 b
n=5
row=1
while row<=n:
    col=1
    while col<=row:
        print(col, end= " ")
        col +=1
    print()
    row+=1


#Question 7 e
n=5
for i in range(1,n+1):
    if i==1:
        j=i
        print(j,end=" ")
    else:
        j=j*11
        print(j,end=" ")
    print()


#Question 7 f
n=5
for i in range(1,2*n):
    if i==1:
        for j in range(1,2*n):
            if j==n:
                print("*",end=" ")
            else:
                print(" ",end=" ")
    elif i>1 and i<n:
        for j in range(1,2*n):
            if j==n:
                print("*",end=" ")
            if j<(n-i+1) or j>=(2*n-(n-i)-1):
                print(" ",end=" ")
            else:
                print("*",end=" ")
    elif i==n:
        for j in range(1,2*n):
            print("*",end=" ")
    else:
        for j in range(1,2*n):
            if j==n:
                print("*",end=" ")
            elif j<=(i-n) or j>=(2*n-(i-n)):
                print(" ",end=" ")
            else:
                print("*",end=" ")
    print()


# Question 7 g
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


#Question 7 h
# Question 7 h

n=5
for i in range(1,2*n):
    if i==1 or i==2*n-1:
        for j in range(1,2*n):
                print("*",end=" ")
    elif i>1 and i<n:
        for j in range(1,2*n):
            if j==n:
                print(" ",end=" ")
            if j<=(n-i+1) or j>=n+i-1:
                print("*",end=" ")
            else:
                print(" ",end=" ")
    elif i==n:
        for j in range(1,2*n):
            if j==1 or j==2*n-1:
                print("*",end=" ")
            else:
                print(" ", end=" ")
    else:
        for j in range(1,2*n):
            if j==n:
                print(" ",end="")
            elif j<=(i-n+1) or j>=(2*n-1-(i-n)):
                print("*",end=" ")
            else:
                print(" ",end=" ")
    print()

#7 c, 7 d, 7 i --- Will be update as soon as I find a solution 
