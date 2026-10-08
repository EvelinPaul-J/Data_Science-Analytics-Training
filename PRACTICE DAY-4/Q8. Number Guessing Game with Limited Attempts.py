secret = 8
for i in range(5):
    guess = int(input("guess the numbr:"))
    if guess == secret:
        print("Correct")
        break
    elif guess < secret:
        print("Too Low")
    else:
        print("Too High")
else:
    print("Game Over")