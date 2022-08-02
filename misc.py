
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


