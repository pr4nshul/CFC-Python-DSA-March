def pattern(n,prev=[]):
    if n == 1:
        print(1)
        prev.append(1)
        return prev
    prev = pattern(n - 1, prev)
    curr = []
    for i in range(n):
        if i == 0:
            item = prev[i]
        elif i == n - 1:
            item = prev[i - 1]
        else:
            item = prev[i - 1] + prev[i]
        print(item, end=" ")
        curr.append(item)
    print()
    return curr

def sum_1_to_n(n):
    if n == 1:
        return 1
    subrec = sum_1_to_n(n-1)
    output = n + subrec
    return output

def last_index_of_target(arr,target,index):
    if index == len(arr):
        return -1

    returned_index = last_index_of_target(arr,target,index+1)
    if returned_index != -1:
        return returned_index
    if arr[index] == target:
        return index
    else:
        return -1

def get_array_of_index(arr,target,index,index_arr=[]):
    if index == len(arr):
        return index_arr
    index_arr = get_array_of_index(arr,target,index+1,index_arr)
    if arr[index] == target:
        index_arr = [index] + index_arr
    return index_arr

def swap(arr,i,j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def reverse_an_array(arr,index):
    if index == len(arr):
        return
    reverse_an_array(arr,index+1)
    if index < len(arr)//2:
        return
    swap(arr,len(arr) - index - 1,index)


def inverse(arr,index,inversed=[]):
    if index == len(arr):
        return inversed
    inversed.append(None)
    inverse(arr,index+1,inversed)
    inversed[arr[index]-1] = index + 1
    return inversed

def bubble_sort_recursive(arr,i,j):
    if i == len(arr):
        return
    if j == len(arr) - i - 1:
        return
    if arr[j] > arr[j+1]:
        swap(arr,j,j+1)
    bubble_sort_recursive(arr,i,j+1)
    bubble_sort_recursive(arr,i+1,0)

def findMaxIdx(arr,i,j,index,maxInd=0):
    if index > j:
        return maxInd
    if arr[index] > arr[maxInd]:
        maxInd = index
    maxInd = findMaxIdx(arr,i,j,index+1,maxInd)
    return maxInd

def selection_sort_recursive(arr,i):
    if i == len(arr):
        return
    j = len(arr)-1-i
    maxIndex = findMaxIdx(arr,0,j,0)
    swap(arr,maxIndex,j)
    selection_sort_recursive(arr,i+1)


def check_valid_string_rec(st,index,count,isvalid=True):
    if index == len(st):
        if count > 0:
            return False
        else:
            return isvalid
    if index == 0 and st[index] != 'a':
        return False
    if st[index] != 'a' or st[index] != 'b':
        return False

    if st[index] == 'b':
        if count == 0:
            count += 1
        elif count == 1:
            count = 0

    isvalid = check_valid_string_rec(st,index+1,count,isvalid)
    return isvalid

def check_twins_rec(st,index,count=0):
    if index >= len(st) - 2:
        return count
    if st[index] == st[index+2]:
        count += 1
    count = check_twins_rec(st,index+1,count)
    return count

def subsequences_rec(unprocess,index=0,process=""):
    if index == len(unprocess):
        print(process)
        return
    ch = unprocess[index]
    asc_ch = ord(ch)
    subsequences_rec(unprocess,index+1,process+ch)
    subsequences_rec(unprocess,index+1, process + str(asc_ch))
    subsequences_rec(unprocess, index + 1, process)

def count_subsequences_rec(unprocess,index=0,count=0,process=""):
    if index == len(unprocess):
        count += 1
        return count
    ch = unprocess[index]
    asc_ch = ord(ch)
    count = count_subsequences_rec(unprocess,index+1,count,process+ch)
    count = count_subsequences_rec(unprocess,index+1,count, process + str(asc_ch))
    count = count_subsequences_rec(unprocess, index + 1,count, process)
    return count

def replace_duplicate_consequtive(st,index=0,prev="",result=""):
    if index == len(st):
        return result

    if prev == st[index]:
        result += "-"
    result += st[index]
    prev = st[index]
    return replace_duplicate_consequtive(st,index+1,prev,result)

def replace_duplicate_consequtive(st,index=0,prev="",result=""):
    if index == len(st):
        return result

    if prev != st[index]:
        result += st[index]
    prev = st[index]
    return replace_duplicate_consequtive(st,index+1,prev,result)

def check_balanced_paranthesis(st,start,end,paran_dic={'{':'}','[':']','(':')'},in_paran=False):
    if start == end :
        if not in_paran:
            return True
        else:
            return False
    if start > end:
        return True
    if start == 0 and st[start] in "]})":
        return False

    ch = st[start]
    if ch in "[({":
        in_paran = True
        minIdx = end + 1
        closing = paran_dic[ch]
        for j in range(end,start,-1):
            if st[j] == closing:
                if j < minIdx:
                    minIdx = j
        if minIdx == end + 1:
            return False
        left = check_balanced_paranthesis(st,start+1,minIdx-1,paran_dic)
        right = check_balanced_paranthesis(st,minIdx+1,end,paran_dic)
        return left and right
    else:
        in_paran = False
        return check_balanced_paranthesis(st,start+1,end,paran_dic,in_paran)


def split_array_into_equal_sum_arrays(arr, left=[], right=[], index=0):
    if index == len(arr):
        if sum(left) == sum(right):
            print(left, right, sep=" and ")
        return

    split_array_into_equal_sum_arrays(arr, left + [arr[index]], right, index + 1)
    split_array_into_equal_sum_arrays(arr, left, right + [arr[index]], index + 1)

def split_array_into_equal_sum_arrays_count(arr, left=[], right=[], index=0):
    if index == len(arr):
        if sum(left) == sum(right):
            return 1
        return 0

    count_left= split_array_into_equal_sum_arrays_count(arr, left + [arr[index]], right, index + 1)
    count_right= split_array_into_equal_sum_arrays_count(arr, left, right + [arr[index]], index + 1)
    return count_left+count_right

def get_input_arr(size):
    print("enter array elements :")
    arr = [int(input(f"{i} :")) for i in range(n)]
    return arr


#1
# n = int(input("enter number of rows of pattern"))
# pattern(n)

#2
# n = int(input("enter number to calculate sum upto "))
# print(sum_1_to_n(n))

#3
# inp = input("enter array of integers")
# arr = [int(item) for item in inp.split()]
# target = int(input("enter item to search last index of :"))
# print(last_index_of_target(arr,target,0))

#4
# inp = input("enter array of integers")
# arr = [int(item) for item in inp.split()]
# target = int(input("enter item to search :"))
# print(get_array_of_index(arr,target,0))

#5
# inp = input("enter array of integers")
# arr = [int(item) for item in inp.split()]
# reverse_an_array(arr,0)
# print(arr)

#6
# inp = input("enter array of integers")
# arr = [int(item) for item in inp.split()]
# arr = inverse(arr,0)
# print(arr)

#7
# inp = input("enter array of integers")
# arr = [int(item) for item in inp.split()]
# bubble_sort_recursive(arr,0,0)
# print(arr)

#8
# inp = input("enter array of integers")
# arr = [int(item) for item in inp.split()]
# selection_sort_recursive(arr,0)
# print(arr)

#9
#st = input("enter string to check valid or not :")
#print(check_valid_string_rec(st,0,0))

#10
#st = input("enter string to check twins in :")
#print(check_twins_rec(st,0))

#11
# st = input("enter string for ascii subsequence :")
#a
# print(count_subsequences_rec(st))
#b
# subsequences_rec(st)

#12
# st = input("enter string with duplicate characters in it :")
# print(replace_duplicate_consequtive(st))

#13
# st = input("enter string with duplicate characters in it :")
# print(replace_duplicate_consequtive(st))

#14
# st = input("enter string to check valid ")
# print(check_balanced_paranthesis(st,0,len(st)-1))

#15
n = int(input("enter size of array"))
arr = get_input_arr(n)
split_array_into_equal_sum_arrays(arr)
print(split_array_into_equal_sum_arrays_count(arr))
