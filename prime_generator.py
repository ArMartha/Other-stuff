import math


def prime_generator(n):
    """This function prints first n prime number"""
    prime_lst = [2, 3]
    c = 1
    while len(prime_lst) < n:
        c += 2
        flag = False
        j = 0
        while j < len(prime_lst) and prime_lst[j] <= math.sqrt (c):
            if c % prime_lst[j] == 0:
                flag = False
                break
            else:
                flag = True
            j += 1
        if flag:
            prime_lst.append(c)

    return(prime_lst)

