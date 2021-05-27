# Question 2 :
def sum (n):
    if n==0:
        return

    prevSum = sum(n-1)
    return (n + prevSum)


# Question 3 :
def target(arr, target, index):
    if index<0:
        return -1

    if arr(index) == target:
        return index

    target(arr,target,index-1)


# Question 4:
def targetIndeces(arr, target, index=0, li=[]):
    if index == len(arr):
        return li

    if arr[index] == target:
        li.append(index)

    targetIndeces(arr, target, index+1, li)


# Question 5 :
def reverse(arr, index=0):
    if index == len(arr):
        return

    reverse(arr, index+1)
    print(arr[index])


# Question 9:
def checkStr(s):
    if len(s)==0:
        return True

    if s[0] == 'a':
        if len(s[1:]) and s[1:3]=='bb':
            return checkStr(s[3:])

        else:
            return checkStr(s[1:])

    return False


# Question 11 :
def asciiString(string, ans="", index=0):
    if index == len(string):
        if len(ans)>0:
            print(ans, end =",")
        return

    count = 0
    ch = string[index]
    code = str(ord(ch))

    asciiString(string, ans, index+1)
    asciiString(string, ans+ch, index+1)
    asciiString(string, ans+code, index+1)


# Question 12 :
def checkDuplicate(s, index = 0):
    if len(s)== index:
        return 

    if s[index] == s[index + 1]:
        print(s[:index+1] + "-" + s[index+1:])

    checkDuplicate(s, index+1)


# Question 13:
def removeDuplicate(s):
    if len(s) <= 1:
        return

    ch = s[0]
    substr = s[1:]

    ans = removeDuplicate(substr)

    if ch = ans[0]:
        return ans
    return ch+ans

# Question 15 :
def equalSum(complete, index=0,  left=[], right=[]):
    if(len(complete) == index):
        if(sum(left) == sum(right)):
            print(left, right)
        return

    current = complete[index]

    equalSum(complete, index+1, left+[current], right)
    equalSum(complete, index+1, left, right+[current])

# Question 2 :
def sum (n):
    if n==0:
        return

    prevSum = sum(n-1)
    return (n + prevSum)


# Question 3 :
def target(arr, target, index):
    if index<0:
        return -1

    if arr(index) == target:
        return index

    target(arr,target,index-1)


# Question 4:
def targetIndeces(arr, target, index=0, li=[]):
    if index == len(arr):
        return li

    if arr[index] == target:
        li.append(index)

    targetIndeces(arr, target, index+1, li)


# Question 5 :
def reverse(arr, index=0):
    if index == len(arr):
        return

    reverse(arr, index+1)
    print(arr[index])


# Question 9:
def checkStr(s):
    if len(s)==0:
        return True

    if s[0] == 'a':
        if len(s[1:]) and s[1:3]=='bb':
            return checkStr(s[3:])

        else:
            return checkStr(s[1:])

    return False


# Question 11 :
def asciiString(string, ans="", index=0):
    if index == len(string):
        if len(ans)>0:
            print(ans, end =",")
        return

    count = 0
    ch = string[index]
    code = str(ord(ch))

    asciiString(string, ans, index+1)
    asciiString(string, ans+ch, index+1)
    asciiString(string, ans+code, index+1)


# Question 12 :
def checkDuplicate(s, index = 0):
    if len(s)== index:
        return 

    if s[index] == s[index + 1]:
        print(s[:index+1] + "-" + s[index+1:])

    checkDuplicate(s, index+1)


# Question 13:
def removeDuplicate(s):
    if len(s) <= 1:
        return

    ch = s[0]
    substr = s[1:]

    ans = removeDuplicate(substr)

    if ch = ans[0]:
        return ans
    return ch+ans

# Question 15 :
def equalSum(complete, index=0,  left=[], right=[]):
    if(len(complete) == index):
        if(sum(left) == sum(right)):
            print(left, right)
        return

    current = complete[index]

    equalSum(complete, index+1, left+[current], right)
    equalSum(complete, index+1, left, right+[current])

''' Question 1, 6, 7, 8, 10, 14 will be updated soon'''     