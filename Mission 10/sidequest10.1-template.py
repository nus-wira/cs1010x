#
# CS1010X --- Programming Methodology
#
# Sidequest 10.1 Template
#
# Note that written answers are commented out to allow us to run your #
# code easily while grading your problem set.

from random import *
from puzzle import GameGrid

###########
# Helpers #
###########

def accumulate(fn, initial, seq):
    if not seq:
        return initial
    else:
        return fn(seq[0],
                  accumulate(fn, initial, seq[1:]))

def flatten(mat):
    return [num for row in mat for num in row]




###########
# Task 1  #
###########

def new_game_matrix(n):
    row = n * [0]
    return n * [row]

def has_zero(mat):
    return 0 in flatten(mat)

def add_two(mat):
    if not has_zero(mat):
        return mat
    
    #finding which 0 to be changed
    flat = flatten(mat)
    n = flat.count(0)
    x = randint(1, n)

    #finding position of 0
    count = 0
    for i in range(len(flat)):
        if flat[i] == 0:
            count += 1
            if count == x:
                index = i
                break

    row_i = index // len(mat)
    col_i = index % len(mat)
    
    #building new matrix
    f_mat = []
    for row in range(len(mat)):
        if row != row_i:
            lst = mat[row]
        else:
            lst = []
            for col in range(len(mat[0])):
                if col != col_i:
                    lst.append(mat[row][col])
                else:
                    lst.append(2)

        f_mat.append(lst)
    
    return f_mat



###########
# Task 2  #
###########

def game_status(mat):
    def has_moves(mat):
        t_mat = transpose(mat)
        for row in range(len(mat)):
            for col in range(len(mat[0]) - 1):
                if mat[row][col] == mat[row][col+1] or t_mat[row][col] == t_mat[row][col+1]:
                    return True
        return False
    if 2048 in flatten(mat):
        return "win"
    elif has_zero(mat) or has_moves(mat):
        return "not over"
    else:
        return "lose"



###########
# Task 3a #
###########


def transpose(mat):
    lst = []
    for j in range(len(mat[0])):
        row = []
        for i in range(len(mat)):
            row += [mat[i][j]]
        
        lst += [row]
    
    return lst


###########
# Task 3b #
###########

def reverse(mat):
    new_mat = []
    for i in range(len(mat)):
        new_mat.append(mat[i][::-1])

    return new_mat



############
# Task 3ci #
############

def merge_left(mat):
    
    #adding a value to leftmost available cell in a row
    def add_n(row,n):
        for i in range(len(row)):
            if row[i] == 0:
                row[i] = n
                break
        return row

    #merging left a single row
    def merge_row(row):
        #filter row to non-empty cells
        f_row = list(filter(lambda x: x != 0, row))
        score = 0
        if not f_row: #empty row
            return row, score
        
        length = len(f_row)
        n_row = (len(row))*[0]
        
        check = False
        for i in range(length):
            if check: #check if curr_t was added to next_t in previous iteration
                check = False
                continue
            
            curr_t = f_row[i]
            if i + 1 == length:
                n_row = add_n(n_row, curr_t)
            else:
                next_t = f_row[i+1]
                if curr_t == next_t:
                    n_row = add_n(n_row, curr_t * 2)
                    score += curr_t * 2
                    check = True
                else:
                    n_row = add_n(n_row, curr_t)
                      
        return n_row, score
    
    n_mat_scores = list(map(merge_row, mat))
    n_mat, scores = list(map(lambda x:x[0], n_mat_scores)), sum(map(lambda x:x[1], n_mat_scores))
    is_valid = mat != n_mat
    
    return n_mat, is_valid, scores
            


#############
# Task 3cii #
#############

def merge_right(mat):
    new_mat = reverse(mat)
    new_mat_merged = merge_left(new_mat)
    new_mat = reverse(new_mat_merged[0])
    
    return (new_mat,) + new_mat_merged[1:]

def merge_up(mat):
    new_mat = transpose(mat)
    new_mat_merged = merge_left(new_mat)
    new_mat = transpose(new_mat_merged[0])
    
    return (new_mat,) + new_mat_merged[1:]

def merge_down(mat):
    new_mat = reverse(transpose(mat))
    new_mat_merged = merge_left(new_mat)
    new_mat = transpose(reverse(new_mat_merged[0]))
    
    return (new_mat,) + new_mat_merged[1:]


###########
# Task 3d #
###########

