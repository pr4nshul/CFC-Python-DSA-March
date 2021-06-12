'''

1. Take as input a 2-D array. Print it as a vertical wave(Column-wise).
Input: 4 4
11 12 13 14
21 22 23 24
31 32 33 34
41 42 43 44
Output: 11, 21, 31, 41, 42, 32, 22, 12, 13, 23, 33, 43, 44, 34, 24, 14
'''


def vertical_pattern(matrix, rows, cols):

    for col in range(cols):
        if col % 2 == 0:
            for row in range(rows):
                print(matrix[row][col],end = " ")
        else:
            for row in range(rows-1,-1,-1):
                print(matrix[row][col], end = " ")
    return

# vertical_pattern(([[11,12,13,14],[21,22,23,24],[31,32,33,34],[41,42,43,44]]), 4,4)
# rows = int(input())
# cols = int(input())
# matrix = [[int(j) for j in input().split()] for i in range(rows)]
# vertical_pattern(matrix, rows, cols)

'''
2. Take as input a 2-D array. Print it as a horizontal wave(Row-wise).
Input: 4 4
11 12 13 14
21 22 23 24
31 32 33 34
41 42 43 44
Output: 11, 12, 13, 14, 24, 23, 22, 21, 31, 32, 33, 34, 44, 43, 42, 41
'''
print()
def horizontal_Pattern(matrix, rows, cols):
    for row in range(rows):
        if row % 2 == 0:
            for col in range(cols):
                print(matrix[row][col],end = " ")
        else:
            for col in range(cols-1,-1,-1):
                print(matrix[row][col], end = " ")

# horizontal_Pattern(([[11,12,13,14],[21,22,23,24],[31,32,33,34],[41,42,43,44]]), 4,4)
# rows = int(input())
# cols = int(input())
# matrix = [[int(j) for j in input().split()] for i in range(rows)]
# vertical_pattern(matrix, rows, cols)

'''
3. Take as input N, an odd number (>=5) . Print the following pattern as given below
for N = 7.
*     * * * *
*     *
*     *
* * * * * * *
      *     *
      *     *
* * * *     *
'''

