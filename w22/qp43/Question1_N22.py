# Question 1(a)
# Initialise array with space for 100 integers.
data_array = [0] * 100

# Question 1(b)
# Read the numbers in file ands tore in data_array.
def read_file(file_name):
    try:
        file = open(file_name, "r")
        for line in file:
            data_array.append(int(line.strip()))
        file.close()
    except:
        print("error")

# Question 1(c)
# Count the number of times the number appears in the file.
def find_values(file_name):
    value = int(input("number (1-100): "))
    while value > 100 or value < 1:
        print("number must be between 1-100 inclusive!")
        value = int(input("number (1-100): "))
    count = 0
    file = open(file_name, "r")
    for line in file:
        if int(line.strip()) == value:
            count += 1
    return count

# Question 1(d)(i)
read_file("IntegerData.txt")
count = find_values("IntegerData.txt")
print("count:", count)

# Question 1(e)
def bubble_sort(array):
    swap = False
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                tmp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = tmp
                swap = True
        if not swap:
            break

bubble_sort(data_array)