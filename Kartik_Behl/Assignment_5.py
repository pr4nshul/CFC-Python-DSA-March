def move_all_x_to_end(st,ar=[],index=0,index_x=0):
    if index == len(st):
        return "".join(ar)
    ar.append(st[index])
    if st[index] != 'x':
        if ar[index_x] == 'x':
            temp = ar[index_x]
            ar[index_x] = ar[index]
            ar[index] = temp
        return move_all_x_to_end(st, ar, index + 1, index_x + 1)
    else:
        return move_all_x_to_end(st, ar, index + 1, index_x)


def maze_hor_ver(row, col, rind=0, cind=0, move=[],all_moves=[]):
    if rind == row-1 and cind == col-1:
        all_moves.append("".join(move))
        return
    if rind == row:
        return
    if cind == col:
        return
    move.append("H")
    maze_hor_ver(row, col, rind, cind + 1, move)
    move.pop()
    move.append("V")
    maze_hor_ver(row, col, rind + 1, cind, move)
    move.pop()
    return all_moves

def maze_hor_ver_diag(row, col, rind=0, cind=0, move=[],all_moves=[]):
    if rind == row-1 and cind == col-1:
        all_moves.append("".join(move))
        return
    if rind == row:
        return
    if cind == col:
        return
    move.append("H")
    maze_hor_ver_diag(row, col, rind, cind + 1, move)
    move.pop()
    move.append("V")
    maze_hor_ver_diag(row, col, rind + 1, cind, move)
    move.pop()
    move.append("D")
    maze_hor_ver_diag(row, col, rind + 1, cind + 1, move)
    move.pop()
    return all_moves

def board_rightmost(board,row,col,rowsize,colsize,rightmost=[0],count=0):
    if row == rowsize:
        if count > rightmost[0]:
            rightmost[0] = count
            for line in board:
                print(line)
            print("-"*30)
        return count

    if col == colsize:
        return
    if board[row][col] == "X":
       return

    if board[row][col] == "O":
        board[row][col] = 1
        board_rightmost(board,row,col+1,rowsize,colsize,rightmost,count)
        board_rightmost(board, row + 1, col, rowsize, colsize, rightmost, count + col)
        board[row][col] = "O"

def codes_for_numeric_string(input_st,code_dict,idx,processed = []):
    if idx == len(input_st):
        print("".join(processed))
        return
    if idx > len(input_st):
        return

    for i in range(1,3):
        val = code_dict[input_st[idx:idx+i]]
        processed.append(val)
        codes_for_numeric_string(input_st,code_dict,idx+i,processed)
        processed.pop()


def keypad_values_from_numeric_count(input_st,idx,process=[]):
    char_keypad_dict = {1:'abc',2:'def',3:'ghi',4:'jkl',5:'mno',6:'pqrs',7:'tuv',8:'wxyz'}
    count = 0
    if idx == len(input_st):
        return 1
    char_key = int(input_st[idx])
    if char_key in char_keypad_dict:
        char_values = char_keypad_dict[char_key]
        for char in char_values:
            process.append(char)
            count += keypad_values_from_numeric_count(input_st,idx+1,process)
            process.pop()
    return count


def keypad_values_from_numeric_print(input_st,idx,process=[]):
    char_keypad_dict = {1:'abc',2:'def',3:'ghi',4:'jkl',5:'mno',6:'pqrs',7:'tuv',8:'wxyz'}
    if idx == len(input_st):
        print("".join(process))
        return
    char_key = int(input_st[idx])
    if char_key in char_keypad_dict:
        char_values = char_keypad_dict[char_key]
        for char in char_values:
            process.append(char)
            keypad_values_from_numeric_print(input_st,idx+1,process)
            process.pop()


def keypad_values_from_numeric_list(input_st,idx,process=[],result_list=[]):
    char_keypad_dict = {1:'abc',2:'def',3:'ghi',4:'jkl',5:'mno',6:'pqrs',7:'tuv',8:'wxyz'}
    if idx == len(input_st):
        result_list.append("".join(process))
        return
    char_key = int(input_st[idx])
    if char_key in char_keypad_dict:
        char_values = char_keypad_dict[char_key]
        for char in char_values:
            process.append(char)
            keypad_values_from_numeric_list(input_st,idx+1,process,result_list)
            process.pop()
    return result_list


