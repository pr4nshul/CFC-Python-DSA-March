'''

1. Take ‘n’ as input and print the following pattern for n = 5 using recursion:
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
'''



'''
2. Take ‘n’ as input and write a recursive function to return the sum of 1 to n.
Eg: for n=5 return 15 (1+2+3+4+5)
'''

def calsum(n):
    if n == 1:
        return 1
    return n + calsum(n-1)

# print(calsum(100))

'''
3. Given an array and a target value, write a recursive function that will return the
last index of the occurrence of that target value. If not present in the array return
-1.
Eg: {3 2 1 8 6 1 3} target = 1
Output: 5

'''
def lastIndex(arr, si, x):
    l = len(arr)
    if si == l:
        return -1
    smallerListOutput = lastIndex(arr, si+1, x)
    if smallerListOutput != -1:
        return smallerListOutput
    else:
        if arr[si] == x:
            return si
        else:
            return -1
# print(lastIndex([1,2,1,12,1], 0, 1))

'''
4. Take an array as input and a target value. Write a recursive function which
returns an array having indices stored in it at which the target value is stored in
the original array.
Eg: {0, 4, 2, 2, 1, 2, 3, 4, 2} target = 2
Output: {2, 3, 5, 8}

'''


def target_index_array(a, target, result=[], index=0):
    if index == len(a):
        return result

    if target == a[index]:
        result.append(index)
    ans = target_index_array(a, target, result, index + 1)

    return ans


# print(target_index_array([1,2,3,1,1],1))

'''
5. Write a recursive function to reverse an array.
a = [5,4,3,2,1]
a = [1,2,3,4,5]
'''

def revarray(a, result = [], si = 0):
    if si == len(a):
        return  result

    revarray(a,result,si+1)
    result.append(a[si])

    return result

# print(revarray([5,4,3,2,1]))

'''
6. Write a recursive function to find the inverse of an array. (for inverse refer
assignment-2)

'''
def inverse_arr(arr,index = 0, inversed=[]):
    if index == len(arr):
        return inversed
    inversed.append(None)
    inverse_arr(arr,index+1,inversed)
    inversed[arr[index]-1] = index + 1
    return inversed

# print(inverse_arr([2,5,4,1,3]))

'''
7. Write a recursive function for Bubble Sort. (Using no loops)
'''

def bubblesort_recursive(arr,i=0,j=0):
    if i == len(arr):
        return
    if j == len(arr) - i - 1:
        return
    if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
    bubblesort_recursive(arr,i,j+1)
    bubblesort_recursive(arr,i+1,0)
    return arr

# print(bubblesort_recursive([5,14,3,2,1]))



'''
8. Write a recursive function for Selection Sort. (Using no loops)
'''


# Utility function to swap values at two indices in the list
def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def findmin(A, j, n, min, minidx = 0):
    if j == n :
        if minidx == 0:
            return min
        else:
            return minidx

    if A[j] < A[min]:
        minidx = j
        min = j

    minidx = findmin(A, j+1, n, min, minidx)
    return minidx

# print(findmin([-2,5,8,4,1,9,3], 2, 7, 1))
# Recursive function to perform selection sort on sublist `A[i…n-1]`
def selectionSort(A, i, n):
    min = i
    if i == len(A):
        return

    min = findmin(A, i+1, n, min)

    swap(A, min, i)

    selectionSort(A, i + 1, n)


A = [3, 5, 8, 4, 1, 9, -2]
selectionSort(A, 0, len(A))
# print(A)

'''
9. Take as input str, a string. Write a recursive function that checks if the string was
generated using the following rules and returns a Boolean value: 
a. the string begins with an 'a' 
b. each 'a' is followed by nothing or an 'a' or "bb" 
c. each "bb" is followed by nothing or an 'a' Print the value returned.
Eg: abba
Output: true
'''

