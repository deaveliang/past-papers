# Open file in read mode.
file = open("names.txt", "r")

# Read the entire content of the file.
text = file.read()
print("Entire Content")
print(text)
file.close()

# Read a specified amount of characters from file.
file = open("names.txt", "r")
text = file.read(5)
print("First 5 Characters")
print(text)
file.close()

# Read line by line and loop through every line in the file.
file = open("names.txt", "r")
for line in file:
    # Every line in the file ends with \n, so by setting end="", we do not print \n.
    print(line, end="")
file.close()

# This is an issue when we store lines into the array.
file = open("names.txt", "r")
array = []
for line in file:
    array.append(line)
print("We have NOT removed the \\n from every line.")
print(array)
file.close()

file = open("names.txt", "r")
array = []
for line in file:
    # strip() removes non-printing characters from the string from both ends.
    # rstrip() and lstrip() removes the characters from the right and left ends.respectively.
    array.append(line.strip())
print("Now the \\n is stripped from every line.")
print(array)
file.close()

# Remember to close file.
file.close()

# How to do expection handling?
try:
    file = open("nothing.txt", "r")
    for line in file:
        print(line.strip())
    # Closing file in the try block is NOT a good practice.
    file.close()
# We can cast error messages.
except FileNotFoundError as error:
    print("File not found. Error:", error)
finally:
    print("Job done.")

# Open file in write mode.
copy = open("copy.txt", "w")
for item in array:
    copy.write(f"{item}\n")
copy.close()

# Store multiple values, which are seperated by commas.
data_array = []
data_file = open("data.txt", "r")
for line in data_file:
    data_array.append(line.strip().split(","))
data_file.close()

for i in range(len(data_array)):
    for j in range(len(data_array[i])):
        print(data_array[i][j], end=" ")
    print()

# You can also store the values in different variables instead of a single array.
line = "Deave,17,Male"
name, age, gender = line.split(",")