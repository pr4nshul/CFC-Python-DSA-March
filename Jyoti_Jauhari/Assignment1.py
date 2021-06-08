'''
1. Write the pseudocode & a program to input credits of a Code for Cause
Campus leader and then output the badge of the lead on the basis of
the following criteria:
a. 7500 <= credits : Tera leader
b. 6000 <= credits < 7500 : Gega leader
c. 4500 <= credits < 6000 : Mega leader
d. Credits < 4500 : Rising Star
'''

def badge(credits):
    if 7500 <= credits:
        print ("Tera leader")
    elif 6000 <= credits and credits < 7500 :
        print("Gega leader")
    elif 4500 <= credits and credits < 6000 :
        print("Mega leader")
    else:
        print("Rising Star")

credits = int(input("Enter your credits: "))
badge(credits)


'''
2. Write the pseudocode & a program to calculate the simple interest
based on the inputs(amount, rate, time) provided by the user.
'''

def calculateSI(a,r,t):
    return (a*r*t)/100

a = float(input("enter amount: "))
r = float(input("enter rate: "))
t = float(input("enter time: "))
print(calculateSI(a,r,t))

'''
3. Write the pseudocode & the program to calculate GCD of two numbers.
'''

#method 1 : brute force
def calculategcd(num1,num2):
    if num1 > num2:
        smaller = num2
    else:
        smaller = num1
    for i in range(1,smaller+1):
        if num1 % i == 0 and num2 % i == 0:
            gcd = i
    return gcd

num1 = int(input("enter 1st num: "))
num2 = int(input("enter 2nd num: "))
print(calculategcd(num1,num2))

#using euclid algo

gcd(A,B) if A > B = gcd(B, A%B) ( till A%B > 0)

def gcd(A, B):
    if B > A:
        A,B = B,A

    while( B > 0):
        A, B = B, A%B
    return A


num1 = int(input('Enter First Number: '))
num2 = int(input('Enter Second Number: '))

print('The GCD of',num1,'and',num2,'is',gcd(num1, num2))

'''
4. Write a program to print even numbers after odd times jump.
E.g: 2, 6, 14, 26, …
2 (then jump 1 even number 4) -> 6
6 (then jump 3 even numbers 8, 10, 12) -> 14
14 (then jump 5 even numbers 16,18,20,22,24) -> 26
'''


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


'''
5. Write a program to count the number of digits in a number
eg - 1234
op - 4
'''

def countdig(num):
    count = 0
    while(num > 0):
        num //= 10
        count += 1
    return count

num = int(input("enter num : "))
print(countdig(num))

'''
6. Write a program to reverse a number (9735 -> 5379)
'''

def reversenum(num):
    temp = 0
    while num > 0:
        temp = temp*10 + num % 10
        num //= 10
    return temp

num = int(input("enter the num: "))
print(reversenum(num))

'''
7.patterns for n=5 
'''

'''
a )
 
*
* *
* * *
* * * *
* * * * *

i = n
j = i
value = * 
'''

n = 5
i = 1
while i <= 5:
    j = 1
    while j<= i:
        print("*", end=" ")
        j += 1
    print()
    i += 1

'''
b)
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

i = n
j = i
value = j
'''

n = 5
i = 1
while i <= 5:
    j = 1
    while j<= i:
        print(j, end=" ")
        j += 1
    print()
    i += 1

'''
c)
    1
   121
  12321
 1234321
123454321

    1
   12
  123
 1234
12345

starting spaces
i = n
j = n - i spaces
value = " "

numbers
j <= i
print number, number ++

decreasing num 
j <= i - 1
print number, number ++
 
'''

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

'''
d) 
     1
    232
   34543
  4567654
 567898765 

     1
    23
   345
  4567
 56789
i = 5

for space
j = n - i

for num
j <= i
value = i then i++

none
2
43
654
8765  

j <= i - 1
val = 2*i then i-- (use diff var)
'''

n = 5
i = 1
while i<=n:
    j = 1
    while j <= n-i:
        print(" ", end=" ")
        j += 1

    #for num
    j = 1
    p = i
    while j<=i:
        print(p, end=" ")
        p += 1
        j += 1

    #for mirror num
    j = 1
    p = 2*(i-1)
    while j<= i-1:
        print(p, end=" ")
        p -= 1
        j += 1

    print()
    i += 1

'''
e)
n = 5

1
1  1
1  2  1
1  3  3  1
1  4  6  4  1

i = n
j = i

val = 
if j==0 or j==i
append 1 to a
print 1

else:
num = a[i-1][j-1] + a[i-1][j]
append and print

'''
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

