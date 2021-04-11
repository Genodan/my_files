#SCRIVERE UNA STRINGA IN MODO ORDINATO
#print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")

#CONTROLLARE LA VERSIONE DEL PYTHON CHE USO 
#import sys
#print(sys.version)
#print(sys.version_info)

#MI DICE IL TEMPO REALE
#from datetime import datetime
#now = datetime.now()
#time = now.strftime("%d:%m:%Y %H:%M:%S")
#print(f"Current time is: {time}")

#CALCOLARE L'AREA DELLO CERCHIO
#import math
#r = eval(input("Radius: "))
#pi = math.pi
#A = r**2 * pi
#print(A)

#INSERISCI NOME E COGNOME
#name = input("name: ")
#surname = input("surname: ")
#print(f"{surname} {name}")

#NUMERI E LA FUNZIONE TUPLE
#numbers = input("Input comma divided numbers: ")
#lista = numbers.split(",")
#tuple = tuple(lista)
#print(lista)
#print(tuple)

#MI DICE ESTENSIONE DEL FILE CHE IO SCRIVO
#file = input("Insert format of file 'es. kkl.mp3': ")
#separate = file.split(".")
#aya = repr(separate[-1])
#print(aya)

#UUUH,SUPPONGO LISTA SEMPLICE 
#color_list = ["Red","Green","White" ,"Black"]
#print(color_list[0], color_list[-1])

#EXAMINATIONA SCHEDULE, MAI CAPITO MAI LO FARO'
#smh = (25,3,2021)
#print("Examination schedule will start from: %i / %i / %i"%smh)

#UTILE PER CAPIRE LA FUNZIONALITA DI %S
#n = eval(input("1 number: "))
#n1 = int("%s"%(n))
#n2 = int("%s%s"%(n,n))
#n3 = int("%s%s%s"%(n,n,n))
#print(n1+n2+n3)

#?????????????????????????????????????????????????????????????
#print(abs.__doc__)

#MI FA VEDERE IL CALENDARIO DEL MESE E ANNO INDICATO
#import calendar
#y = input("anno: ")
#m = input("mese: ")
#print(calendar.month(y,m))

#UN CODICE FACILE DEL PRINT NORMALE
#print("""
#a string that you "don't" have to escape
#This
#is a ....... multi-line
#heredoc string --------> example
#""")

#INDICANDO 2 DATI MI DICE QUANTI GIORNI MANCANO PER LA DATA
#import datetime
#dat = input("date in format YYYY-MM-DD: ")
#year1, month1, day1 = map(int,dat.split("-"))
#date1 = datetime.date(year1,month1,day1)
#daty = input("second date in format YYYY-MM-DD: ")
#year2,month2,day2 = map(int,daty.split("-")) 
#date2 = datetime.date(year2,month2,day2)
#delta = date2 - date1
#print(delta.days)

#CALCOLARE AREA DELLA SFERA
#import math
#r = eval(input("Input a radius of a shpere: "))
#pi = math.pi
#V = 4/3 * pi * r**3
#print(V)

#DIFFERENZA ASSOLUTA TRA I NUMERI
#def difference(n):
#    if n =< 17:
#        return 17 - n
#    elif n > 17:
#        return (n-17)*2
#print(difference(8))
#print(difference(22))

#CALCOLA SE IL NUMERO DATO E VICINO DI 100 A 1000 OPPURE 2000
#def near_thousand(n):
#    if (abs(1000 - n) <= 100 or abs(2000 - n) <= 100):
#        return print(True)
#    else:
#        return print(False)
#near_thousand(1000)
#near_thousand(1100)
#near_thousand(1200)
#near_thousand(2100)
#near_thousand(1900)
#near_thousand(2200)

#SOMMA DEI 3 NUMERI, E SE SONO UGUALI SI MOLTIPLICA LA SOMMA PER 3
#def sum_numbahs(x,z,y):
#    sum = x + y + z

#    if x == y == z:
#        sum *= 3

#    return print(sum)

#sum_numbahs(1,1,1)

