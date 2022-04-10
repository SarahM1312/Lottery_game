#Lottery

#Amount of money that can be won for number of winning matches
money_win = {3:20,
             4:40,
             5:100,
             6:10000,
             7:1000000,}

#Welcome message
print("Welcome to the Lotto! \n"
      "If you have 3 matching numbers you will win £{}\n"
      "If you have 4 matching numbers you will win £{} \n"
      "If you have 5 matching numbers you will win £{}\n"
      "If you have 6 matching numbers you will win £{} \n"
      "If you have 7 matching numbers you will win £{} \n".format(money_win[3],money_win[4],money_win[5],money_win[6],money_win[7]))

#user name
name = input("What is your name?")

#User to choose 7 numbers
user_numbers = []
for x in range(7):
    your_numbers = int(input("Please select a number from 1-40?"))
    user_numbers.append(your_numbers)

# To check the below uncomment code
#print(user_numbers)

#Randomly choosing the lottery numbers

import random

list_winning_numbers = []
for x in range(7):
    winning_numbers = (random.randint(1, 40))
    list_winning_numbers.append(winning_numbers)

# To check the below uncomment the below
#print(list_winning_numbers)

#Determine how many winning numbers there are

matching_numbers = 0

for user_num in user_numbers:
    for list_winning_num in list_winning_numbers:
        if list_winning_num == user_num:
            matching_numbers = matching_numbers + 1

# To check uncomment the below
#print(matching_numbers)

#Telling the user the outcome:

if matching_numbers == 3:
    print("Congratulation {}, you have 3 matches - you have won £{}\n "
          "The winning numbers were {} The numbers you selected were {}".format(name,money_win[3],list_winning_numbers,user_numbers))
elif matching_numbers == 4:
    print("Congratulation {}, you have 4 matches - you have won £{}\n "
          "The winning numbers were {} The numbers you selected were {}".format(name,money_win[4],list_winning_numbers,user_numbers))
elif matching_numbers == 5:
    print("Congratulations {}, you have 5 winning matches - you have won £{}\n "
          "The winning numbers were {} The numbers you selected were {}".format(name,money_win[5],list_winning_numbers,user_numbers))
elif matching_numbers ==6:
    print("Congratulations {}, you have 6 winning matches - you have won £{} \n"
          " The winning numbers were {} The numbers you selected were {}".format(name,money_win[6],list_winning_numbers,user_numbers))
elif matching_numbers == 7:
    print("WINNER ALERT!!! {}, you have 7 winning matches - you have won £{} \n "
          "The winning numbers were {} The numbers you selected were {}".format(name,money_win[7],list_winning_numbers,user_numbers))
elif matching_numbers == 0:
    print("Better luck next time you don't have any winning matches\n "
          "The winning numbers were {} The numbers you selected were {}".format(list_winning_numbers,user_numbers))
else:
    print("You have {} matches but have not won any money - try again \n "
          "The winning numbers were {} Your numbers were {}".format(matching_numbers,list_winning_numbers,user_numbers))
