# Quesiton 1(a)

# dataStored is a global 1D array of type integer that stores up to 20 elements.
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

# Question 1(d)(i)

def bubbleSort():
    swap = False

    for i in range(numberItems):
        for j in range(numberItems - i - 1):
            if dataStored[j] > dataStored[j + 1]:
                tmp = dataStored[j]
                dataStored[j] = dataStored[j + 1]
                dataStored[j + 1] = tmp
                swap = True

        if not swap:
            break

# Question 1(d)(ii)

bubbleSort()
print(dataStored)

# Question 1(e)(i)

def linearSearch(dataToFind):
    for i in range(numberItems):
        if dataToFind == dataStored[i]:
            return i
    return -1

# Question 1(e)(ii)

number = int(input("Search: "))
index = linearSearch(number)
print(index)
