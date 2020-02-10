#
# CS1010X --- Programming Methodology
#
# Mission 7 - Sidequest 1
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from lazy_susan import *

##########
# Task 1 #
##########

def solve_trivial_2(table):
    move = get_table_state(table)
    return flip_coins(table, move)

# test:
##t2_1 = create_table(2)
##solve_trivial_2(t2_1)
##print(check_solved(t2_1))


########################################################
## VISUALIZATION ALTERNATIVE
## Run the following two lines below to see how the
## coins on the table are flipped and rotated.

##t2_1_run = create_table(2)
##run(t2_1_run, solve_trivial_2)
##print(check_solved(t2_1_run))

########################################################
## GUI ALTERNATIVE
## Run the following two lines below to use the
## interactive GUI to solve the table instead.

##t2_1_susan = create_table(2)
##Susan(t2_1_susan)

########################################################





##########
# Task 2 #
##########

def solve_trivial_4(table):
    return solve_trivial_2(table)

# test:
##t4_2 = create_table(4)
##solve_trivial_4(t4_2)
##print(check_solved(t4_2))


########################################################
## VISUALIZATION ALTERNATIVE
## Run the following two lines below to see how the
## coins on the table are flipped and rotated.

##t4_2_run = create_table(4)
##run(t4_2_run, solve_trivial_4)
##print(check_solved(t4_2_run))

########################################################
## GUI ALTERNATIVE
## Run the following two lines below to use the
## interactive GUI to solve the table instead.

##t4_2_susan = create_table(4)
##Susan(t4_2_susan)

########################################################





##########
# Task 3 #
##########

def solve_2(table):
    move = (0,1)
    flip_coins(table, move)
    if check_solved(table):
        return table
    else:
        return(flip_coins(table, move))

# test:
# t2_3 = create_table(2)
# solve_2(t2_3)
# print(check_solved(t2_3))


########################################################
## VISUALIZATION ALTERNATIVE
## Run the following two lines below to see how the
## coins on the table are flipped and rotated.

##t2_3_run = create_table(2)
##run(t2_3_run, solve_2)

########################################################
## GUI ALTERNATIVE
## Run the following two lines below to use the
## interactive GUI to solve the table instead.

# t2_3_susan = create_table(2)
# Susan(t2_3_susan)

########################################################





##########
# Task 4 #
##########

def solve_4(table):

    move_a = (1,0,1,0)
    move_b = (1,1,0,0)
    move_c = (1,0,0,0)
    
    for moves_made in range(2**get_table_size(table)):
        if moves_made%2 == 0:
            flip_coins(table, move_a)
        elif moves_made == 3:
            flip_coins(table, move_c)
        else:
            flip_coins(table, move_b)

        if check_solved(table):
            return table

# test:
# t4_4 = create_table(4)
# solve_4(t4_4)
# print(check_solved(t4_4))


########################################################
## VISUALIZATION ALTERNATIVE
## Run the following two lines below to see how the
## coins on the table are flipped and rotated.

##t4_4_run = create_table(4)
##run(t4_4_run, solve_4)

########################################################
## GUI ALTERNATIVE
## Run the following two lines below to use the
## interactive GUI to solve the table instead.

# t4_4_susan = create_table(4)
# Susan(t4_4_susan)

########################################################





##########
# Task 5 #
##########

def solve(table):    
    def tuple_of_moves(n):
        if n == 2:
            return ((1,0),)

        #assuming N is always a power of 2
        m = int(n/2)
        prev_moves = tuple_of_moves(m)
        final_moves = ()

        #top N/2 - 1 rows
        for i in range(m-1):
            row = 2*prev_moves[i]
            final_moves += (row,)

        middle_row = m*(1,) + m*(0,)
        final_moves += (middle_row,)

        #bottom N/2 - 1 rows
        for i in range(m-1):
            row = prev_moves[i] + m*(0,)
            final_moves += (row,)

        return final_moves

    def algorithm(n):
        if n == 2:
            return (0,)

        prev = algorithm(n-1)
        order = prev + ((n-2),) + prev
        return order  

    #check first if the coins are already solved (n=1 will go here)
    if check_solved(table):
        return table

    n = get_table_size(table)
    moveset = tuple_of_moves(n)
    move_order = algorithm(n)
    
    for i in range(len(move_order)):
        move_n = move_order[i]
        flip_coins(table, moveset[move_n])
        if check_solved(table):
            return table

# test:

t4_5 = create_table(4)
solve(t4_5)
print(check_solved(t4_5))


t8_5 = create_table(8)
solve(t8_5)
print(check_solved(t8_5))

t16_5 = create_table(16)
solve(t16_5)
print(check_solved(t16_5))

# Note: It is not advisable to execute run() if the table is large.
