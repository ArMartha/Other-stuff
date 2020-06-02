###Get the Collatz Sequence

def collatz(number):
    collatz = []
    collatz.append(number)
    while number != 1:
        if number % 2 ==0:
            number = number/2
        else:
            number = 3* number +1
        collatz.append(number)
    return collatz
