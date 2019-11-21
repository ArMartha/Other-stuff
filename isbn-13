##CHECK ISBN-13

inpt = input()
isbn_check = [int(x) for x in inpt[:-1]]
lst = [ isbn_check[i]*3 if (i + 1) % 2 == 0 else isbn_check[i] for i in range(0, len(isbn_check))]
check_sum = 10 - sum(lst) % 10
if check_sum == int(inpt[-1]):
    print('Correct!')
else:
    print('Incorrect!')