def permutation_print(input_str,  processed = []):
    if input_str == "":
        print("".join(processed))
        return

    for i in range(len(input_str)):
        ch = input_str[i]
        processed.append(ch)
        permutation_print(input_str[0:i]+input_str[i+1:],processed)
        processed.pop()

def permutation_return_list(input_str,  processed = [], result_list = []):
    if input_str == "":
        result_list.append("".join(processed))
        return

    for i in range(len(input_str)):
        ch = input_str[i]
        processed.append(ch)
        permutation_return_list(input_str[0:i]+input_str[i+1:],processed,result_list)
        processed.pop()
    return result_list

def permutation_return_count(input_str,  processed = []):
    count = 0
    if input_str == "":
        return 1

    for i in range(len(input_str)):
        ch = input_str[i]
        processed.append(ch)
        count += permutation_return_count(input_str[0:i]+input_str[i+1:],processed)
        processed.pop()
    return count

def sum_of_left_right_equal(inp_arr,idx,left=[],right=[]):
    if idx == len(inp_arr):
        if sum(left) == sum(right):
            print(f"{left}:{right}")
        return
    left.append(inp_arr[idx])
    sum_of_left_right_equal(inp_arr,idx + 1 ,left,right)
    left.pop()
    right.append(inp_arr[idx])
    sum_of_left_right_equal(inp_arr,idx + 1,left,right)
    right.pop()

def sum_of_left_right_equal_count(inp_arr,idx,left=[],right=[]):
    if idx == len(inp_arr):
        if sum(left) == sum(right):
            return 1
        return 0
    left.append(inp_arr[idx])
    count_l = sum_of_left_right_equal_count(inp_arr,idx + 1 ,left,right)
    left.pop()
    right.append(inp_arr[idx])
    count_r = sum_of_left_right_equal_count(inp_arr,idx + 1,left,right)
    right.pop()
    return count_l + count_r

def subsequence_where_sum_equals_target(arr,target,idx=0,result_list=[],curr_list=[]):
    if idx == len(arr):
        if sum(curr_list) == target:
            result_list.append(curr_list[:])
        return

    curr_list.append(arr[idx])
    subsequence_where_sum_equals_target(arr,target,idx+1,result_list,curr_list)
    curr_list.pop()
    subsequence_where_sum_equals_target(arr, target, idx + 1, result_list, curr_list)
    return result_list

def print_lexographically(num, val=1, result_list=[]):
    if len(result_list) == num:
        print(result_list)
        return
    if val > num:
        return

    result_list.append(val)
    print_lexographically(num,val * 10,result_list)
    if (val + 1) % 10 == 0:
        return
    print_lexographically(num, val + 1, result_list)

def is_safe_pos(board,row,col):
    if row - 1 >= 0:
        if col - 2 >= 0:
            if not board[row - 1][col - 2 ]:
                return False
        if col + 2 < len(board):
            if not board[row - 1][col + 2]:
                return False
    if row - 2 >= 0:
        if col - 1 >= 0:
            if not board[row - 2][col - 1]:
                return False
        if col + 1 < len(board):
            if not board[row - 2][col + 1]:
                return False
    return True


def n_nights_list_moves(board,row,col,moves=[]):
    if row == len(board):
        curr_moves = []
        for line in board:
            curr_moves.append(line[:])
        moves.append(curr_moves)
        return
    if col == len(board):
        n_nights_list_moves(board,row + 1,0,moves)
        return
    if board[row][col]:
        if is_safe_pos(board,row,col):
            board[row][col] = False
            n_nights_list_moves(board,row,col+1,moves)
            board[row][col] = True
        n_nights_list_moves(board, row, col + 1, moves)
    return moves

