# Write the pseudocode & a program to calculate the simple interest
# based on the inputs(amount, rate, time) provided by the user.

# pseudocode
# Step 1. Take input for amount.
# Step 2. Take input for rate.
# Step 3. Take input for time.
# Step 4. calculate interest as per formula and assign it to new variable (let say Interest)
# Step 5. print variable Interest.

# Implementation

amount = int(input('Please Enter Amount : '))
rate = int(input('Please Enter Rate : '))
time = int(input('Please Enter time : '))
interest = (amount * rate * time) / 100
print(f'Simple Interest is {interest}')

