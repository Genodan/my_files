something = 0
spese1 = []
while something != 10:
    something += 1
    spese = eval(input(f"QUanti soldi hai speso il giorno {something}? "))
    if spese < 0:
        print("non possono guadagnare i soldi i studenti, genio")
        exit()
    spese1.append(spese)
media = sum(spese1) / len(spese1)
if media > 50:
    print(media)
    print("I studenti hanno speso tanti soldi, più di 50, male")
elif media == 50:
    print(media)
    print("I studenti hanno speso esattamente 50, non male")
else:
    print(media)
    print("Hanno speso meno di 50 euro")




