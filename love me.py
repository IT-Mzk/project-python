print("Welcome to my quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play =))) ")
score = 0

answer = input("Do you love me? ")
if answer.lower() == "yes":
    print('cute <3')
    score += 1
else:
    print("answer again ^^ ")

answer = input("Love me or not? =)) (yes/no) ")
if answer.lower() == "yes":
    print('I love you too, bae <3')
    score += 1
else:
    print("what =)) ")

answer = input("Will u marry me? (yes/no) ")
if answer.lower() == "yes":
    print('omg I love you so much <3')
    score += 1
else:
    print("you must love me =))) ")


#print("You got " + str(score) + " questions correct!")
