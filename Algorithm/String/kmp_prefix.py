
def kmp_prefix(input_str):
    '''
    prefix helper for Knuth-Morris-Pratt (KMP)
    :param input_str:
    :return:
    '''
    prefix = [-1]
    k = -1
    for i in range(1, len(input_str)):
        while k >= 0 and input_str[i] != input_str[k+1]:
            k = prefix[k]
        if input_str[i] == input_str[k+1]:
            k += 1
        prefix.append(k)

    return prefix


def is_repeated_substring_pattern(input_str):
    '''
    check if input_str is with repeated substring pattern
    :param input_str:
    :return:
    '''
    prefix = kmp_prefix(input_str)
    latest_zero = -1
    for i in range(0, len(prefix)):
        if prefix[i] == 0:
            latest_zero = i
        elif latest_zero != -1 and prefix[i] != prefix[i-1]+1:
            latest_zero = -1
    return latest_zero != -1 and (len(prefix)-latest_zero) % latest_zero == 0


# Examples
#input_str = 'abcbababcbababcbaaabcbababcbababcbaaabcbababcbababcba'
#print(kmp_prefix(input_str))
#print(is_repeated_substring_pattern(input_str))

#input_str = 'abababababababababcccccccccccabababab'
#print(kmp_prefix(input_str))
#print(is_repeated_substring_pattern(input_str))
