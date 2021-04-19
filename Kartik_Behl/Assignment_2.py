#1 decimal to octal
def deci_to_octal(num):
    octal = 0
    place = 1
    while num > 0:
        rem = num % 8
        octal = rem * place + octal
        num = num // 8
        place = place * 10
    return octal


#2 calculator
def calculator(num1,num2,oper):
    if oper == '*':
        return num1 * num2
    elif oper == '/':
        if num2 != 0:
            return num1 / num2
        return "Can't Divide by 0"
    elif oper == '%':
        if num2 != 0:
            return num1 % num2
        return "Can't Modulo by 0"
    elif oper == '+':
        return num1 + num2
    elif oper == '-':
        return num1 - num2
    else:
        return 'Invalid Operation'

#3 checkcase of character
def checkcase(char):
    char = ord(char)
    if 65 <= char <= 90:
        return 'Uppercase'
    elif 97 <= char <= 122:
        return 'Lowercase'
    else:
        return 'Invalid Character'

#4 reverse a number
def reverse_num(num):
    num_reversed = 0
    place = 10
    while num > 0:
        lastdig = num % 10
        num_reversed =  num_reversed * place + lastdig
        num = num // 10
    return num_reversed


#5 inverse of a number
def get_inverse(num):
    arr = get_array_from_number(num)
    result_arr = [None]*len(arr)
    for i in range(len(arr)):
        result_arr[arr[i] - 1] = i+1
    return get_number_from_array(result_arr)

#utility method for inverse
def get_number_from_array(result_arr):
    number = 0
    for elem in result_arr:
        number = number * 10 + elem
    return number

#utility method for inverse
def get_array_from_number(num):
    arr = []
    while num > 0:
        arr.insert(0,num%10)
        num = num // 10
    return arr

#6 GCD OF 2 numbers
def gcd_of_2(num1,num2):
    divident,divisor = num1,num2
    if num1 == num2:
        return num1
    elif num1 < num2:
        divident = num2
        divisor = num1

    while divident % divisor > 0:
        temp = divident % divisor
        divident = divisor
        divisor = temp
    return divisor

#7 LCM OF 2 numbers
def lcm_of_2(num1,num2):
    if num1 == num2:
        return num1
    result = num1 * num2
    multiplier = 1
    while num1 * multiplier < result:
        if (num1 * multiplier) % num2 == 0:
            result = num1 * multiplier
            break
        multiplier += 1
    return result

#8 count multiples of 5 in array
def count_multiples_of_five(array):
    count_5 = 0
    for element in array:
        if element % 5 == 0:
            count_5 += 1
    return count_5

#Utility that returns an array of given size
def get_array():
    size = int(input("Enter size for array :"))
    array = []
    print("Enter array elements :")
    for i in range(size):
        array.append(int(input("Enter element {i} : ")))
    return array

#Utility for count primes in array
def check_prime(ele):
    num = 2
    while num * num <= ele:
        if ele % num == 0:
            return False
        num += 1
    else:
        return True

#9 count prime numbers in array
def count_prime_in_array(array):
    count = 0
    for ele in array:
        if check_prime(ele):
            count += 1
    return count

#10 check if array is sorted or not
def check_sorted_array(array):
    for i in range(0,len(array)):
        for j in range(i,len(array)):
            if array[i] > array[j]:
                return False
    return True

#utility for sorting
def swap(unsorted_arr, src, tgt):
    temp = unsorted_arr[src]
    unsorted_arr[src] = unsorted_arr[tgt]
    unsorted_arr[tgt] = temp

#11 sort arrays of 0's and 1's
def sort_1_0_array(array):
    i = 0
    j = len(array) - 1
    while i < j:
        if array[i] == 1 and array[j] == 0:
            swap(array, i, j)
        else:
            if array[i] == 0:
                i += 1
            if array[j] == 1:
                j -= 1

#12 sort odd and even numbers of array
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

