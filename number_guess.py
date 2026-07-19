import random
player = {}
player["name"] = input("enter your name: ")
while True:
    try:
        player["age"]=int(input("enter your age: "))
        break
    except ValueError:
        print("Please enter an integer only!")
        
levels = ("Easy", "Medium", "Hard")
print("\nChoose Difficulty")
print("1. Easy")
print("2. Medium")
print("3. Hard")
choice = input("Enter your choice (1-3): ")

if choice == "1":
    number_range = 10
    attempts = 5
elif choice == "2":
    number_range = 20
    attempts = 4
elif choice == "3":
    number_range = 30
    attempts = 3
else:
    print("Invalid choice! Easy mode selected.")
    number_range = 10
    attempts = 5

while True:
    guess = []        #list
    number = random.randint(1, number_range)
    for i in range(attempts):
        print(f"\nAttempt {i+1} of {attempts}")
        try:
            g = int(input(f"Enter your guess between 1 and {number_range}: "))
        except ValueError:
            print("Please enter an integer only!")
            continue
        guess.append(g)
    
        if g == number:
            print("Correct!")
            break
        elif g > number:
            if g - number <= 2:
                print("Near High")
            else:
                print("Too High")
        else: 
            if number - g <= 2:
                print("Near Low")
            else:
                print("Too Low")

    print("your guess: ", guess)
    def check_guess(g, number):
        if g == number:
            print("You Win!")
        else:
            print("wrong guess")
    
    check_guess(g,number)
    choice = input("\nDo you want to play again? (y/n): ")
    if choice.lower() != "y":
        print("Thanks for playing!")
        break
    