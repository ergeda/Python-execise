
def fibonacci_number_dp(n):
    '''
    calculate n-th Fibonacci number via dynamic programming
    :param n:
    :return:
    '''
    assert(n >= 0)

    a, b = 0, 1
    for i in range(2, n+1):
        if i % 2 == 1:
            b += a
        else:
            a += b
    return a if n % 2 == 0 else b


def fibonacci_number_recursive(n):
    '''
    calculate n-th Fibonacci number recursively
    :param n:
    :return:
    '''
    assert(n >= 0)

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_number_recursive(n-2) + fibonacci_number_recursive(n-1)
