# Question (a)
# Declare the global 1D array, arrayData, with ten elements.
arrayData = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8]
arrayLength = len(arrayData)

# Question (b)(i)
# Define a function called linearSearch.
def linearSearch(value):
    for i in range(arrayLength):
        if arrayData[i] == value:
            return True
    return False

# Question (b)(ii)
# Get input from user.
number = int(input("number: "))

# Output appropriate message.
if linearSearch(number):
    print("found")
else:
    print("not found")

# Question (c)
def bubbleSort():
    for i in range(arrayLength):
        for j in range(arrayLength - 1):
            if arrayData[j] >= arrayData[j + 1]:
                tmp = arrayData[j]
                arrayData[j] = arrayData[j + 1]
                arrayData[j + 1] = tmp

bubbleSort()
print(arrayData)