def checkStr(s):
    if len(s) == 0:
        return True

    if s[0] == 'a':
        if len(s[1:]) and s[1:3]=='bb':
            return checkStr(s[3:])

        else:
            return checkStr(s[1:])

    return False

# print(checkStr("abbaa"))

'''
10.Take as input str, a string. A “twin” is defined as two instances of a char
separated by a char. 
E.g. "AxA" the A's make a “twin”. “twins” can overlap, so
"AxAxA" contains 3 “twins” - 2 for A and 1 for x. Write a function which
recursively counts the number of “twins” in a string. Print the value returned.
Eg: AXAXA
Output: 3
'''

def check_twins(str, index = 0, count = 0):
    if index >= len(str) - 2:
        return count
    if str[index] == str[index+2]:
        count += 1
    count = check_twins(str,index+1,count)
    return count

# print(check_twins("AXAXA"))

'''
11.Take as input str, a string. We are concerned with all the possible
ascii-subsequences of str.
E.g. “ab” has following ascii-subsequences “”, “b”,
“98”, “a”, “ab”, “a98”, “97”, “97b”, “9798”
a. Write a recursive function which returns the count of ascii-subsequences
for a given string. Print the value returned.
b. Write a recursive function which prints all possible ascii-subsequences for
a given string (void is the return type for function).
Eg: ab
Output: '' b 98 a ab a98 97 97b 9798
 9
'''

def print_subseq(string , ans="" ,index = 0) :
    if (index == len(string)):
        print(ans)
        return

    ch = string[index]
    print_subseq(string, ans, index + 1)
    print_subseq(string, ans + ch, index + 1)
    print_subseq(string, ans + str(ord(ch)), index + 1)


def count_subseq(string, index=0):
    if (index == len(string)):
        return 1
    count = 0
    ch = string[index]
    count += count_subseq(string, index + 1)
    count += count_subseq(string, index + 1)
    count += count_subseq(string, index + 1)

    return count

# print_subseq("ab")
# print(count_subseq("ab"))


'''
12.Take as input str, a string. Write a recursive function which returns a new string
in which all duplicate consecutive characters are separated by a ‘ - ’. E.g. for
“hello” return “hel-lo”
'''

def consecutive_duplicate_modify(str,index=0,prev="",result=""):
    if index == len(str):
        return result

    if prev == str[index]:
        result += "-"
    result += str[index]
    prev = str[index]
    return consecutive_duplicate_modify(str,index+1,prev,result)

# print(consecutive_duplicate_modify("caabbccdda"))

'''
13. Take as input str, a string. Write a recursive function which returns a new string
in which all duplicate consecutive characters are removed. E.g. for “heeeello”
return “helo”.
'''
def removeduplicates(str):
    if len(str) == 0 or len(str) == 1:
        return str
    if str[0] == str[1]:
        smalloutput = removeduplicates(str[2:])
        return str[0] + smalloutput
    else:
        smalloutput = removeduplicates(str[1:])
        return str[0] + smalloutput

# print(removeduplicates("caabbccdda"))

'''
14.Take as input str, a string. The string is a mathematical expression. Eg: “[a + {b +
(c+d) + e} + f]”. Write a recursive function which checks if the brackets are
balanced or not.

'''

'''
15. Take as input N, a number. Take N more inputs and store that in an array.
a. Write a recursive function which counts the number of ways the array
could be split in two groups, so that the sum of items in both groups is
equal. Each number in the array must belong to one of the two groups.
Print the value returned.
b. Write a recursive function which keeps track of ways an array could be
split in two groups, so that the sum of items in both groups is equal. Each
number in the array must belong to one of the two groups. Return type of
function should be void. Print the two groups, each time you find a
successful split.
Eg: 6
1 2 3 3 4 5
Output: 6
1 2 3 3 and 4 5
1 3 5 and 2 3 4
1 3 5 and 2 3 4
2 3 4 and 1 3 5
2 3 4 and 1 3 5
4 5 and 1 2 3 3
'''

#Note: will upload soln of 1, 14, 15 soon