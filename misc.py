import math


def add_binary(num1, num2):

    if len(num1) > len(num2):
        num2 = ('0' * (len(num2) - len(num1)) + num2)

    elif len(num2) > len(num1):
        num1 = ('0' * (len(num2) - len(num1)) + num1)

    num1 = num1[::-1]
    num2 = num2[::-1]

    print(num1[::-1], num2[::-1])

    carry = 0
    num3 = ''
    for i, j in zip(num1, num2):
        digit = (int(i) + int(j) + carry) % 2
        carry = (int(i) + int(j) + carry) // 2
        num3 += str(digit)

    return str(carry) + num3[::-1]


def karatsuba(num1, num2):

    if len(num1) == 1:
        return int(num1) * int(num2)

    split1 = int(math.floor(len(num1)/2))
    split2 = int(math.floor(len(num2)/2))

    a = num1[0:split1]
    b = num1[split1:len(num1)]

    c = num2[0:split2]
    d = num2[split2: len(num2)]

    ac = karatsuba(a, c)
    abcd = karatsuba(str(int(a) + int(b)), str(int(c) + int(d)))
    bd = karatsuba(b, d)

    print(f'ac is {ac}')
    print(f'bd is {bd}')
    print(f'abcd is {abcd}')

    return ac * (10 ** len(num1)) + bd + (abcd - ac - bd) * (10 ** int(math.floor(len(num1)/2)))
