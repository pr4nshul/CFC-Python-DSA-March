# Write the pseudocode & the program to calculate GCD of two numbers

# pseudocode
# Step 1. Take input for first operand (let say A).
# Step 2. Take input for second operand (let say B).
# Step 3. calculate GCD by looping over B till B is not 0.
# Step 4. calculate mod of a and b and assign it to b and assign earlier value of B to A and go back to step 3
# Step 4. print value of A.

# Implementation

x = int(input('Enter first operand : '))
y = int(input('Enter second operand : '))
a, b = x, y
c = 1

while b:
    temp = a % b
    a, b = b, temp
print(f'GCD of {x} and {y} is {a}')
