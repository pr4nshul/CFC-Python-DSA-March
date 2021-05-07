#Q1
def deci_to_octal(num):
    oct = 0
    place = 1
    while num > 0:
        rem = num % 8
        oct = rem * place + oct
        num = num // 8
        place = place * 10
    return oct

# Q 2
def calculator(num1,num2,oper):
    if oper == '*':
        return num1 * num2
    elif oper == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Not Defined"
    elif oper == '%':
        if num2 != 0:
            return num1 % num2
        else:
            return "Not defined"
    elif oper == '+':
        return num1 + num2
    elif oper == '-':
        return num1 - num2
    else:
        return 'Invalid'

n1 = int(input("Enter first Number: "))
n2 = int(input("Enter second number: "))
op = input("Enter operand: ")
sol = calculator(n1,n2,op)
print(sol)

#Q3

def case(char):
    char = ord(char)
    if 65 <= char <= 90:
        return 'Uppercase'
    elif 97 <= char <= 122:
        return 'Lowercase'
    else:
        return 'Invalid Character'

ch = input("Enter a char:")
res = case(ch)
print(res)

#Q4

n = int(input("Enter the number: "))

rev_num = 0
rem = 0

while n > 0:
    rem = n % 10
    rev_num = (rev_num*10) + rem
    n = n // 10

print("Reverse number is: ", rev_num)

#Q6

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

#Q7

def lcm_num(num1,num2):
    if num1 == num2:
        return num1
    result = num1 * num2
    mul = 1
    while (num1*mul<result):
        if ((num1 * mul) % num2 == 0):
            result = num1 * mul
            break
        mul = mul + 1
    return result

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
sol = lcm_num(n1,n2)
print(sol)

#Q10

def is_sorted(array):
    for i in range(0,len(array)):
        for j in range(i,len(array)):
            if (array[i] > array[j]):
                return False
    return True

#q11

def swap(a, x, y):
    temp = a[x]
    a[x] = a[y]
    a[y] = temp

def sort_array(arr):
    i = 0
    j = len(arr) - 1
    while i < j:
        if (arr[i] == 1 and arr[j] == 0):
            swap(arr, i, j)
        else:
            if arr[i] == 0:
                i += 1
            if arr[j] == 1:
                j -= 1
    print(arr)

arr = [1,0,1,1,1,0,0,0,1,0,0,1,1]
sort_array(arr)

#Q12

def sort_odd_even(array):
    i = 0
    j = len(array) - 1
    while i < j:
        if array[i] % 2 != 0 and array[j] % 2 == 0:
            swap(array,i,j)
        else:
            if array[i] % 2 == 0:
                i += 1
            if array[j] % 2 != 0:
                j -= 1

#Q 14

target = int(input("Enter Target: "))
nums = list(map(int, input("Enter Elements: ").split(",")))
pairs = []
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            sol = (nums[i], nums[j])

            pairs.append(sol)
print(pairs)

#Q 15

target=int(input("Enter target: "))
nums=list(map(int,input("Enter elements: ").split(",")))
triplets=[]
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        for k in range(j+1,len(nums)):
            if nums[i]+nums[j]+nums[k]==target:
                sol=(nums[i],nums[j],nums[k])
                triplets.append(sol)
print(triplets)

# Q 16
