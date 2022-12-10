
##Integration project
##Ben Aboulhosn
##9/21
global lives
lives = 3
def yourWrong(lives):
    print("Wrong.. That's unfortunate you now lose a life")
    lives = lives - 1
    print("You have", lives, " Lives Remaining.")
    return(lives)
#i got really stuck on being able to return this value it always goes back to three even though im returning it.
print(lives)
    # this is used to count how many questions the user gets wrong

print("This is the 'Are You Smarter Than A Stressed Out College Student Quiz'", end='.')
# end= added a period to the end of the print statement

print("--------" * 10)
# * is used for the string to repeat it 10 times
# only for looks^)

print("There are 10 questions in this quiz")
print("For every question you answer wrong you lose a life")
print("You start with 3 lives, if you still have lives remaining you will win an award.")

print("Most of these questions will be math related(Please type out the whole answer)")
test1 = False
#the while not in this next line is used to make make sure that the user provides the correct
# input it tests whether a integer has been passed and if it hasn't it sends an error message

while not test1:
    try:
        Question_1_Addition = int(input("What is 9+10," + "\n is it, \n A.21 \n B.18 \n C.19 \n D.20 "))
        test1 = True
    except:
        print("Invalid input, Please type the actual number")
# int is used to turn the number the user puts in from a string to a integer

# \n is used to create a line seperation for the different answer

if Question_1_Addition == 9 + 10:
    # + in this if statement is used as addition
    print("Congrats!, You are correct.")
else:
    yourWrong(lives)
print("There goes question 1. easy right")

print(lives)

Question_2_Logic = input(
            "If im facing right and i turn 270 degrees to the right then another 90 to the left, which way am I facing"
            " now \n A. forward \n B. back \n C. right \n D. left")



# if statements are used to make sure the user gets the question right.
#or operator allows the user to input the Letter or the written out answer
if Question_2_Logic == "left":

    print("Congrats!, You are correct.")
else:
    lives = yourWrong(lives)
print("There goes question 2. feelin dumb yet")

while test1 != False:
    #try is used to make sure make sure that the program doesnt just close when a invalid input is entered
    try:
        Question_3_Integers = int(input("What is 6 cubed \n A.216 \n B. 164 \n C.320 \n D. 232."))
        test1 = False
    except:
        print("invalid input")
# ** is a integer(integer as in x^n) function(makes 6 to the power of 3)

if Question_3_Integers == 6 ** 3:

    print("Congrats!, You are correct.")
else:
    lives = yourWrong(lives)
print("There goes question 3. Getting a little challenge eh.")

while not test1:
    try:
        Question_4_Subtraction = float(input("What is 1092.50 - 740.25?"
                                             " \n A. 400.25 \n B. 342.25 \n C. 310.25 \n D.352.25"))
        test1 = True
    except:
        print("invalid input")

# - is used for subtraction

if Question_4_Subtraction == 1092.50 - 740.25:
    print("Congrats!, You are correct.")
else:
   lives = yourWrong(lives)
print("There goes question 4. This was a freebie!!.")

# and statement doesnt really have any purpose in here, it just sees that the previous test was true and runs continues
test2 = True
while test1 and test2:
    try:
        Question_5_Multiplication = int(input("What is 32 * 7 \n A. 214 \n B.224 \n C. 234 \n D.244"))
        test1 = False
    except:
        print("invalid input")

# * is used for multiplication

if Question_5_Multiplication == 32 * 7:

    print("Congrats!, You are correct.")
else:
  lives = yourWrong(lives)
print("There goes question 5. Hope u didn't have to bring out the calculator.")
while not test1:
    try:
        Question_6_Division = int(input("What is 108 / 4 \n A. 29 \n B. 27 \n C. 28 \n D.26"))
        test1 = True
    except:
        print("invalid input")

# / is used for division

if Question_6_Division == 108 / 4:

    print("Congrats!, You are correct.")
else:
   lives = yourWrong(lives)
print("There goes question 6. Easy right... so close to that amazing reward.")

while test1:
    try:
        Question_7_Floor_Division = int(input("If there are are 198 slices of pizza and there are 8 slices in a pizza,"
                                              " How many pizzas are there? \n A.24 \n B.19 \n C.26 \n D.20"))
        test1 = False
    except:
        print("Invalid Input")

if Question_7_Floor_Division == 198 // 8:

    print("Congrats!, You are correct.")
else:
   lives = yourWrong(lives)
print("There goes question 7. A little tricky.")

while not test1:
    try:
        Question_8_Remainder = int(input("What is the remainder of slices in the previous question?"
                                         " \n A. 2 \n B. 4 \n C. 6 \n D. 0"))
        test1 = True
    except:
        print("invalid input")

# % gives me the remainder

if Question_8_Remainder == 198 % 8:

    print("Congrats!, You are correct.")
else:
   lives = yourWrong(lives)

try:
    Question_9_Fill = int(input("you have done so well heres a freebie, whats 1+1"))
except:
    Question_9_Fill = input("How do you mess that up the answer is 2 type the number '2'")

if Question_9_Fill == 2:

    print("Congrats!, You are correct.")
else:
   lives = yourWrong(lives)
print("There goes question 9. Your welcome. Last question now, You ready....")
while test1:
    try:
        Question_10_Me = int(input(
    "What is me the creator of this quizzes favorite number "
    "\n careful now this is worth 3 lives \n also no answer choices(dont look at the code)"))
        test1 = False
    except:
        print("invalid input")
if Question_10_Me == 36:

    print("Congrats!, You are correct.")
else:
    print("Wrong.. Thats unfortunate you now lose a life")
    lives = lives - 3
    print("You have", lives, " Lives Remaining.")
print("There goes question 10. Do you have any lives remaining??.")
#> function is used to check if the person won the game by seeing if they have more than 0 lives therefore at least having 1.
if lives > 0:
# for in range just repeats the print statement 5 times
    for index in range(5):
        print("You have won 1 million dollars!!!!!!!!!!!!" * 10)
else:
    print("That's unfortunate, you could have won the reward of 1 million dollars")
print("Thank you for taking the test and goodbye")
#im not sure what to add for the final project but i mainly just fixed up typos
