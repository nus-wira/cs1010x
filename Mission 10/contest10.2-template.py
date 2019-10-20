#
# CS1010X --- Programming Methodology
#
# Contest 10.2 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from random import *
from puzzle_AI import *

def flatten(mat):
    return [num for row in mat for num in row]

def AI(mat):
    
    def tile_pos(mat, n):
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col] == n:
                    row_i, col_j = row, col
        return row_i, col_j

    def high(mat):
        return max(flatten(mat))

    def high_n(mat, n):
        t = flatten(mat)
        t.sort(reverse=True)
        return t[n-1]

    #takes matrix, gives max_tile position
    def max_tile(mat):
        return tile_pos(mat, high(mat))

    def max_tile2(mat):
        for i in range(2, len(flatten(mat))):
            if tile_pos(mat, high_n(mat,i)) != max_tile(mat):
                return tile_pos(mat, high_n(mat,i))

    #to move
    MONO_PWR = 1.2
    SMTH_PWR = 0.6
    ZERO_PWR = 4
    
    
    def mono_score(mat):
        total = 0
        
        for row in mat:
            right, left = 0, 0
            for i in range(len(row) - 1):
                if row[i+1] >= row[i]:
                    right += (row[i+1]**MONO_PWR) - (row[i]**MONO_PWR)
                else:
                    left += (row[i]**MONO_PWR) - (row[i+1]**MONO_PWR)
            total += min(left, right)

        return total


    def smooth_score(mat):
            
        total = 0
        for row in mat:
            count = 0
            for i in range(len(row) - 1):
                if row[i] == row[i+1] and row[i] != 0:
                    count += row[i]**SMTH_PWR
                    
                elif count > 0:
                    total += 1 + count
                    count = 0
            if count > 0:
                total += count
                
        return total

    #takes matrix, gives score - higher score for more zeros
    def zero_score(mat):
        return flatten(mat).count(0)**ZERO_PWR

    ZERO_WEIGHT = 270
    SMOOTH_WEIGHT = 700
    MONO_WEIGHT = 47
    
    def total_score(mat):
        zero = zero_score(mat) * ZERO_WEIGHT
        smooth = smooth_score(mat) * SMOOTH_WEIGHT
        mono = mono_score(mat) * MONO_WEIGHT
        return zero + smooth - mono

    def overall_score(mat):
        return total_score(mat) + total_score(transpose(mat))
         
    
    moves = {"w": merge_up, "a":merge_left, "s":merge_down, "d":merge_right}

    lst = [(mat.copy(), 0, [])]
    search_depth = 0
    while search_depth < 1:
        t_lst = []
        for matrix_state in lst:   
            matrix = matrix_state[0]

            
            for move in moves:
                if not moves[move](matrix)[1]:
                    continue
                temp = []
                test_mat = moves[move](matrix)
                
                def ave(f, lst):
                    return sum(list(map(f, lst)))/len(lst)

                score = overall_score(moves[move](matrix)[0])
                
                moveset = matrix_state[2].copy()
                moveset.append(move)

                t_lst.append((test_mat, score, moveset))
                
                
        lst.clear()
        lst.extend(t_lst)
        search_depth += 1
    

    lst.sort(key=lambda x:x[1], reverse=True)
    return lst[0][2][0]



# UNCOMMENT THE FOLLOWING LINES AND RUN TO WATCH YOUR SOLVER AT WORK
##game_logic['AI'] = AI
##gamegrid = GameGrid(game_logic)

# UNCOMMENT THE FOLLOWING LINE AND RUN TO GRADE YOUR SOLVER
# Note: Your solver is expected to produce only valid moves.
get_average_AI_score(AI, True)
