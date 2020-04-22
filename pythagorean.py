import math
#
#
def pythagorean_triples(src):
    """This function searches pythagorean triples which sum is equal to src"""
    number = math.sqrt(src)

    for n in range(1, int(number)):
        for m in range(n + 1, int(number)):
            a = m ** 2 - n ** 2
            b = 2 * m * n
            c = m * m + n * n
            if a + b + c == src:
                return c**2
