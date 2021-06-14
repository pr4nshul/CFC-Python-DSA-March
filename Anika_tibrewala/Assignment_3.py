Assignment 3

#Q1
def vertical_pattern(matrix, rows, cols):

    for col in range(cols):
        if col % 2 == 0:
            for row in range(rows):
                print(matrix[row][col],end = " ")
        else:
            for row in range(rows-1,-1,-1):
                print(matrix[row][col], end = " ")
    return
#Q2
print()
def horizontal_Pattern(matrix, rows, cols):
    for row in range(rows):
        if row % 2 == 0:
            for col in range(cols):
                print(matrix[row][col],end = " ")
        else:
            for col in range(cols-1,-1,-1):
                print(matrix[row][col], end = " ")

#q3
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


#Q4
def counterClockspiralPrint(m, n, arr) :
    k = 0; l = 0
     
    
    cnt = 0
 
    total = m * n
 
    while (k < m and l < n) :
        if (cnt == total) :
            break
 
        for i in range(k, m) :
            print(arr[i][l], end = " ")
            cnt += 1
         
        l += 1
 
        if (cnt == total) :
            break
 
        for i in range (l, n) :
            print( arr[m - 1][i], end = " ")
            cnt += 1
         
        m -= 1
         
        if (cnt == total) :
            break
 
        
        if (k < m) :
            for i in range(m - 1, k - 1, -1) :
                print(arr[i][n - 1], end = " ")
                cnt += 1
            n -= 1
 
        if (cnt == total) :
            break
 
        
        if (l < n) :
            for i in range(n - 1, l - 1, -1) :
                print( arr[k][i], end = " ")
                cnt += 1
                 
            k += 1
             
 
arr = [ [ 1, 2, 3, 4 ],
        [ 5, 6, 7, 8 ],
        [ 9, 10, 11, 12 ],
        [ 13, 14, 15, 16 ] ]
         
counterClockspiralPrint(R, C, arr)

#Q6
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

#q8
def intersection(arr1, arr2):
    result = []
    for number in arr1:
        if number in arr2:
            result.append(number)
            arr2.remove(number)
    return result

#Q9
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
#Q13
for i in range(len(string)):
    if i+1 < len(string):
        str= str + string[i] + str(ord(string[i+1]) - ord(string[i]))
    else:
        str = str + string[i]