#CONTROLLA SE AL INIZIO DELLA STRINGA DATA C'E' "IS", NEL CASO SE C'E ALLORA SCRIVE STRINGA SENZA MODIFICARLA, E SE NON C'E ALLORA LA AGGIUNGE
#def new_string(str):
#    if len(str) >= 2 and str[:2] == "Is":
#        return str
#    return "Is" + str
#print(new_string("IsEmpty"))
#print(new_string("Array"))

#COPIA LA STRINGA DATA PER LE VOLTE CHE INDICO
#def copies(str, n):
#    result = ""
#    for i in range(n):
#        result = result + str
#    return result

#print(copies("Fabien", 10))

#SE IL NUMERO DELL'UTENTE è PARI O DISPARI
#def even_odd(n):
#    if n % 2 == 0:
#        return "Even"
#    else:
#        return "Odd"

#n = eval(input("Input a number: "))
#print(even_odd(n))

#INSERISCI I NUMERI E TI DICE QUANTE VOLTE HAI INSERITO 4 
#def count(r):
#    count = 0
#    for i in range(r):
#        num = eval(input("Input a number: "))
#        if num == 4:
#            count += 1
#    return count

#print(count(5))

#CHIEDE DI INSERIRE UNA STRINGA E INSERIRE UN NUMERO, E MOLTIPLICA PRIMI 2 SEGNI DELLA STRINGA PER IL NUMERO DATO, INVECE SE è TROPPO PICCOLA LA STRINGA, TI COPIA LA STRINGA PER LA QUANTITA DEL NUMERO DATO 
#def substring_copie(str, n):
#    result = ""
#    if len(str) < 2:
#        for j in range(n):
#            result = result + str
#    else:
#        for j in range(n):
#            characters = str[:2]
#            result = result + characters 
#    return result

#print(substring_copie("abcdef", 2))
#print(substring_copie("p", 3))

#MI DICE SE LA LETTERA INSERITA è UNA VOCALE OPPURE NO
#def vowel(char):
#    vow = "aeiou"
#    return char in vow

#print(vowel("o"))
#print(vowel("c"))
    
#CONROLLO SE IL NUMERO INDICATO è PRESENTE NELLA LISTA DEI NUMERI
#def numbercheeck(data, n):
#    if n in data:
#        return True
#    return False
#print(numbercheeck([1,3,5,8], 1))
#print(numbercheeck([1,3,8,5], 123))

#CREARE UN ISTOGRAMMA CON I NUMERI DATI 
#def histogram(items):
#    for n in items:
#        result = ""
#        times = n
#        while times > 0:
#            result += "*"
#            times -= 1
#        print(result)
#histogram([1,2,4,3])

#CONCATENARE LISTA IN STRINGA
#def contatenate(lista):
#    result = ""
#    for ele in lista:
#        result += str(ele)
#    return result
#print(contatenate([1,5,7,32]))

#CONTROLLO DI NUMERI NELLA LISTA E ETC. LUNGA STORIA
#numbers = [    
#    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
#    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
#    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
#    958,743, 527
#    ]
#for ele in numbers:
#    if ele % 2 == 0:
#        print(ele)
#    if ele == 237:
#        print(ele)
#        break

#PRINT DELLA LISTA1 DEI DATI CHE NON SONO PRESENTI IN LISTA 2 
#color_list_1 = set(["White", "Black", "Red"])
#color_list_2 = set(["Red", "Green"])
#print(color_list_1.difference(color_list_2))

#AREA DEL TRIANGOLO
#def volume(b,h):
#    A = (b * h)/2
#    return A
#print(volume(20,40))

#MASSIMO COMUNE DIVISORE
#def gcd(x, y):
#    gcd = 1
#    if x % y == 0:
#        return y
#    for k in range(int(y / 2), 0, -1):
#        if x % k == 0 and y % k == 0:
#            gcd = k
#            break
#    return gcd
#print(gcd(12,16))

#MINIMO COMUNE DIVISORE
#def lcd(x, y):
#    if x > y:
#        z = x
#    else:
#        z = y
#    while True:
#        if z % x == 0 and z % y == 0:
#            lcd = z
#            break
#        z += 1
#    return z
#print(lcd(4,6))