def print_ganesha_pattern(n):
    for i in range(n):
        for j in range(n):
            if i == n // 2 or j == n // 2:
                print("*", end=" ")
            elif (j == 0 and i <= n // 2) or (j == n - 1 and i >= n // 2) or (i == 0 and j >= n // 2) or (
                    i == n - 1 and j <= n // 2):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

n = int(input())
print_ganesha_pattern(n)


'''
4. Take as input a 2-D array. Print it in spiral form anti-clockwise.
Input: 4 4
11 12 13 14
21 22 23 24
31 32 33 34
41 42 43 44
Output: 11, 21, 31, 41, 42, 43, 44, 34, 24, 14, 13, 12, 22, 32, 33, 23
'''
def anticlockwise_spiralTraverse(array):
    result = []
    startRow, endRow = 0, len(array) - 1
    startCol, endCol = 0, len(array[0]) - 1

    while startRow <= endRow and startCol <= endCol:
        for row in range(startRow, endRow + 1):
            result.append(array[row][startCol])

        for col in range(startCol + 1, endCol + 1):
            result.append(array[endRow][col])

        for row in reversed(range(startRow, endRow)):
            result.append(array[row][endCol])

        for col in reversed(range(startCol + 1, endCol)):
            result.append(array[startRow][col])

        startRow += 1
        startCol += 1
        endRow -= 1
        endCol -= 1

    return result

# array = [[11,12,13,14],[21,22,23,24],[31,32,33,34],[41,42,43,44]]
# rows, cols = map(int,input().split())
# array = [[int(j) for j in input().split()] for i in range(rows)]
# print(anticlockwise_spiralTraverse(array))

'''5. Take as input a 2-D array. Print it in spiral form clockwise.
Input: 4 4
11 12 13 14
21 22 23 24
31 32 33 34
41 42 43 44
Output: 11, 12, 13, 14, 24, 34, 44, 43, 42, 41, 31, 21, 22, 23, 33, 32'''

def spiralTraverse(array):
    result = []
    startRow, endRow = 0, len(array) - 1
    startCol, endCol = 0, len(array[0]) - 1

    while startRow <= endRow and startCol <= endCol:
        for col in range(startCol, endCol + 1):
            result.append(array[startRow][col])

        for row in range(startRow + 1, endRow + 1):
            result.append(array[row][endCol])

        for col in reversed(range(startCol, endCol)):
            result.append(array[endRow][col])

        for row in reversed(range(startRow + 1, endRow)):
            result.append(array[row][startCol])

        startRow += 1
        startCol += 1
        endRow -= 1
        endCol -= 1

    return result

# array = [[11,12,13,14],[21,22,23,24],[31,32,33,34],[41,42,43,44]]
# rows, cols = map(int,input().split())
# array = [[int(j) for j in input().split()] for i in range(rows)]
# print(spiralTraverse(array))

'''
6. Take input ‘n’ and then take ‘n’ more integer as input values of 1st array, then
take ‘m’ as input followed by ‘m’ more integer as input values of 2nd array. Write
a function that returns the sum of two arrays as an array.
Input: 4
3 5 0 7
5
9 0 2 8
Output: 1 2 5 3 5

'''

def sumofarrays(arr1, arr2):
    n1 = 0
    n2 = 0
    i = 0
    j = 0
    last_a1 = len(arr1) - 1
    last_a2 = len(arr2) - 1
    power = 0
    while i < len(arr1) and j < len(arr2):
        n1 += (10 ** power) * (arr1[last_a1 - i])
        i += 1
        n2 += (10 ** power) * (arr2[last_a2 - j])
        j += 1
        power += 1

    result = n1 + n2
    sum = list(map(int, str(result)))
    return sum

# arr1 = [int(item) for item in input().split()]
# arr2 = [int(item) for item in input().split()]
# ans = sumofarrays(arr1, arr2)
# for i in ans:
#     print(i, end=" ")


'''
7. There is a group of MMA fighters standing together in a line. Given the value of
their strengths, find the strength of the strongest fighter in continuous sub-groups
of size k.
Input: 5 3
1 3 1 4 5
Output: 3 4 5
'''
def findstrength(array, subgroup_size):
    i = 0
    result = []
    while i <= len(array) - subgroup_size:
        j = i
        max_strength = array[i]
        while j < i+subgroup_size:
            if array[j] > max_strength:
                max_strength = array[j]
            j += 1
        result.append(max_strength)
        i += 1
    return result

array = [1,2,3,2,1]
# print(findstrength(array, 2))

'''
8. Take 2 arrays as input and find the intersection of the two arrays(elements in
common).
Input: 7
1 2 3 1 2 4 1
2 1 3 1 5 2 2
Output: {1, 1, 2, 2, 3}
'''

def intersection(arr1, arr2):
    result = []
    for number in arr1:
        if number in arr2:
            result.append(number)
            arr2.remove(number)
    return result

# arr1 = [int(item) for item in input().split()]
# arr2 = [int(item) for item in input().split()]
# print(intersection(arr1,arr2))

'''
9. Take an array as input (can have both positive and negative integers), the task is
to compute the sum of minimum and maximum elements of all sub-array of size
‘k’.
Input: 7 4
2 5 -1 7 -3 -1 -2
Output: 18
Hint: Subarrays of size 4 are :
{2, 5, -1, 7}, min + max = -1 + 7 = 6
{5, -1, 7, -3}, min + max = -3 + 7 = 4
{-1, 7, -3, -1}, min + max = -3 + 7 = 4
{7, -3, -1, -2}, min + max = -3 + 7 = 4
Sum of all min & max = 6 + 4 + 4 + 4 = 18
'''

def sum_of_min_and_max_ele_in_subarray(array, subarray_size):
    i = 0
    result = []
    total = 0
    while i <= len(array) - subarray_size:
        j = i
        max_strength = array[i]
        min_strength = array[i]
        while j < i+subarray_size:
            if array[j] > max_strength:
                max_strength = array[j]

            if array[j] < min_strength:
                min_strength = array[j]

            j += 1
        result.append(min_strength + max_strength)
        i += 1

    for i in result:
        total += i

    return total

# array = [2, 5, -1, 7, -3, -1, -2]
# n, k = map(int,input().split())
# array = [int(item) for item in input().split()]
# print(sum_of_min_and_max_ele_in_subarray(array, k))

'''
10.Take as input S, a string. Write a function that replaces every odd character with
the character having just higher ascii code and every even character with the
character having just lower ascii code. Print the value returned.
Input: abcg
Output: badf
'''
def replace_even_odd_character_ascii(s):
    count = 0
    result = ""

    for char in s:
        if count%2 == 0:
            new_char = chr(ord(char) + 1)
            result += new_char
        else:
            new_char = chr(ord(char) - 1)
            result += new_char
        count += 1

    return result
# print(replace_even_odd_character_ascii("abcg"))
# s = input()
# print(replace_even_odd_character_ascii(s))


'''
11.Take as input S, a string. Write a function that toggles the case of all characters
in the string. Print the value returned.
Input: abcDEasW
Output: ABCdeASw
'''

def togglecase(s):
    solution = ""

    for char in s:
        temp = ord(char)

        if temp >= 65 and temp <= 90:
            x = temp - 65
            solution += chr(97 + x)
        else:
            x = temp - 97
            solution += chr(65 + x)

    return solution

# print(togglecase("abcDEasW"))
# s = input()
# print(togglecase(s))

'''
12.Take as input S, a string. Write a program that inserts between each pair of
characters the difference between their ascii codes and print the ans.
Input: acb
Output: a2c-1b
'''
def insert_ascii_difference(s):
    solution = ""
    i = 0
    while i < len(s) - 1:
        solution += s[i] + str(ord(s[i + 1]) - ord(s[i]))
        i += 1

    solution += s[i]
    return solution

# print(insert_ascii_difference("acb"))

'''
13. You are provided with a string consisting of only 'a' and 'b' as the characters.
You have to make it a perfect string. The perfectness of a string is defined as the
maximum length substring of the same characters. You are given a number ‘k’
which denotes the maximum number of characters you can change. Find the
maximum perfectness he can generate by changing not more than ‘k’ characters.
Input: 2 abba
Output: 4

'''

# note : facing issue in 13, will update it's soln soon