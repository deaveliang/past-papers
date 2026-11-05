# Question 1(a)

# Initialise an array to player name and their high scores.

LIST_LENGTH = 10
player_data = [[None for i in range(2)] for j in range(LIST_LENGTH + 1)]

# Question 1(b)

def read_high_scores(file_name):
    try:
        file = open(file_name, "r")
        name = True
        count = 0
        for line in file:
            if name:
                player_data[count][0] = line.strip()
                name = False
            else:
                player_data[count][1] = int(line.strip())
                name = True
                count += 1
        file.close()
    except FileNotFoundError:
        print("file not found!")
    

# Question 1(c)


def output_high_score():
    for i in range(LIST_LENGTH):
        print(player_data[i][0], player_data[i][1])

# Question 1(d)(i)

read_high_scores("HighScore.txt")
output_high_score()

# Question 1(e)(i)

NAME_LENGTH = 3
MIN_SCORE = 1
MAX_SCORE = 100000

name = str(input("name: "))
while len(name) != NAME_LENGTH:
    print(f"name must be {NAME_LENGTH} letters only!")
    name = str(input("name: "))

score = int(input("score: "))
while score < MIN_SCORE or score > MAX_SCORE:
    print(f"score must be between {MIN_SCORE} and {MAX_SCORE} inclusive!")
    score = int(input("score: "))

# Question 1(e)(ii)

new_player_data = player_data

def create_new_list(name, score):
    if new_player_data[LIST_LENGTH - 1][1] > score:
        return
    else:
        new_player_data[LIST_LENGTH][0] = name
        new_player_data[LIST_LENGTH][1] = score
        swap = False
        for i in range(LIST_LENGTH + 1):
            for j in range(LIST_LENGTH - i):
                if new_player_data[j][1] < new_player_data[j + 1][1]:
                    tmp = new_player_data[j]
                    new_player_data[j] = new_player_data[j + 1]
                    new_player_data[j + 1] = tmp
                    swap = True
            if not swap:
                break

# Question 1(e)(iii)

print(player_data)
create_new_list(name, score)
print(new_player_data)

# Question 1(f)

def write_top_ten(file_name):
    try:
        file = open(file_name, "w")
        for i in range(LIST_LENGTH):
            for j in range(2):
                file.write(str(new_player_data[i][j]) + "\n")
        file.close()
    except FileNotFoundError:
        print("file not found!")

write_top_ten("NewHighScore.txt")