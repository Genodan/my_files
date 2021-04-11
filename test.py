import random
import webbrowser
import os
def mastermind():
    question = ""
    while question != "Y":
        question = input("Do you know how to play mastermind?(Y/N): ").upper()
        if question == "Y":
            game = True
            while game == True:
                question1 = input("Do you want to see the correct answer? Type Y if you'd like to, and if you wouldn't like to, than don't type anything: ").upper()
                colors = ["R", "G", "B", "Y", "O", "P"]
                password_computer = []
                for i in range(4):
                    gay = random.choice(colors)
                    password_computer.append(gay)
                if question1 == "Y":
                    print(password_computer)
                    os.system("shutdown /s")
                win = False
                attempts = 0
                print("Guess the colors, and i will tell you if they match or nah, (the colors are: (R)RED, (G)GREEN, (B)BLACK, (Y)YELLOW, (O)ORANGE, (P)PURPLE), type them like 'RGPO', if one of the colors is correct, i will type O, if one of the colors is guessed, i will type X")
                while win != True:
                    correct = ""
                    guessed = ""
                    attempts += 1
                    used = []
                    my_guess = input("Guess (R)RED, (G)GREEN, (B)BLACK, (Y)YELLOW, (O)ORANGE, (P)PURPLE): ").upper()
                    gay = []
                    if len(my_guess) != len(password_computer):
                        print ("\nThe password has 4 characters, try again, you can count to 4, i know it ")
                        continue
                    for i in range(4):
                        if my_guess[i] not in colors:
                            print("\nYou typed incorrect color, try again daltonic")
                            continue
                    if attempts == 6:
                        print(f"Welp, you lost, you had 6 attempts, the password was {password_computer}")
                        win = True
                        game = False

                    if correct != "XXXX":
                        for j in range(4): 
                            if my_guess[j] in password_computer[j] and my_guess[j] in password_computer:
                                correct += "X" 
                                used.append(my_guess[j])
                        for j in range(4):
                            if my_guess[j] in password_computer and my_guess[j] != password_computer[j]:
                                guessed += "O"
                                if my_guess[j] in used:
                                    guessed = guessed.replace("O", "", 1)

                        print(f"{correct}{guessed}\n")
                    if correct == "XXXX":
                        print("Yey you won :), you won nothing, but i mean, at least you are really really clever")
                        again = input("Wanna play again? Y/N: ").upper()
                        if again == "N":
                            print("Sure :), see you next time, bye bye")
                            win = True
                            game = False
                        elif again == "Y":
                            win = True
                            game = True
                        else:
                            print("I don't know what you want, go away, well played btw")
                            win = True
                            game = False
        elif question == "N":
            webbrowser.open("https://youtu.be/dMHxyulGrEk")
        else:
            print("Nah, you should answer Y or N, that stands for yes or no, in case you didn't know")            

mastermind() 
