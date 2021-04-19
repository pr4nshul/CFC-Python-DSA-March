#1
user_credit = int(input("Enter credits for Code for Cause Campus Leader"))
if user_credit >= 7500:
    print("Tera leader")
elif 6000 <= user_credit < 7500:
    print("Gega leader")
elif 4500 <= user_credit < 6000:
    print("Mega leader")
else:
    print("Rising Star")
print()
print()

#2
principal = float(input("Enter principal amount : "))
rate = float(input("Enter rate percentage : "))
time = float(input("Enter time : "))
simple_interest = (principal * rate * time )/ 100
print(f"Your Simple Interest for Principal = Rs.{principal} at Rate = {rate}% for Time = {time} years is Rs.{simple_interest}")
print()
print()

#3
#GCD OF 2 NUMBERS
first = int(input("enter  1st integer : "))
second = int(input("enter  2nd integer : "))

divident = second
divisor = first
if first == second:
    divisor = first
elif first > second:
    divident = first
    divisor = second
while divident % divisor > 0:
    temp = divisor
    divisor = divident % divisor
    divident = temp
print(f"GCD OF {first} and {second} is {divisor}")
print()
print()

#4
series_range = int(input("range for even series odd jumps"))
nums = 2
to_add = 4
while nums <= series_range:
    print(nums,end=' ')
    nums += to_add
    to_add += 4
print()
print()

#5
number = int(input("enter integer number"))
entered_num = abs(number)
count = 1 if number == 0 else 0
while entered_num > 0:
    entered_num = entered_num//10
    count += 1
print(f"the number of digits in {number} are {count}")
print()
print()

#6
number = int(input("enter integer number"))
entered_num = number
neg_flag = False
if number < 0 :
    entered_num = abs(number)
    neg_flag = True
reversed_num = 0
while entered_num > 0:
    last_dig = entered_num % 10
    entered_num = entered_num//10
    reversed_num = reversed_num * 10 + last_dig
print(f"the number {number} in reversed form is {reversed_num if not neg_flag else (-1 * reversed_num)}")
print()
print()

#7
#a
row = 0
n = 5
while row < n:
    col = 0
    while col <= row:
        print("*",end=" ")
        col += 1
    print()
    row += 1

print()
print()

#b
row = 0
n = 5
while row < n:
    col = 0
    count_for_col = 1
    while col <= row:
        print(count_for_col,end=" ")
        count_for_col += 1
        col += 1
    print()
    row += 1


print()
print()

#c
row = 0
n = 5
while row < n:
    col = 0
    count_for_col = 1
    while col <= row:
        print(count_for_col,end=" ")
        count_for_col += 1
        col += 1
    print()
    row += 1

print()
print()

#d
row = 0
n = 5
while row < n:
    col = 0
    count_for_col = 1
    while col < n + row :
        if col + row < n - 1:
            print(" ", end=" ")
        else:
            print(count_for_col, end=" ")
            if col < n -1:
                count_for_col += 1
            else:
                count_for_col -= 1
        col += 1
    print()
    row += 1

print()
print()

#e
row = 0
n = 5
count_for_col = 1
while row < n:
    col = 0
    while col < n + row :
        if col + row < n - 1:
            print(" ", end=" ")
        else:
            print(count_for_col, end=" ")
            if col < n - 1:
                count_for_col += 1
            elif col == n + row -1:
                count_for_col += 1
            else:
                count_for_col -= 1
        col += 1
    print()
    row += 1

print()
print()

#f
row = 0
n = 6
prev_arr = []
next_arr = []
while row < n:
    col = 0
    next_arr = list()
    while col <= row :
        if col == 0 and row == 0:
            print(1,end=" ")
            next_arr = [1]
        else:
            val = 0
            if col - 1 != -1 :
                val += prev_arr[col-1]
            if col < len(prev_arr):
                val += prev_arr[col]
            print(val,end=" ")
            next_arr.append(val)
        col += 1
    prev_arr = next_arr
    print()
    row += 1

print()
print()

#g
user_inp = 5
row = 0
row_mirror = 0
while row_mirror < 2 * user_inp - 1:
    col = 0
    while col < user_inp + row:
        if col + row  < user_inp - 1:
            print(" ",end=" ")
        else:
            print("*",end=" ")
        col += 1
    if row_mirror < user_inp - 1 :
        row += 1
    else:
        row -= 1
    print()
    row_mirror += 1

print()
print()

#h
user_inp = 5
row_mirror = 0
row = 0
while row_mirror < 2 * user_inp - 1:
    col = 0
    while col < 2 * user_inp:
        if col > row and col < (2*user_inp) - (row + 1):
            print(" ",end=" ")
        else:
            print("*",end=" ")
        col += 1
    print()
    if row_mirror < user_inp - 1:
        row += 1
    else:
        row -= 1
    row_mirror += 1
print()
print()

#i
user_inp = 5
row_mirror = 0
row = user_inp - 1
while row_mirror < 2 * user_inp - 1:
    col = 0
    while col < 2 * user_inp - 1:
        if col > row and col < (2*user_inp - 1) - (row + 1):
            print(" ",end=" ")
        else:
            print("*",end=" ")
        col += 1
    print()
    if row_mirror < user_inp - 1:
        row -= 1
    else:
        row += 1
    row_mirror += 1
print()
print()

#j
user_inp = 5
row_mirror = 0
row = 0
while row_mirror < 2 * user_inp - 1:
    col = 0
    val = user_inp
    inner = False
    while col < 2 * user_inp - 1:
        if row == 0 or row == 2 * user_inp - 1:
            print(val, end=" ")
        elif col >= row and col <= (2*user_inp - 1) - (row + 1):
            inner = True
            print(val, end=" ")
        else:
            if inner:
                val += 1
                print(val,end=" ")
            else:
                print(val, end=" ")
                val -= 1
        col += 1
    print()
    if row_mirror < user_inp - 1:
        row += 1
    else:
        row -= 1
    row_mirror += 1
print()
print()