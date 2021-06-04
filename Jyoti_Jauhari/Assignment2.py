"""
1. decimal to octal
"""
# def decToOctal(n):
#   oct = 0
#   place = 1
#   while n > 0:
#     rem = n % 8
#     oct = place * rem + oct
#     n = n // 8
#     place = place * 10
#   return oct
#
# n = 8
# print(decToOctal(n))
#


""" 2. Write a program that takes two numbers ‘n1’ & ‘n2’ and a character ‘ch’ as input.
- If ch = ‘*’ returns multiplication of the numbers
- If ch = ‘/’ returns quotient after division of the numbers
- If ch = ‘%’ returns remainder after division of the numbers
- If ch = ‘+’ returns addition of the numbers
- If ch = ‘-’ returns sunbtraction of the numbers """

# def calculator(n1, n2,ch):
#     if ch=="*":
#         print(n1*n2)
#     elif ch=="+":
#         print(n1+n2)
#     elif ch=="-":
#         print(n1-n2)
#     elif ch=="%":
#         print(n1%n2)
#     elif ch=="/":
#         print(n1/n2)
# calculator(8,4,"/")

'''
3. Write a function that accepts a character and prints if it is “Uppercase” or
“Lowercase”.
'''
# def check(char):
#     char = ord(char)
#     if 65 <= char <= 90:
#         return 'Uppercase'
#     elif 97 <= char <= 122:
#         return 'Lowercase'
#
# print(check('j'))

'''
4. Write a program to reverse a number: 38105 -> 50183
'''

# def reverse(num):
#     revnum = 0
#     while num:
#         temp = num % 10
#         revnum = (revnum * 10) + temp
#         num //= 10
#     return revnum
#
# print(reverse(38105))

'''
# 5. Write a program to calculate inverse of a number.
# (For calculating inverse, you should have a valid input i.e, for a number of n
# digits, the value of each digit should be 1 to n and is unique.)
# 25413 -> 41532 (in “25413” 2 is at 1st place therefore 1 is placed on 2nd place in
# “41532”. 5 is at 2nd place in “25413” therefore 2 is at 5th place in “41532” and so
# on.
# '''
# # 25413  41532,
#
# def calculatelength(num):
#     count = 0
#     while num:
#         num //= 10
#         count += 1
#     return count
#
# def calculateInverse(num):
#     n = calculatelength(num)
#     index = n
#     print(n)
#     inverse = 0
#     while num:
#         rem = num % 10
#         inverse = inverse + index * pow(10, n - rem)
#         num //= 10
#         index -= 1
#
#     return  inverse
#
# print(calculateInverse(25413))


# '''
# 6. Write a function that takes two integers ‘a’ & ‘b’ and returns its GCD.
# '''

# def gcd(A, B):
#     if B > A:
#         A,B = B,A
#
#     while( B > 0):
#         A, B = B, A%B
#     return A
#
#
# num1 = int(input('Enter First Number: '))
# num2 = int(input('Enter Second Number: '))
#
# print('The GCD of',num1,'and',num2,'is',gcd(num1, num2))

# '''
# 7. Write a function that takes two integers ‘a’ & ‘b’ and returns its LCM.
# '''
#
# # This function computes LCM using gcd
# def compute_lcm(x, y):
#    lcm = (x*y)//gcd(x,y)
#    return lcm
#
# num1 = 15
# num2 = 5
#
# print("The L.C.M. is", compute_lcm(num1, num2))

'''
8. Write a program to count multiple of 5 in an array. Take the input array from the
user.
For eg: {5, 45, 23, 63, 27, 80, 15, 2, 65, 30}
Ans: 6
'''

# def countMultipleof(arr):
#     count = 0
#     for i in arr:
#         if i % 5 == 0:
#             count += 1
#     return count
#
# li = [5, 45, 23, 63, 27, 80, 15, 2, 65, 30]
# print(countMultipleof( li ))

'''
9. Write a program to count prime numbers in an array.
'''
# sieve method can be used if num of ele in array are in thousands, millions or billions

