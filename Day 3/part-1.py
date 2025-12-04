"""
Idea 1:
    Iterate through the whole line
    Search for 9s, then 8s, then 7s 

Idea 2:
    Find the highest number that excludes the last number
    Find the highest number that excludes the first number and the picked number
    ^Those are your two numbers
"""

filename = "Day 3\input.txt"

def main():
    """The solution to the problem"""
    file = open(filename)
    lines = file.readlines()

    total = 0

    for line in lines:
        int_line = []
        for i in range(len(line)):
            if (line[i] != '\n'):
                int_line.append(int(line[i]))
        total += find_highest(int_line)

    print(total)

def find_highest(line):
    """Finds the highest 2-digit combination in a number"""
    first_number = 0
    second_number = 0
    index = 0

    for i in range(len(line) - 1):
        value = line[i]
        if value > first_number:
            first_number = value
            index = i

    for j in range(1, len(line)):
        value = line[j]
        if (value > second_number) and (j > index):
            second_number = value

    final_str_num = str(first_number) + str(second_number)
    print(final_str_num)
    return int(final_str_num)


main()