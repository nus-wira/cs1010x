#
# CS1010X --- Programming Methodology
#
# Mission 3
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

###########
# Task 1a #
###########

def compose(f, g):
    return lambda x:f(g(x))

def thrice(f):
    return compose(f, compose(f, f))

def repeated(f, n):
    if n == 0:
        return identity
    else:
        return compose(f, repeated(f, n - 1))

# Your answer here:
# n = 9

###########
# Task 1b #
###########

identity = lambda x: x
add1 = lambda x: x + 1
sq = lambda x: x**2


# (i) print(thrice(thrice)(add1)(6))
# Explanation: the function thrice is applied on thrice,
# causing the function add1 to be applied 3^3 = 27 times onto add1
# it will print 33

# (ii) print(thrice(thrice)(identity)(compose))
# Explanation: identity function applied 27 times on compose. since identity function returns the input,
# it will print the function compose - this compose function will only compose any 2 functions once

# (iii) print(thrice(thrice)(sq)(1))
# Explanation: sq function applied 27 times on 1
# it will print 1

# (iv) print(thrice(thrice)(sq)(2))
# Explanation: sq function applied 27 times on 2
# it will try to print extremely huge number, squaring 27 times
# IDLE fails to print number


###########
# Task 2a #
###########

def combine(f, op ,n):
    result = f(0)
    for i in range(n):
        result = op(result, f(i))
    return result

def smiley_sum(t):
    def f(x):
        if x == 0 or x == 1:
            return x
        else:
            return 2*(x**2) #each term to be added in S(t) is twice the squares

    def op(x, y):
        return x + y

    n  = t + 1

    # Do not modify this return statement
    return combine(f, op, n)

###########
# Task 2b #
###########

def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

def new_fib(n):
    def f(x):
        ...

    def op(x, y):
        ...

    return combine(f, op, n+1)

# Your answer here: Not possible. The nth term in the fibonacci sequence is defined as
# the sum of only the previous two terms in the sequence,
# whereas the combine function combines all n previous terms in the sequence.
# Fibonacci sequence requires the terms to be added up to continually change, and
# the combine function does not allow for this, only adding up a new term one-by-one,
# based on a predefined function.