# def checkPrime(ele):
#     num = 2
#     while num * num <= ele:
#         if ele % num == 0:
#             return False
#         num += 1
#     else:
#         return True
#
# def countPrime(arr):
#     count = 0
#     for ele in arr:
#         if checkPrime(ele):
#             count += 1
#     return count

'''
10. Write a function to check if an array is sorted or not.
'''

#can use aany corting algo

# def check_sorted_array(array):
#     for i in range(0,len(array)):
#         for j in range(i,len(array)):
#             if array[i] > array[j]:
#                 return False
#     return True

'''
11.Write a program sort an array that contains only 0’s & 1’s
For eg: {1,0,1,1,1,0,0,0,1,0,0,1,1}
Ans: {0,0,0,0,0,0,1,1,1,1,1,1,1}
'''

# def sortZeroOne(arr):
#     i = 0
#     j = len(arr) - 1
#
#     while j > i:
#         if arr[i] != 0:
#             if arr[j] == 0:
#                 arr[i], arr[j] = arr[j],arr[i]
#                 i += 1
#                 j -= 1
#
#             else:
#                 j -= 1
#
#         else:
#             i += 1
#     return arr
#
# print(sortZeroOne([1,0,1,1,1,0,0,0,1,0,0,1,1]))

'''
12. Write a program to sort odd and even numbers without taking extra space. (place
even numbers first then all the odd numbers}
For eg: {3,8,5,13,6,12,18,5}
Ans: {8,6,12,18,3,5,13,5}

'''
# def sort_odd_even(array):
#     i = 0
#     j = len(array) - 1
#     while i < j:
#         if array[i] % 2 != 0 and array[j] % 2 == 0:
#             swap(array,i,j)
#         else:
#             if array[i] % 2 == 0:
#                 i += 1
#             if array[j] % 2 != 0:
#                 j -= 1

'''
13. Write a function to reverse an array without taking extra space.
'''

# def reverse_without_extra_space(arr):
#     i = 0
#     j = len(arr) - 1
#     while i < j:
#         arr[i], arr[j] = arr[j] , arr[i]
#         i += 1
#         j -= 1

'''
14.Write a program to input an array and a target value, a number. Write a function
which prints all pairs of numbers which sum equals to the target.
For eg: For this array => {3, 1, 11, 2, 9, 7, 4, 5, -1, 13, 6} and target of 8
Ans: (3,5), (1,7), (2,6), (9,-1)

'''

'''
15.Write a program to input an array and a target value, a number. Write a function
which prints all triplets of numbers which sum equals to the target.
For eg: For this array => {3, 1, 2, 9, 7, 5, -1, 6} and target of 9
Ans: (3,1,5), (3,7,-1), (1,2,6), (1,9,-1)
'''
#time - O(N2) , space - O(N)

# def threeNumberSum(array, targetSum):
# 	array.sort()
# 	triplet = []
# 	for i in range (len(array) - 2):
# 		leftptr = i + 1
# 		rightptr = len(array) - 1
# 		while leftptr < rightptr :
# 			currentSum = array[i] + array[leftptr] + array[rightptr]
# 			if currentSum == targetSum:
# 				triplet.append([array[i], array[leftptr], array[rightptr]])
# 			elif currentSum < targetSum :
# 				leftptr += 1
# 			elif currentSum > targetSum :
# 				rightptr -= 1
# 	return triplet

'''
16.Write a program to input an array & print all possible subsets of the array
For eg: for [7, 2, 6] the following subsets are possible
{}
{7}
{2}
{6}
{7,2}
{7,6}
{2,6}
{7,2,6}
'''

numbers = list(map(int, input().split(" ")))

li = [{}]

for i in range(len(numbers)):
    l = {numbers[i]}
    li.append(l)

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        k = {numbers[i], numbers[j]}
        li.append(k)
print(li)

'''
17.Write a program to input an array & print all possible permutations of the array
For eg: for [7, 2, 6] the following subsets are possible
{7,2,6}
{7,6,2}
{2,7,6}
{2,6,7}
{6,2,7}
{6,7,2}
'''