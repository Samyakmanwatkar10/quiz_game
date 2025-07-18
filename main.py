print("Welcome to my quiz game!")

playing=input("Do you want to play? (yes/no): ")

if playing.lower()!= "yes":
    quit()
    
print("Great! Let's get started.")
score=0

answer=input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is 'Central Processing Unit'.")

answer=input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is 'Graphics Processing Unit'.")

answer=input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is 'random access memory'.")

answer=input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is 'power supply unit'.")

print(f"your score is {score} out of 4")
print(f"You got {score/4 * 100}% correct.")