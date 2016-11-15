
def greatest_common_divisor(a, b):
    '''
    find the greatest common divisor
    :param a:
    :param b:
    :return:
    '''
    while b != 0:
        a, b = b, a % b
    return a
