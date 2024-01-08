print("Welcome to today Quiz!") 

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = int(input("what is the sum of 8 + 8? "))
if answer==16:
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Who is the CM of Andhra Pradesh in 2023? ")
if answer.lower() == "jagan mohan reddy" or "mohan reddy" or "jagan":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("what is DBMS stands for? ")
if answer.lower() == "database management system":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What is the nearest planet to earth? ")
if answer.lower() == "mercury":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
answer = input('what is the most ornament in cosmetics category? ')
if answer.lower() == "eye cosmetics":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")
