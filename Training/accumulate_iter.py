def accumulate_iter(combiner, null_value, term, a, next, b):
    
    def next_n(f, n): #defining applying function f n times
        def repeat_func(x):
            function = x
            for i in range(n):
                function = f(function)
            return function
        return repeat_func
    def max_n(a, f, b): #max times next function applied on a
        count = 0
        while f(a) <= b:
            a = f(a)
            count += 1
        return count
    
    count_total = max_n(a, next, b)
    total = null_value
    
    for i in range(count_total, -1, -1):
        term_n = term(next_n(next, i)(a))
        
        total = combiner(term_n, total)
    return total
