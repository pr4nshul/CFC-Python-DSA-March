#Question 1
def deci_to_oct(deci):
    res=0
    place=1
    while deci>0:
        rem=deci%8
        res=place*rem+res
        deci=deci//8
        place=place*10
    return res
deci_to_oct(453)

#Question 2
def calculator(a,b,ch):
    if ch=="*":
        print(a*b)
    elif ch=="+":
        print(a+b)
    elif ch=="-":
        if a>b:
            print(a-b)
        else:
            print(b-a)
    elif ch=="%":
        if a>b:
            print(a%b)
        else:
            print(b%a)
    elif ch=="/":
        print(a/b)
calculator(9,8,"+")


#Question3
def up_or_low(ch):
    if 65<=ord(ch)<=90:
        print("Uppercase")
    
    if 97<=ord(ch)<=122:
        print("Lowercase")
up_or_low("a")


#Question 4
n=int(input())
res=0
while n>0:
    rem=n%10
    res=res*10+rem
    n=n//10
print(res)

#Question 5
n = int(input())
s = str(n)
li = [0]*len(s)
for i in range(len(s)):
    index = int(s[i])
    li[index-1] = str(i+1)
print("".join(li))


#Question 6
def GCD(a,b):
    if a>b:
        while b!=0:
            res=a-b
            a=b
            b=res
        return a
    else:
        while a!=0:
            res=b-a
            b=a
            a=res
        return b
GCD(24,36)


#Question 7
def LCM(a,b):
    if a>b:
        maxim=a
    else:
        maxim=b
    while (1):
        if maxim%a==0 and maxim%b==0:
            print(maxim)
            break
        maxim+=1
LCM(12,24)


#Question 8
numbers=list(map(int,input().split(",")))

count=0
for i in range(len(numbers)):
    if numbers[i]%5==0:
        count+=1
print(count)

#Question 9:
nums = [2, 1, 6, 7, 12, 17]
count = 0
for i in nums:
    if i == 0 or i == 1:
        count += 1
    else:
        j = 2
        while j < i:
            if i % j == 0:
                count += 1
                break
            j += 1
print(len(nums) - count)

#Question 10
def isSorted(numbers):
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            if numbers[i]>numbers[j]:
                return False
            else:
                break
    return True
numbers=list(map(int,input().split(",")))  
isSorted(numbers)


#Question 11
def swap(arr,a,b):
    arr[a],arr[b]=arr[b],arr[a]
    
numbers=list(map(int,input().split(",")))

for i in range(len(numbers)):
    start=0
    end=len(numbers)-1
    
    while start!=end and start<end:
        if numbers[start]==1 and numbers[end]==0:
            swap(numbers,start,end)
            start+=1
            end-=1
        elif numbers[start]==1 and numbers[end]!=0:
            end-=1
        else:
            start+=1
print(numbers)


#Question 12
nums = [3,8,5,13,6,12,18,5]
even = []
odd = []

for i in nums:
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)

print(sorted(even) + sorted(odd))


#Question 13
def reverse(arr,start,end):
    while start<end and start!=end:
        arr[start],arr[end-1]=arr[end-1],arr[start]
        start+=1
        end-=1
    return arr
numbers=list(map(int,input().split(",")))
size=len(numbers)
print(reverse(numbers,0,size))


#Question 14
target=int(input("Target: "))
numbers=list(map(int,input("Elements: ").split(",")))
pairs=[]
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if numbers[i]+numbers[j]==target:
            ele=(numbers[i],numbers[j])
            
            pairs.append(ele)
print(pairs)


#Question 15
target=int(input("Enter target: "))
numbers=list(map(int,input("Enter elements: ").split(",")))
triplets=[]
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        for k in range(j+1,len(numbers)):
            if numbers[i]+numbers[j]+numbers[k]==target:
                ele=(numbers[i],numbers[j],numbers[k])
                triplets.append(ele)
print(triplets)


#Question 16
numbers=list(map(int,input().split(",")))

li=[{}]

for i in range(len(numbers)):
    l={numbers[i]}
    li.append(l)
    
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        k= {numbers[i],numbers[j]}
        li.append(k)
print(li)


#Question 17
nums = [7,2,6]
def permutation(nums):
    if len(nums) == 0:
        print("No permutation")
        return
    base = [nums[0]]
    for i in range(1,len(nums)):
        permute = []
        for j in range(len(base)):
            curr = [base[j]]
            for k in range(0,len(curr) + 1):
                element = curr[:k] + [nums[i]] + curr[k:]
                permute.append(element)
        base = permute
    return base
print(permutation(nums))
