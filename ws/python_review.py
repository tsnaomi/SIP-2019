
print("PYTHON WORKSHEET")  # :)


# Strings ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 1) ---------------------------------|

woah = "sisterho"
print(woah)

# 2) ---------------------------------|

woah = "sisterho"
print(len(woah))

# Strings + Loops ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 3) ---------------------------------|

dog = "dog"
for i in range(dog):
    print(i)

# 4) ---------------------------------|

dog = "dog"
for i in dog:
    print(i)

# 5) ---------------------------------|

dog = "dog"
for i in dog:
    print("woof!")

# 6) ---------------------------------|

dog = "dog"
for i in range(len(dog)):
    print(i)

# Lists, Strings, + Loops ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 7) ---------------------------------|

ice_cream = []
num_of_scoops = 8

for i in range(num_of_scoops):
	ice_cream.append("scoop")

print(ice_cream)

# 8) ---------------------------------|

wah = "Wah!" * 5
print(wah)

# 9) ---------------------------------|

wah = ["ZipZapZop!"] * 3
print(wah)

# Lists + Conditionals ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 10) --------------------------------|

numbers = [0, 2, 7, 9, 10]
huh_1 = []
huh_2 = []

for i in numbers:
	huh_1.append(i)

	if i % 2 == 0:
		huh_2.append("even")
	else:
		huh_2.append("odd")

print("numbers:", numbers)
print("list 1:", huh_1)
print("list 2:", huh_2)

# 11) --------------------------------|

numbers = [0, 2, 5, 9, 14, 16, 19]
huh_1 = []
huh_2 = []

for i in range(len(numbers)):
    huh_1.append(i)

    if numbers[i] % 2 == 0:
        numbers[i] = "even"
    else:
        numbers[i] = "odd"

print("numbers:", numbers)
print("list 1:", huh_1)
print("list 2:", huh_2)

# 12) --------------------------------|

numbers = [0, 2, 5, 9, 14, 16, 19]
huh_1 = []
huh_2 = []

for i in range(len(numbers)):
    huh_1.append(i)

    if numbers[i] % 2 == 0:
        huh_2[i] = "even"
    else:
        huh_2[i] = "odd"

print("numbers:", numbers)
print("list 1:", huh_1)
print("list 2:", huh_2)


# Booleans ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 13) --------------------------------|

town = [
    "villagers", "angel", "detective",
    "mafia", "joker", "peeker",
    ]

if "mafia" in town:
	print(True)
else:
	print(False)

# 14) --------------------------------|

print("mafia" in town)

# Counters ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 15) --------------------------------|

boba = 0
for more_please in range(20):
	boba += 1

print(boba)

# 16) --------------------------------|

boba = 0
for more_please in boba:
    boba += 1

print(boba)

# Functions ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 17) --------------------------------|

def coffee():
    return "Coffee coffee coffee!"

def morning():
    print("In the morning,")
    print("I drink")
    coffee()

morning()

# 18) --------------------------------|

def coffee():
    return "Coffee coffee coffee!"

def morning():
    print("In the morning,")
    print("I drink", coffee())

morning()

# Functions + Arguments ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 19) --------------------------------|

def add_pi(num):
    return n + 3.1415

def weird_math(n):
    add_pi(n)
    print(n)

weird_math(4)

# 20) --------------------------------|

def add_pi(num):
    return num + 3.1415

def weird_math(n):
    add_pi(n)
    print(n)

weird_math(4)

# 21) --------------------------------|

def add_pi(num):
    return num + 3.1415

def weird_math(n):
    n = add_pi(n)
    print(n)

weird_math(4)

# 22) --------------------------------|

def add_pi(num):
    return num + 3.1415

def weird_math(n):
    n += add_pi(n)
    print(n)

weird_math(4)
