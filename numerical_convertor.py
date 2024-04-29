import math

dec_1 = 19
dec_2 = 2572

bin_1 = 10011
bin_2 = 101000001100


def decimalToBinary(decimal):
    """
    function that converts numbers from decimal to binary
    """
    frac, intNum = math.modf(decimal)

    bin_int = []
    bin_frac = []

    rem = divmod(int(intNum), 2)

    while True:
        bin_int = [rem[1]] + bin_int
        rem = divmod(rem[0], 2)
    
        if rem[0] == 1:
            bin_int = [rem[1]] + bin_int
            bin_int = [rem[0]] + bin_int
            break

    joined_answer = int(''.join(map(str,bin_int)))

    return joined_answer

# change binary int to decimal format
def convertInt_binary(binary):
    result = 0
    power = 0

    bin_elements = [elem for elem in str(binary)]
    print(bin_elements)

    for i in range(-1, -(len(bin_elements) + 1), -1):
        if int(bin_elements[i]) == 1:
            result += (2 ** power)

        power += 1
    
    return result

# change binary float to decimal format
def convertFloat_binary(binary):
    result = 0
    power = -1

    bin_elements = [elem for elem in str(binary)]
    print(bin_elements)

    for i in range(len(bin_elements)):
            elem = int(bin_elements[i])
            if elem == 1:
                result += (2 ** power)

            power -= 1

    return result

result = binaryToDecimal(10011.01)
print(result)

print("###############################################")

res = convertInt_binary('10011')
rest = convertFloat_binary('01')
print(res)
print(rest)