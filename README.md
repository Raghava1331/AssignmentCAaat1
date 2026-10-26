# COMPUTER ARCHITECTURE
Assignment aat1
**NAME:** Raghava 
**USN:** 1NH25AI114-T
This repository contains Python programs developed for two Computer Architecture assignment questions.

Signed binary arithmetic using 8-bit 2's complement representation.
Rotate Right (ROR) and Rotate Right through Carry (RCR) operations on an 8-bit binary number.
The programs display intermediate steps and final results to verify the output against manual binary calculations.
question1_signed_arithmetic.py: Performs signed binary addition and subtraction using 8-bit 2's complement representation and checks for arithmetic overflow.

question2_rotate_operations.py: Performs ROR and RCR operations on an 8-bit binary number by three positions, displaying each intermediate step and carry flag.

output.txt: Contains the output obtained by executing both Python programs.

README.md: Provides project information, execution instructions, and verified results.

Requirements
Python 3
No additional libraries are required.
How to Execute
Question 1: Signed Binary Arithmetic
Run the following command in the terminal:

python question1_signed_arithmetic.py

The program evaluates the following expressions:

+46 + (+29)
(-48) - (-23)
It displays the operands in 8-bit 2's complement binary format, performs the arithmetic operations, and displays the final results in binary and decimal formats. It also checks for arithmetic overflow.

Question 2: Rotate Operations
Run the following command in the terminal:

python question2_rotate_operations.py

The program performs the following operations on the binary number 11010101:

Rotate Right (ROR) by three positions.
Rotate Right through Carry (RCR) by three positions.
It displays the original binary number, demonstrates the rotation process step by step, and displays the final binary result. For RCR, the initial carry flag is assumed to be 0, and both the initial and final carry values are displayed.

Note: On some Windows systems, use py instead of python if the Python command is unavailable.

Verified Results
Question 1: Signed Binary Arithmetic
Expression 1: +46 + (+29)

Binary result: 01001011

Decimal result: 75

Arithmetic overflow: No

Expression 2: (-48) - (-23)

Binary result: 11100111

Decimal result: -25

Arithmetic overflow: No

The signed 8-bit 2's complement range is -128 to +127. Both results are within this range.

Question 2: Rotate Operations
ROR by three positions

Original binary number: 11010101

Final binary result: 10111010

RCR by three positions

Original binary number: 11010101

Initial carry flag: 0

Final binary result: 01011010

Final carry flag: 1

Concepts Demonstrated
8-bit binary representation
Signed integers using 2's complement
Binary addition and subtraction
Arithmetic overflow detection
Rotate Right (ROR)
Rotate Right through Carry (RCR)
Carry flag handling
Python programming for Computer Architecture
Verification
The program outputs were checked against manual binary calculations. Both programs can be executed in a Python environment to reproduce the results.

The output.txt file contains the captured output of both programs for verification.
