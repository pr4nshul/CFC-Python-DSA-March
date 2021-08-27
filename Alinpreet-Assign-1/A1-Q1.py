# QUESTION 1: Write the pseudocode & a program to input credits of a Code for Cause Campus leader and
# then output the badge of the lead on the basis of the following criteria:
# a. 7500 <= credits : Tera leader
# b. 6000 <= credits < 7500 : Gega leader
# c. 4500 <= credits < 6000 : Mega leader
# d. Credits < 4500 : Rising Star

# PseudoCode :
# Step 1. Take Credit Input from User
# Step 2. Check if Credit is greater than equal to 7500, if yes , Print 'Tera Leader' otherwise pass to step 3.
# Step 3. Check if Credit is greater than equal to 6000, if yes , Print 'Gega Leader' otherwise pass to step 4.
# Step 4. Check if Credit is greater than equal to 4500, if yes , Print 'Mega Leader' otherwise pass to step 5.
# Step 5. Check if Credit is less 4500, if yes , Print 'Rising Star'.

# Implementation

leader_credits = int(input('Enter credits here : '))  # Step 1

if leader_credits >= 7500:  # Step 2
    print('Tera leader')
elif leader_credits >= 6000:  # Step 3
    print('Gega leader')
elif leader_credits >= 4500:  # Step 4
    print('Mega leader')
else:  # Step 5
    print('Rising Star')
