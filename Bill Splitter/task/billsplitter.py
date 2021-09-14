# Stage 4/4: Party is over
# Description

# It's the right time to update your dictionary with new split
# values to make our "Who is lucky?" feature better. First, we
# need to recalculate the split value for everyone. Make sure
# that our lucky one pays 0.

# Recalculate the split value for n-1 people where n is the
# total length of the dictionary and update the values in the
# dictionary with the new split value for everyone.

# If a user decides not to use the "Who is lucky" feature, print
# the original dictionary.

# Objectives

# In this stage your program should perform the following
# steps together with the steps from the previous stages:
# 1. In case of an invalid number of people, "No one is
#    joining for the party" is expected as an
#    output.
# 2. Otherwise, if the user choice is Yes, re-split the bill
#    according to the feature;
# 3. Round the splti value to two decimal places;
# 4. Update the dictionary with new split values and 0
#    for the lucky person;
# 5. Print the updated dictionary;
# 6. If the user entered anything else instead of Yes,
#    print the original dictionary.

# Examples
# The greater-than symbol followed by a space ( > )
# represents the user input. Note that it's not part of the input.

# Example 1: The feature is used

# Enter the number of friends joining (including
# you):
# > 5

# Enter the name of every friend (including you),
# each on a new line:
# > Marc
# > Jem
# > Monica
# > Anna
# > Jason

# Enter the total bill value:
# > 100

# Do you want to use the "Who is lucky?" feature? Write Yes/No:
# > Yes

# > Jem is the lukcy one!

# {'Marc': 25, 'Jem': 0, 'Monica': 25, 'Anna': 25,
# 'Jason': 25}

# Example 2: The feature is skipped

# Enter the number of friends joining (including
# you):
# > 5

# Enter the name of every friend (including you),
# each on a new line:
# > Marc
# > Jem
# > Monica
# > Anna
# > Jason

# Enter the total bill value:
# > 100

# Do you want to use the "Who is lucky?" feature? Write Yes/No:
# > No

# No one is going to be lucky

# {'Marc': 20, 'Jem': 20, 'Monica': 20, 'Anna': 20,
# 'Jason': 20}

# Example 3: Invalid input

# Enter the number of friends joining (including
# you):
# > 0

# No one is joining for the party

import random

class BillSplitter:
    def __init__(self):
        self.n = None
        self.friends = {}
        self.bill = None

    def take_friends(self):
        print('Enter the number of friends joining (including you):')
        try:
            self.n = int(input())
            assert self.n > 0
        except AssertionError:
            print("No one is joining for the party")
        else:
            print("Enter the name of every friend (including you), each on a new line:")
            [self.friends.update({input(): 0}) for _ in range(self.n)]
            print("Enter the total bill value:")
            self.bill = int(input())
            print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
            answer = input()
            lucky = random.choice([_ for _ in self.friends])
            if answer == 'Yes':
                print(lucky + " is the lucky one!")
                each_bill = round(self.bill / (self.n - 1), 2) if (self.bill / (self.n - 1)) % 1 != 0 else round(self.bill / (self.n - 1))
                for f in self.friends:
                    self.friends[f] = each_bill
                self.friends[lucky] = 0
            else:
                print("No one is going to be lucky")
                each_bill = round(self.bill / self.n, 2) if (self.bill / self.n) % 1 != 0 else round(self.bill / self.n)
                for f in self.friends:
                    self.friends[f] = each_bill
            print(self.friends)


def main():
    bill_splitter = BillSplitter()
    bill_splitter.take_friends()


if __name__ == '__main__':
    main()