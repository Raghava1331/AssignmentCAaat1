number = "11010101"
n = 3

print("Original 8-bit number:", number)

ror = number

print("\n(a) Rotate Right without Carry (ROR)")
print("Original:", ror)

for i in range(n):
    ror = ror[-1] + ror[:-1]
    print("Step", i + 1, ":", ror)

print("Final ROR result:", ror)


rcr = number
carry = 0

print("\n(b) Rotate Right through Carry (RCR)")
print("Initial number:", rcr)
print("Initial carry:", carry)

for i in range(n):
    new_carry = int(rcr[-1])
    rcr = str(carry) + rcr[:-1]
    carry = new_carry

    print("Step", i + 1, ":", rcr, "| Carry:", carry)

print("Final RCR result:", rcr)
print("Final carry:", carry)