def text_play():
    def print_game(mat, score):
        for row in mat:
            print(''.join(map(lambda x: str(x).rjust(5), row)))
        print('score: ' + str(score))
    GRID_SIZE = 4
    score = 0
    mat = add_two(add_two(new_game_matrix(GRID_SIZE)))
    print_game(mat, score)
    while True:
        move = input('Enter W, A, S, D or Q: ')
        move = move.lower()
        if move not in ('w', 'a', 's', 'd', 'q'):
            print('Invalid input!')
            continue
        if move == 'q':
            print('Quitting game.')
            return
        move_funct = {'w': merge_up,
                      'a': merge_left,
                      's': merge_down,
                      'd': merge_right}[move]
        mat, valid, score_increment = move_funct(mat)
        if not valid:
            print('Move invalid!')
            continue
        score += score_increment
        mat = add_two(mat)
        print_game(mat, score)
        status = game_status(mat)
        if status == "win":
            print("Congratulations! You've won!")
            return
        elif status == "lose":
            print("Game over. Try again!")
            return

# UNCOMMENT THE FOLLOWING LINE TO TEST YOUR GAME
##text_play()


# How would you test that the winning condition works?
# Your answer: edit new_game_matrix to spawn 1024 tiles. make a move and it says that the game is won 
#


##########
# Task 4 #
##########

def make_state(matrix, total_score):
    return matrix, total_score

def get_matrix(state):
    return state[0]

def get_score(state):
    return state[1]

def make_new_game(n):
    mat = add_two(add_two(new_game_matrix(n)))
    return make_state(mat, 0)

def move(op):
    def f(state):
        mat, valid, score_increment = op(get_matrix(state))
        score = get_score(state)
        if valid:
            score += score_increment
            mat = add_two(mat)
        return make_state(mat, score), valid
    return f

def left(state):
    return move(merge_left)(state)

def right(state):
    return move(merge_right)(state)

def up(state):
    return move(merge_up)(state)

def down(state):
    return move(merge_down)(state)


# Do not edit this #
game_logic = {
    'make_new_game': make_new_game,
    'game_status': game_status,
    'get_score': get_score,
    'get_matrix': get_matrix,
    'up': up,
    'down': down,
    'left': left,
    'right': right,
    'undo': lambda state: (state, False)
}

# UNCOMMENT THE FOLLOWING LINE TO START THE GAME (WITHOUT UNDO)
##gamegrid = GameGrid(game_logic)




#################
# Optional Task #
#################

###########
# Task 5i #
###########

def make_new_record(mat, increment):
    return mat, increment

def get_record_matrix(record):
    return record[0]

def get_record_increment(record):
    return record[1]

############
# Task 5ii #
############

def make_new_records():
    return []

def push_record(new_record, stack_of_records):
    return [new_record] + stack_of_records[:2]

def is_empty(stack_of_records):
    return stack_of_records == []

def pop_record(stack_of_records):
    if is_empty(stack_of_records):
        return None, None, stack_of_records
    record = stack_of_records.pop(0)
    return get_record_matrix(record), get_record_increment(record), stack_of_records

#############
# Task 5iii #
#############

# COPY AND UPDATE YOUR FUNCTIONS HERE
def make_state(matrix, total_score, records):
    return matrix, total_score, records

def get_matrix(state):
    return state[0]

def get_score(state):
    return state[1]

def make_new_game(n):
    mat = add_two(add_two(new_game_matrix(n)))
    return make_state(mat, 0, make_new_records())

def move(op):
    def f(state):
        mat, score, records = get_matrix(state), get_score(state), get_records(state)
        mat, valid, score_increment = op(mat)
        if valid:
            records = push_record(make_new_record(mat, score_increment), records)
            score += score_increment
            mat = add_two(mat)
        return make_state(mat, score, records), valid
    return f

def left(state):
    return move(merge_left)(state)

def right(state):
    return move(merge_right)(state)

def up(state):
    return move(merge_up)(state)

def down(state):
    return move(merge_down)(state)

# NEW FUNCTIONS TO DEFINE
def get_records(state):
    return state[2]

def undo(state):
    if is_empty(get_records(state)):
        return state, False
    records, score = get_records(state), get_score(state)
    mat, score_increment, records = pop_record(records)
    return make_state(mat, score - score_increment, records), True
    


# UNCOMMENT THE FOLLOWING LINES TO START THE GAME (WITH UNDO)
game_logic = {
    'make_new_game': make_new_game,
    'game_status': game_status,
    'get_score': get_score,
    'get_matrix': get_matrix,
    'up': up,
    'down': down,
    'left': left,
    'right': right,
    'undo': undo
}
gamegrid = GameGrid(game_logic)
