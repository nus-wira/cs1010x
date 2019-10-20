#
# CS1010X --- Programming Methodology
#
# Mission 2 - Side Quest 2
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

##########
# Task 1 #
##########

# Simplifed Order notations:

# 4^n * n^2
# Ans: 4^n * n^2

# n * 3^n
# Ans: n * 3^n

# 1000000000n^2
# Ans: n^2

# 2^n/1000000000
# Ans: 2^n

# n^n + n^2 + 1
# Ans: n^n

# 4^n + 2^n
# Ans: 4^n

# 1^n
# Ans: 1

# n^2
# Ans: n^2

# Faster order of growth in each group:

# i. 4^n * n^2
# ii. 2^n
# iii. n^n
# iv. n^2


##########
# Task 2 #
##########

# Time complexity: O(n)
# Space complexity: O(n)


##########
# Task 3 #
##########

# Time complexity of bar: O(n)
# Time complexity of foo: O(n^2)

# Space complexity of bar: O(n)
# Space complexity of foo: O(n)

def bar(n):
    if n == 0:
        return 0
    else:
        return n + bar(n - 1)

def foo(n):
    if n == 0:
        return 0
    else:
        return bar(n) + foo(n - 1)

def improved_foo(n):
    def improved_bar(n):
        return int(n*(n+1)/2) #simplified bar

    total = 0

    for i in range(n):
        total += improved_bar(i + 1)
    
    return total

# Improved time complexity: O(n)
# Improved space complexity: O(1)
