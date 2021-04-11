import string

hellow = "Hellow".upper()
alphabet = set("Hellow".upper())
full_alphabet = set(string.ascii_uppercase)
already_used = set()
while len(alphabet) > 0:
    ele = [used if used in already_used else "-" for used in hellow]
    not_used = ["-" if used in already_used else used for used in full_alphabet]
    print("Guess this: "," " .join(ele))
    guess = input("Input: ").upper()
    if guess in full_alphabet - already_used:
        already_used.add(guess)
        if guess in alphabet:
            alphabet.remove(guess)
            print("")
    elif guess in already_used:
        print()
        print("You already used this letter, the letters you haven't used yet are: "," ".join(not_used))

print(f"Yey, you guessed a word {hellow}")







        

    