'''
f) diamond
n = 5
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
    
rmirror = 2*n-1
i = n
j = 2*i - 1 stars    
'''

n = 5
i = 1
rmirror = 1

while rmirror <= (2*n-1):
    j = 1
    while j <= n - i:
        print(" ", end=" ")
        j += 1

    j = 1
    while j <= 2*i - 1:
        print("*", end=" ")
        j += 1

    if rmirror < n:
        i += 1
    else:
        i -= 1

    rmirror += 1
    print()


'''
g) butterfly pattern


*                 *
* *             * *
* * *         * * *    
* * * *     * * * *
* * * * * * * * * *
* * * *     * * * *
* * *         * * *
* *             * *
*                 *       

n = 5
star = i
space = 2*n - 2, then -2

for down half
* * * *     * * * *
* * *         * * *
* *             * *
*                 * 

i = n-1  
star = (n - i)
space = 2

'''

n = 5
space = 2*n - 2
i = 1
while i <= n:
    print("* "*i + "  "*space + "* "*i)
    space -= 2
    i += 1
#lowerhalf
i = 1
space = 2
while i<= n-1:
    print("* " *(n-i) + "  " * space + "* " *(n-i))
    space += 2
    i += 1

'''
h) hollow diamond
* * * * * * * * * 
* * * *   * * * *
* * *       * * *
* *           * *
*               *
* *           * *
* * *       * * *
* * * *   * * * *  
* * * * * * * * *

n = 5
star 1 st line

* * * *   * * * *
* * *       * * *
* *           * *
*               *
* *           * *
* * *       * * *
* * * *   * * * *  

n = 5
7 row = 2n - 3

space = 2*i - 3 or space = 1 then +2
star = n - i

'''
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


'''
i)
5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 5
5 4 3 3 3 3 3 4 5
5 4 3 2 2 2 3 4 5
5 4 3 2 1 2 3 4 5
5 4 3 2 2 2 3 4 5
5 4 3 3 3 3 3 4 5
5 4 4 4 4 4 4 4 5
5 5 5 5 5 5 5 5 5

'''

'''
basic pattern :
5
54
543
5432
54321
'''
# n = 5
# i = 1
# while i <= n:
#     j = 1
#     p = n
#     while j<=i:
#         print(p, end=" ")
#         p -= 1
#         j += 1
#     print()
#     i += 1


'''
row mirror:
5 5 5 5 5 
5 4 4 4 4 
5 4 3 3 3 
5 4 3 2 2 
5 4 3 2 1 
5 4 3 2 2 
5 4 3 3 3 
5 4 4 4 4 
5 5 5 5 5 
'''

# n = 5
# i = 1
# i_mirror = 1
# while i_mirror <= 2*n - 1:
#     j = 1
#     p = n
#     while j <= n:
#         if j <= i:
#             print(p, end=" ")
#         else:
#             print(n-i+1, end=" ")
#         p -= 1
#         j += 1
#
#     print()
#     if i_mirror <= n - 1:
#         i += 1
#     else:
#         i -= 1
#
#     i_mirror += 1

'''
col mirror :
5 5 5 5 5 5 5 5 5 
5 4 4 4 4 4 4 4 5 
5 4 3 3 3 3 3 4 5 
5 4 3 2 2 2 3 4 5 
5 4 3 2 1 2 3 4 5
'''
# n = 5
# i = 1
# while i <= n:
#     j = 1
#     p = n
#     col_mirror = 1
#     while col_mirror <= 2*n -1 :
#         if j <= i:
#             print(p, end=" ")
#
#         else:
#             print(n-i+1, end=" ")
#
#         if col_mirror <= n-1 :
#             j += 1
#             p -= 1
#         else:
#             j -= 1
#             p += 1
#         col_mirror += 1
#     print()
#     i += 1

#Final code:

n = 5
i = 1
row_mirror = 1
while row_mirror <= 2*n - 1:
    j = 1
    p = n
    col_mirror = 1
    while col_mirror <= 2*n -1 :
        if j <= i:
            print(p, end=" ")

        else:
            print(n-i+1, end=" ")

        if col_mirror <= n-1 :
            j += 1
            p -= 1
        else:
            j -= 1
            p += 1
        col_mirror += 1

    print()
    if row_mirror <= n - 1:
        i += 1
    else:
        i -= 1

    row_mirror += 1