# Quesiton 1(a)

# dataStored is a global 1D array of type integer that stores up 20 elements.
# numberItems is a global variable that stores the quantity of items the array contains.
numberItems = 0
dataStored = [0] * 20

# Question 1(b)

def initialise():
    global numberItems

    numberItems = int(input("Number of items: "))
    while numberItems > 20 or numberItems < 1:
        numberItems = int(input("Number of items: "))

    for i in range(numberItems):
        dataStored[i] = int(input(f"Item {i + 1}: "))

# Question 1(c)(i)

numberItems = 0
initialise()