#SUMMA DEI NUMERI MA SE CI SONO 2 NUMERI UGUALI ALLORA LA SOMMA è 0
#def sum(x,y,z):
#    sum = x + y + z
#    if x == y or x == z or z == x:
#        sum = 0
#    return sum
#print(sum(1,2,3))
#print(sum(23,23,23))

#LA SOMMA DEI 2 NUMERI, PERò SE LA SOMMA SI TROVA DA 15 A 20, ALLORA MI SCRIVE 20
#def sum(x,y):
#    sum = x + y
#    if sum in range(15,20):
#        return 20
#    return sum
#print(sum(12,24))
#print(sum(12,6))

#SCRIVO 2 NUMERI, MA SE I NUMERI SONO UGUALI, OPPURE LA LORO SOMMA O DIFFERENZA è UGUALE A 5 ALLORA MI RITORNA TRUE
#def sum(x,y):
#    sum = x + y
#    if x == y or abs(x - y == 5) or x + y == 5:
#        return True
#    else:
#        return False
#print(sum(7,2))
#print(sum(3,2))
#print(sum(2,2))

#SOMMA I NUMERI DATI SE TUTTI E DUE SONO INTEGERS
#def add_numbers(x,y):
#    if not isinstance(x, int) or not isinstance(y, int):
#        raise TypeError("Inputs must be integers")
#    return x + y
#print(add_numbers(10,20))
#print(add_numbers("a",20))

#MY PERSONAL INFORMATION I GUESS
#def personal_info():
#    name, age = "Bogdan", 15
#    address = "Via Aldo Manuzio 19/2, Genova, Italia"
#    print(f"Name: {name}\nAge: {age} \nAddress: {address}")
#personal_info()

#RISOLVERE UN DOPPIO QUADRATO VABBE FANCULO MATEMATICA VECCHIA
#print("(x + y) * (x + y)")
#print("x = 4, y = 3")
#x,y = 4,3
#result = x * x + x * y + y * x + y * y
#print(f"({x} + {y}) ^ 2 = {result}")

#COMPIERE LA DISTANZA ATTRAVERSO LE 2 COORDINATE
#import math 
#p1 = [4, 0]
#p2 = [6, 6]
#result = math.sqrt ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
#print(result)

#CONTROLLO SE IL FILE ESISTE (il commando open è per creare il file)
#import os.path
#open('abc.py', 'w')
#print(os.path.isfile('abc.py'))

#THE BOSS OF THE GYM
#import webbrowser
#webbrowser.open("https://youtu.be/jhzzQd5hdCM")

# PER CONTROLLARE SE PYTHON FUNZIONA SU 32 BIT O 64 BIT
#import struct
#print(struct.calcsize("P") * 8)

#MI DICE LE INFORMAZIONI DEL SISTEMA OPERATIVO SU QUALE MI TROVO 
#import platform
#import os
#print(os.name)
#print(platform.system())
#print(platform.release())
#print(platform.processor())

#SORTEGGIO DEI FILE DATA
#import glob
#import os
#files = glob.glob("*.py")
#files.sort(key=os.path.getmtime)
#print("\n".join(files))

#TROVA IL NUMERO CHE MANCA NELLA LISTA
#def li(num_list):
#    a,b = num_list[0],num_list[-1]
#    result = []
#    for n in range(a,b):
#        if n not in num_list:
#            result.append(n)
#    return result
#print(li([1,2,3,4,6,8,9,10,13,14,15]))

#IL MIO RADICE QUADRATA
#def my_sqrt(x):
#    if x < 2: return x 
#   left = 1
#   right = int(x/2)+1
#   while left <= right:
#       mid = int((left + right) / 2)
#       if mid * mid == x:
#           return mid
#       if mid * mid > x:
#           right = mid - 1
#       else:
#           left = mid + 1
#   return right        
#print(my_sqrt(64))

#CONVERTITORE DA DECIMALE IN BINARIO
#def binario(n):
#    print(bin(n))
#binario(5)

