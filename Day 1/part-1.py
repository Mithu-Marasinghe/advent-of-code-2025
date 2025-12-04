
filename = "Day 1\input.txt"
STARTING_POSTION = 50

def main():
    """The solution to the problem"""
    count = 0
    current_pos = STARTING_POSTION

    file = open(filename)
    lines = file.readlines()
    for line in lines:
        amount = int(line[1:])
        if line[0] ==  "L":
            amount = -amount

        new_position = (current_pos + amount) % 100

        print(f"{current_pos} was moved {amount} to {new_position} and the count is {count}")

        if new_position == 0:
            count+=1
        current_pos = new_position
    print(count)


main()