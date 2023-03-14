print("Welcome to the Quiz!")

playing = input("Do you want to play? ")
print(playing)

if playing.lower() != "yes":
    quit()

print("Okay Let's play :) ")

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
else:
    print("Incorrect!")

answer = input("What does USB stand for? ")
if answer.lower() == "universal serial bus":
    print("Correct!")
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
else:
    print("Incorrect!")

answer = input("What does ATM stand for? ")
if answer.lower() == "automated teller machine":
    print("Correct!")
else:
    print("Incorrect!")


