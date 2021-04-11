import random
print("Try to immagine a number, and computer will try to guess it, and you have to give computer some advices via input")
def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"Is {guess} too high 'H', too low 'L', or correct 'C'?: ").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
        
    print(f"Yey you guessed {guess}, that was actually my number! ")

n = int(input("Number: "))
computer_guess(n)