#13 reverse an array without taking extra space
def reverse_without_extra_space(array):
    i = 0
    j = len(array) - 1
    while i < j:
        swap(array,i,j)
        i += 1
        j -= 1

#14 pairs with a given sum
def pairs_with_given_sum(array,target_sum):
    for i in range(len(array) - 1):
        value_to_search = target_sum - array[i]
        for j in range(i+1,len(array)):
            if array[j] == value_to_search:
                print(f'({array[i]},{array[j]})',end=" ")


#15 triplets with a given sum
def triplets_with_given_sum(array,target_sum):
    for i in range(len(array) - 2):
        for j in range(i+1,len(array)-1):
            value_to_search = target_sum - array[j] - array[i]
            for k in range(j + 1, len(array)):
                if array[k] == value_to_search:
                    print(f'({array[i]},{array[j]},{array[k]})',end=" ")

# subsets of an array
def subsets_of_an_array(array):
    base_set = [[]]
    for item in array:
        list_subset_to_append = []
        for subset_idx in range(0,len(base_set)):
            curr_subset = []
            for base_set_item in base_set[subset_idx]:
                curr_subset.append(base_set_item)
            curr_subset.append(item)
            list_subset_to_append.append(curr_subset)
        for subset in list_subset_to_append:
            base_set.append(subset)
    return base_set

# permutations of an array
def perm_of_array(array):
    if len(array) == 0:
        return 'No permutations for empty array'
    base_array = [[array[0]]]
    for i in range(1,len(array)):
        list_perm_to_append = []
        for j in range(len(base_array)):
            current_perm = base_array[j]
            for k in range(0,len(current_perm) + 1):
               element = current_perm[:k] + [array[i]] + current_perm[k:]
               list_perm_to_append.append(element)
        base_array = list_perm_to_append
    return base_array

# num = int(input("Enter number is base 10 form :"))
# print(f" {num} in octal form is {deci_to_octal(num)}")

# num1 = float(input("Enter number 1 :"))
# num2 = float(input("Enter number 2 :"))
# oper = input("Enter operation :")
# print(f'result of {num1} {oper} {num2} = {calculator(num1,num2,oper)}')

# char = input("enter character to check case :")
# print(f'The charcter {char} is {checkcase(char)}')

# num = int(input("Enter a number to be reversed :"))
# print(f'{reverse_num(num)}')

# num = int(input("Enter a number to be inversed :"))
# print(f'{get_inverse(num)}')

# num1 = int(input("enter first number for gcd "))
# num2 = int(input("enter second number for gcd"))
# print(f'gcd of {num1}  and {num2} = {gcd_of_2(num1,num2)}')

# num1 = int(input("enter first number for lcm "))
# num2 = int(input("enter second number for lcm"))
# print(f'gcd of {num1}  and {num2} = {lcm_of_2(num1,num2)}')

# array = get_array()
# print(f'count of multiples of 5 in {array} = {count_multiples_of_five(array)}')

# array = get_array()
# print(f'count of prime numbers in {array} = {count_prime_in_array(array)}')

# array = get_array()
# result = 'sorted' if check_sorted_array(array) else 'unsorted'
# print(f'the array {array} is {result}')

# array = get_array()
# sort_1_0_array(array)
# print(f'result array after sorting 0\'s and 1\'s {array}')

# array = get_array()
# sort_odd_even(array)
# print(f'result array after sorting odd and even is {array}')

# array = get_array()
# reverse_without_extra_space(array)
# print(f'array after reversal = {array}')

# array = get_array()
# target_sum = int(input("Enter target sum value"))
# pairs_with_given_sum(array,target_sum)

# array = [3, 1, 2, 9, 7, 5, -1, 6]
# target_sum = int(input("Enter target sum value"))
# triplets_with_given_sum(array,target_sum)

# array = [7,2,6]
# print(subsets_of_an_array(array))

# array = [1,2,3]
# print(perm_of_array(array))

