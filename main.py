# Get user name
userName = input("What is your name? ")

# ensure that user can only pick 3 or 6 holes
numHoles = 0
isValidHoles = False
while isValidHoles == False:
    if numHoles != 0:
        print(f"{numHoles} is not a valid number, this course only has options for 3 or 6 holes.")
    numHoles = int(input("would you like to play 3 holes, or 6 holes (3 or 6)? "))
    if numHoles == 3 or numHoles == 6:
        isValidHoles = True

# par is 3 for each hole
par = numHoles * 3

# ask user for strokes taken on each hole
numPutts = 0
i=1
while i <= numHoles:
    numPutts += int(input(f"How mny putts did you need for hole {i}? "))
    i+=1

if numPutts > par:
    print(f"Nice try, {userName}... your total score was: +{numPutts - par}.")
elif numPutts < par:
    print(f"Great Job, {userName}! Your total score was -{par - numPutts}.")
else:
    print(f"Good game, {userName}.  Your total score was: 0.")