def n_nights_print_moves(board,row,col):
    if row == len(board):
        for line in board:
            print(line)
        print("")
        return
    if col == len(board):
        n_nights_print_moves(board,row + 1,0)
        return
    if board[row][col]:
        if is_safe_pos(board,row,col):
            board[row][col] = False
            n_nights_print_moves(board,row,col+1)
            board[row][col] = True
        n_nights_print_moves(board, row, col + 1)


def is_safe_sudoku(board,row,col,val):
    for c in range(len(board)):
        if board[row][c] == val:
            return False
    for r in range(len(board)):
        if board[r][col] == val:
            return False
    r_start = row - row % 3
    c_start = col - col % 3
    r_end = r_start + 3
    c_end = c_start + 3
    for r in range(r_start,r_end):
        for c in range(c_start,c_end):
            if board[r][c] == val:
                return False
    return True


def sudoku(board,row,col):
    if row == len(board):
        for line in board:
            print(line)
        print("_"*50)
        return

    if col == len(board):
        sudoku(board,row+1,0)
        return

    if board[row][col] == 0:
        for val in range(1,10):
            if is_safe_sudoku(board,row,col,val):
                board[row][col] = val
                sudoku(board,row,col+1)
                board[row][col] = 0
    else:
        sudoku(board,row,col+1)
#1
# st = input("enter string with characters and x's :")
#print(move_all_x_to_end(st))

#2
# st = input("enter row and col").split()
# row,col = list(map(int,st))
# print(maze(row,col))

#3
# st = input("enter row and col").split()
# row,col = list(map(int,st))
# print(maze_hor_ver_diag(row,col))

#4
# board = []
# for row in range(5):
#         board.append(["O"]*4)
#
# board[1][3]="X"
# board[2][2]="X"
# board[3][0]="X"
# board[4][0]="X"
# board[4][1]="X"
#
# board_rightmost(board,0,0,5,4)

#5
inp_st = input("enter a numeric string to get all possible code values")
code_dict = { str(i-ord('a')+1) :chr(i)  for i in range(ord('a'),ord('z')+1) }
codes_for_numeric_string(inp_st,code_dict,0)

#6
# inp_st = input("enter a numeric string to get all possible phone keypad values")
# print(keypad_values_from_numeric_count(inp_st,0))
# print("-"*50)
# keypad_values_from_numeric_print(inp_st,0)
# print("-"*50)
# print(keypad_values_from_numeric_list(inp_st,0))

#7
# inp_st = input("enter a string for permutations :")
# permutation_print(inp_st)
# print("_"*50)
# print(permutation_return_list(inp_st))
# print("_"*50)
# print(permutation_return_count(inp_st))
# print("_"*50)

#8
# st_arr = input("enter space separated array elements").split()
# arr = list(map(int,st_arr))
# sum_of_left_right_equal(arr,0)
# print(sum_of_left_right_equal_count(arr,0))

#9
# st_arr = input("enter space separated array elements :").split()
# arr = list(map(int,st_arr))
# target = int(input("enter target sum :"))
# print(subsequence_where_sum_equals_target(arr,target))

#10
# num = int(input("enter number to generate lexographic series upto"))
# print_lexographically(num)

#11
#n = int(input("enter size of board"))
#board = [ [True]*n for i in range(n)]
# moves = n_nights_list_moves(board,0,0)
# for board in moves:
#     for row in board:
#         print(row)
#     print("-"*50)
#n_nights_print_moves(board,0,0)

#12
# board = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
#          [5, 2, 0, 0, 0, 0, 0, 0, 0],
#          [0, 8, 7, 0, 0, 0, 0, 3, 1],
#          [0, 0, 3, 0, 1, 0, 0, 8, 0],
#          [9, 0, 0, 8, 6, 3, 0, 0, 5],
#          [0, 5, 0, 0, 9, 0, 6, 0, 0],
#          [1, 3, 0, 0, 0, 0, 2, 5, 0],
#          [0, 0, 0, 0, 0, 0, 0, 7, 4],
#          [0, 0, 5, 2, 0, 6, 3, 0, 0]]
# sudoku(board,0,0)