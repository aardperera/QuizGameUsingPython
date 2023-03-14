print("Welcome to the Quiz!")

playing = input("Do you want to play? ")
print(playing)

if playing != "yes":
    quit()

print("Okay Let's play :) ")

answer = input("What does CPU stand for? ")
if answer == "Central Processing Unit":
    print("Correct!")
else:
    print("Incorrect!")

answer = input("What does USB stand for? ")
if answer == "Universal Serial Bus":
    print("Correct!")
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer == "Random Access Memory":
    print("Correct!")
else:
    print("Incorrect!")

answer = input("What does ATM stand for? ")
if answer == "Automated Teller Machine":
    print("Correct!")
else:
    print("Incorrect!")
    
answer = input("What does GPU stand for? ")
if answer == "Graphic Processing Unit":
    print("Correct!")
else:
    print("Incorrect!")
    
answer = input("What does BIOS stand for? ")
if answer == "Basic Input Output System":
    print("Correct!")
else:
    print("Incorrect!")


