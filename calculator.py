from colorama import init
from colorama import Fore, Back, Style

# use Colorama to make Termcolor work on Windows too
init()

print(Back.GREEN)
print(Fore.BLACK)

what = input("What function? (+, -, *, /): ")

print(Back.CYAN)

a = float(input("Insert first number: "))
b = float(input("Insert second number: "))

print(Back.MAGENTA)

if what == "+":
	c = a + b
	print("Result: " + str(c))

elif what == "-":
	c = a - b
	print("Result: " + str(c))

elif what == "*":
	c = a * b
	print("Result: " + str(c))

elif what == "/":
	c = a / b
	print("Result: " + str(c))
	
else: 
	print("nope")