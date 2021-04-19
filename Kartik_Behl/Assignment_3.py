#1 print vertical wave
def vertical_wave_pattern(array,n):
    top = -1
    left = 0
    count = 0
    while count < n*n:
        if top == -1:
            top += 1
            while top < n:
                count += 1
                print(array[top][left],end=",")
                top += 1
            left += 1
        if top == n and left < n:
            top -= 1
            while top >= 0:
                count += 1
                print(array[top][left],end=",")
                top -= 1
            left += 1

#2 horizontal wave
def horizontal_wave_pattern(array,n):
    top = 0
    left = -1
    count = 0
    while count < n * n:
        if left == -1:
            left += 1
            while left < n:
                count += 1
                print(array[top][left], end=",")
                left += 1
            top += 1
        if left == n and top < n:
            left -= 1
            while left >= 0:
                count += 1
                print(array[top][left], end=",")
                left -= 1
            top += 1
#3 pattern
def draw_pattern(num):
    top = 0
    while top < num:
        left = 0
        while left < num:
            if top < (num//2):
                    if top == 0:
                        if left == 0 or left >= num // 2:
                            print("*",end="")
                        else:
                            print(" ",end="")
                    else:
                        if left == 0 or left == num // 2:
                            print("*",end="")
                        else:
                            print(" ",end="")
            elif top == num//2:
                print("*",end="")
            else:
                if top == num - 1:
                    if left <= num // 2 or left == num - 1:
                        print("*",end="")
                    else:
                        print(" ",end="")
                else:
                    if left == num // 2 or left == num - 1:
                        print("*",end="")
                    else:
                        print(" ",end="")

            left += 1
        top += 1
        print()

#4 spiral anticlockwise
def draw_spiral_anticlock(array):
    length = len(array)
    left = 0
    top =  0
    bottom = length - 1
    right = length - 1
    row,col = 0,0
    count = 0
    direction = "LB"
    while count < length * length:
        if direction == "LB":
            row = top
            col = left
            while row <= bottom:
                print(array[row][col])
                row += 1
                count += 1
            direction = "BR"
            left += 1
        if direction == "BR":
            row = bottom
            col = left
            while col <= right:
                print(array[row][col])
                col += 1
                count += 1
            direction = "RT"
            bottom -= 1
        if direction == "RT":
            row = bottom
            col = right
            while row >= top:
                print(array[row][col])
                row -= 1
                count += 1
            direction = "TL"
            right -= 1
        if direction == "TL":
            col = right
            row = top
            while col >= left:
                print(array[row][col])
                col -= 1
                count += 1
            direction = "LB"
            top += 1

#5 spiral clockwise
def draw_spiral_clockwise(array):
    length = len(array)
    left = 0
    top =  0
    bottom = length - 1
    right = length - 1
    row,col = 0,0
    count = 0
    direction = "LT"
    while count < length * length:
        if direction == "LT":
            row = top
            col = left
            while col <= right:
                print(array[row][col])
                col += 1
                count += 1
            direction = "TR"
            top += 1
        if direction == "TR":
            row = top
            col = right
            while row <= right:
                print(array[row][col])
                row += 1
                count += 1
            direction = "RB"
            right -= 1
        if direction == "RB":
            row = bottom
            col = right
            while col >= left:
                print(array[row][col])
                col -= 1
                count += 1
            direction = "BL"
            bottom -= 1
        if direction == "BL":
            col = left
            row = bottom
            while row >= top:
                print(array[row][col])
                row -= 1
                count += 1
            direction = "LT"
            left += 1


#6 two array sum
def sum_of_two_arrays(first_array,second_array):
    result_arr = []
    i,j = len(first_array) - 1,len(second_array) - 1
    first_num = 0
    second_num = 0
    place = 1
    while i >= 0:
        last_digit = first_array[i]
        first_num =  last_digit * place + first_num
        place *= 10
        i -= 1
    place = 1
    while j >= 0:
        last_digit = second_array[i]
        second_num = last_digit * place + second_num
        place *= 10
        j -= 1
    print(first_num,second_num)
    result = first_num + second_num
    while result > 0:
        result_arr = [result % 10] + result_arr
        result = result // 10
    print(result_arr)


    # i,j = len(first_array) - 1,len(second_array) - 1
    # carry = 0
    # result_array = []
    # while i >= 0 and j >= 0:
    #     result = first_array[i]+ second_array[j] + carry
    #     if result >= 10 :
    #         carry = 1
    #         result -= 10
    #     else:
    #         carry = 0
    #     result_array = [result] + result_array
    #     i -= 1
    #     j -= 1
    # while i >= 0:
    #     result = first_array[i] + carry
    #     if result >= 10:
    #         carry = 1
    #         result -= 10
    #     else:
    #         carry = 0
    #     result_array = [result] + result_array
    #     i -= 1
    # while j >= 0:
    #     result = second_array[j] + carry
    #     if result >= 10:
    #         carry = 1
    #         result -= 10
    #     else:
    #         carry = 0
    #     result_array = [result] + result_array
    #     j -= 1
    # if carry != 0:
    #     result_array = [carry] + result_array
    # print(result_array)

#7 print maximum strength in subgroups of size k
def max_strength_in_continous_subgroup(strength_array,subgroup_value):
    i = 0
    while i <= len(strength_array) - subgroup_value:
        j = i
        max_strength = strength_array[i]
        while j < i+subgroup_value:
            if strength_array[j] > max_strength:
                max_strength = strength_array[j]
            j += 1
        print(max_strength,end=" ")
        i += 1

#8 intersection of 2 arrays
def intersection_of_two_arrays(first_array,second_array):
    checked_array = [False] * len(second_array)
    result_array = []
    for i in range(len(first_array)):
        for j in range(len(second_array)):
            if first_array[i] == second_array[j] and not checked_array[j]:
                result_array += [first_array[i]]
                checked_array[j] = True
                break
    return result_array

#9 total sum of maximum and minimum elements in a subarray of size k
def sum_max_min_subarray_size(array,subarray_size):
    result = 0
    for i in range(len(array)-subarray_size+1):
        min = array[i]
        max = array[i]
        for j in range(i,i+subarray_size):
            if array[j] > max:
                max = array[j]
            if array[j] < min:
                min = array[j]
        result += min + max
    return result

#10 replace odd position with higher ascii and even with lower ascii
def replace_even_odd_position_with_ascii(input_str):
    result_str = ""
    for index in range(len(input_str)):
        if index % 2 == 0:
            result_str += chr(ord(input_str[index]) + 1)
        else:
            result_str += chr(ord(input_str[index]) - 1)
    return  result_str

#11 toggle case of characters
def toggle_case(input_str):
    new_str = ""
    for char in input_str:
        if 65 <= ord(char) <= 90: #character is in lower case
            new_str += chr(ord(char) + 32)
        elif 97 <= ord(char) <= 122:
            new_str += chr(ord(char) - 32)
        else:
            return "Invalid characters in string"
    return new_str

#12 print characters along with ascii difference
def ascii_difference_between(input_str):
    new_str = input_str[0]
    for i in range(1,len(input_str)):
        new_str += str(ord(input_str[i]) - ord(input_str[i-1]))+input_str[i]
    return new_str


#13 perfect substring of maximum length
def get_maximum_perfect_string(input_str,max_changes):
    max_count_sbstr = 1
    if not input_str:
        return 0
    size = len(input_str)
    if  size > 1:
        for i in range(0,size):
            changes = max_changes
            count_subs_str = 0
            prev_char = input_str[i]
            for j in range(i,-1,-1):
                if input_str[j] != prev_char:
                     if changes != 0:
                         changes -= 1
                     else:
                        break
                count_subs_str += 1
            if count_subs_str > max_count_sbstr:
                max_count_sbstr = count_subs_str
    return max_count_sbstr

#utility function to return an array of given size
def get_array(size):
    arr = []
    for i in range(size):
        arr.append(int(input(f"enter element {i} of array")))
    return arr
#utility function to return a 2d array of given size
def get_2d_array(row,col):
    print("enter elements of array")
    arr = [[int(input(f"enter element {i}{j} :"))for j in range(col)] for i in range(row)]
    return arr

#1
# n,m = [int(size) for size in input("enter row and column size (space separated) of 2d array").split(" ")]
# arr = get_2d_array(n,m)
# vertical_wave_pattern(arr,n)

print()

#2
# n,m = [int(size) for size in input("enter row and column size (space separated) of 2d array").split(" ")]
# arr = get_2d_array(n,m)
# horizontal_wave_pattern(arr,n)

#3
# draw_pattern(int(input("enter (odd) number for pattern")))

#4
# n,m = [int(size) for size in input("enter row and column size (space separated) of 2d array").split(" ")]
# arr = get_2d_array(n,m)
# draw_spiral_anticlock(arr)

#5
# n,m = [int(size) for size in input("enter row and column size (space separated) of 2d array").split(" ")]
# arr = get_2d_array(n,m)
# draw_spiral_clockwise(arr)

#6
# n = int(input("enter size of 1st array"))
# first = get_array(n)
# m = int(input("enter size of 2nd array"))
# second = get_array(m)
#
# sum_of_two_arrays(first,second)

#7
# n = int(input("enter size of array"))
# subgroup_value = int(input("enter size of subgroup"))
# strength_array = get_array(n)
# max_strength_in_continous_subgroup(strength_array,subgroup_value)

#8
# n = int(input("enter size of array"))
# first = get_array(n)
# second = get_array(n)
# print(intersection_of_two_arrays(first,second))

#9
# n = int(input("enter size of array"))
# subarray_size = int(input("enter subarray size"))
# array = get_array(n)
# print(sum_max_min_subarray_size(array,subarray_size))
#

#10
# print(replace_even_odd_position_with_ascii("abcg"))

#11
# input_str = input("Enter string of characters :")
# print(toggle_case(input_str))

#12
# input_str = input("Enter string of characters :")
# print(ascii_difference_between(input_str))

#13
# input_str = input("Enter string of only a's and b's :")
# max_changes = int(input("Enter maximum number of changes allowed :"))
# print(get_maximum_perfect_string(input_str,max_changes))