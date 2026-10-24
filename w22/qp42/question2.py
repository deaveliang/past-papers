# Question (a)

# Initialise a 2D array, jobs, and a variable, numberOfJobs.
jobs = [[None for i in range(2)] for j in range(100)]
numberOfJobs = 0

# Question (b)

def initialise():
    numberOfJobs = 0

    for i in range(len(jobs)):
        for j in range(2):
            jobs[i][j] = -1

# Question (c)

def addJob(job_no, priority):
    # Index of next free element would be numberOfJobs.
    global numberOfJobs # Fix error: cannot access local variable where it is not associated with a value.
    if numberOfJobs >= 100:
        print("Not added")
    else:
        jobs[numberOfJobs][0] = job_no
        jobs[numberOfJobs][1] = priority
        print("Added")
    numberOfJobs += 1

# Question (d)

initialise()

addJob(12, 10)
addJob(526, 9)
addJob(33, 8)
addJob(12, 9)
addJob(78, 1)

# Question (e)

"""
Find the lowest priority and store the index.
Swap the element at index_floor with the element with the lowest priority.
Increment index_floor by 1.
Repeat again.
"""

def selectionSort():
    for i in range(numberOfJobs - 1): # Subtract one becasue the last element is already sorted.
        lowest_priority = jobs[i][1]
        lowest_index = i

        for j in range(i + 1, numberOfJobs):
            if jobs[j][1] < lowest_priority:
                lowest_priority = jobs[j][1]
                lowest_index = j

        temp = jobs[i]
        jobs[i] = jobs[lowest_index]
        jobs[lowest_index] = temp

"""
Start with the second element, since the first element is assume to be sorted.
Compare second element with the first element if the second is smaller swap them.
Move to the third element, compare it with first two, and put it in its correct position
Repeat until array is sorted.
"""

# Question (f)

def printArray():
    for i in range(numberOfJobs):
        print(f"{jobs[i][0]} priority {jobs[i][1]}")
    print()

# Question (g)(i)

selectionSort()
printArray()
