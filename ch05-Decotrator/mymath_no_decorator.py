# coding: utf-8

# http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/fibtable.html

# Python設計模式深入解析 p76, p77

known = {0:0, 1:1}
known_num = {0:0}

def nsum(n):
    '''返回前n個數字的和'''
    assert(n >= 0), 'n must be >= 0'
    if n in known_num:
        return known_num[n]
    res =  n + nsum(n-1)
    known_num[n] = res
    return res

def fibonacci(n):
    '''返回費波那契數列的第n個數'''
    assert(n >= 0), 'n must be >= 0'
    if n in known:
        return known[n]
    res = fibonacci(n-1) + fibonacci(n-2)
    known[n] = res
    return res

if __name__ == '__main__':
    from timeit import Timer
    t = Timer('fibonacci(100)', 'from __main__ import fibonacci')
    print(t.timeit())
    print(fibonacci(100)) # 354224848179261915075

    t = Timer('nsum(100)', 'from __main__ import nsum')
    print(t.timeit())
    print(nsum(100)) # 5050
