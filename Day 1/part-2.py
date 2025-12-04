
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

        if (current_pos + amount) > 99:
            count+=((current_pos + amount) // 100)
        elif (current_pos + amount <= 0):
            count+=(abs(current_pos + amount) // 100)
            if current_pos > 0: count +=1


        print(f"{current_pos} was moved {amount} to {new_position} and the count is {count}")

        current_pos = new_position
    print(count)


main()