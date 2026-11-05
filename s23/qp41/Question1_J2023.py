# Question 1(a)(i)

data_array = []

# Question 1(a)(ii)

try:
    file = open("Data.txt", "r")
    for line in file:
        data_array.append(int(line))
    file.close()
except FileNotFoundError:
    print("file not found!")

# Question 1(b)(i)

def print_array(array):
    for item in data_array:
        print(item, end=" ")
    print()

# Question 1(b)(ii)

print_array(data_array)

# Question 1(c)

def linear_search(array, value):
    count = 0
    for item in data_array:
        if item == value:
            count += 1
    return count

# Question 1(d)(i)

MIN_VALUE = 0
MAX_VALUE = 100

number = int(input("number: "))
while number > MAX_VALUE or number < MIN_VALUE:
    print(f"number must be between {MIN_VALUE} and {MAX_VALUE}!")
    number = int(input("number: "))

result = linear_search(data_array, number)
print(f"The number is {number} is found {result} times.")