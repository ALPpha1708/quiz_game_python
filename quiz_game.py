print("Welcome to my Computer Quiz!")

playing = input("do u wanna play? ")

if playing.lower() != "yes":
    quit()

print("Okay! let's play")
score = 0

answer = input("7+1=")

if answer.lower() == "8":
    print("Correct")
    score+=1
else:
    print("Incorrect")
    
answer = input("9+2=")

if answer.lower() == "11":
    print("Correct")
    score+=1
else:
    print("Incorrect")
    
answer = input("15/3=")

if answer.lower() == "5":
    print("Correct")
    score+=1
else:
    print("Incorrect")
    
answer = input("5*5=")

if answer.lower() == "25":
    print("Correct")
    score+=1
else:
    print("Incorrect")
    
print("You got "+str(score)+" questions correct")