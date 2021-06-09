#Question 1:
A = [[11,12,13,14], [21,22,23,24], [31,32,33,34], [41,42,43,44]]   

for i in range(len(A)):
    for x in A:
        print(x[i], end = " ")


#Question 2:
A = [[11, 12, 13, 14], [21, 22, 23, 24], [31, 32, 33, 34], [41, 42, 43, 44]]

for i in range(len(A)):
    if i % 2 == 0:
        for j in range(0, len(A), 1):
            print(A[i][j], end=" ")

    else:
        for j in range(len(A)-1, -1, -1):
            print(A[i][j], end=" ")

#Question 3
n = 7
for i in range(n):
    if i == n//2:
        for j in range(n):
            print("*", end = " ")
        print()
        
    elif i == 0:
        for j in range(n):
            if j == i or j >= 3:
                print("*", end = " ")
            else:
                print(" ", end = " ")
        print()
    elif i == n-1:
        for j in range(n):
            if j == n-1 or j <= 3:
                print("*", end = " ")
            else:
                print(" ", end = " ")
        print()
        
    elif i < 3 :
        for j in range(n):
            if j == 0 or j == 3:
                print("*", end = " ")
            else:
                print(" ", end = " ")
        print()
        
    else:
        for j in range(n):
            if j == n-1 or j == 3:
                print("*", end = " ")
            else:
                print(" ", end = " ")
        print()



#Question 6
def sum_of_Arr(A, B, n, m):
    C = []
    if n > m :
        for i in range(m):
            C.append(A[i]+B[i])
    else:
        for i in range(n):
            C.append(A[i]+B[i])
    return C

A = [3, 5, 0, 7]
B = [9, 0, 2, 8, 5]

sum_of_Arr(A, B, 4, 5)


#Question 7
n = 5
m = 3
strength = [1, 3, 1, 4, 5]

minIdx = 0
sub = []
if n < m:
    for i in range(len(strength)):
        if strength[i] == n:
            minIdx = i
else:
    for i in range(len(strength)):
        if strength[i] == m:
            minIdx = i
if n < m:
    for i in range(minIdx, len(strength)):
        if strength[i] >= n and strength[i] <= m:
            sub.append(strength[i])
else:
     for i in range(minIdx, len(strength)):
        if strength[i] >= m and strength[i] <= n:
            sub.append(strength[i])
            
print(sub)


#Question 8
A = list(map(int, input("Enter 1st array: ").split(",")))
B = list(map(int, input("Enter 2nd array: ").split(",")))
res = []

for i in A:
    if i in B:
        res.append(i)
        B.remove(i)
print(sorted(res))


#Question 10
string = "abcg"
s = ""

for i in range(len(string)):
    if i%2 == 0:
        s = s + chr(ord(string[i]) + 1)
    else:
        s = s + chr(ord(string[i]) - 1)
print(s)


#Question 11
string = "abcDEasW"
s = ""

for i in range(len(string)):
    if 65 <= ord(string[i]) <= 90 :
        s = s + string[i].lower()
    if 97 <= ord(string[i]) <= 122 :
        s = s + string[i].upper()
        
print(s)



#Question 12
string = "acb"
s = ""

for i in range(len(string)):
    if i+1 < len(string):
        s= s + string[i] + str(ord(string[i+1]) - ord(string[i]))
    else:
        s = s + string[i]
        
print(s)