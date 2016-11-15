import math


def is_prime(n):
    '''
    check if n is prime
    :param n:
    :return:
    '''
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if (n % i) == 0:
            return False
    return True
