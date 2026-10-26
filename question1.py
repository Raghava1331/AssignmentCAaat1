def to_8bit(n):
    return format(n & 0xFF, '08b')


def signed_value(binary):
    value = int(binary, 2)

    if value >= 128:
        value -= 256

    return value


def perform_operation(a, b, operation):
    bin_a = to_8bit(a)
    bin_b = to_8bit(b)

    if operation == '+':
        result = a + b
        binary_result = (int(bin_a, 2) + int(bin_b, 2)) & 0xFF

    elif operation == '-':
        result = a - b
        binary_result = (int(bin_a, 2) - int(bin_b, 2)) & 0xFF

    binary_result = format(binary_result, '08b')

    overflow = not (-128 <= result <= 127)

    print("\nExpression:", a, operation, b)
    print("First operand :", bin_a)
    print("Second operand:", bin_b)
    print("Result in binary:", binary_result)
    print("Result in decimal:", signed_value(binary_result))
    print("Arithmetic overflow:", "Yes" if overflow else "No")


# (a) +46 + (+29)
perform_operation(46, 29, '+')

# (b) (-48) - (-23)
perform_operation(-48, -23, '-')