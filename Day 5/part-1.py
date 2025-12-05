"""
Idea 1
    - For each ingredient
        - Check all ranges and find a match

Idea 2 (deemed too slow)
    - Add all possible numbers to a set
        - Check if the number is in the set
"""

filename = "Day 5\input.txt"

def main():
    """The solution to the problem"""
    file = open(filename)
    lines = file.readlines()

    count = 0
    index = 0
    possible_values = []

    for i in range(len(lines)):
        if (lines[i][-1] == '\n'):
            lines[i] = lines[i][:-1]

    line = lines[index]

    while (line != ''):
        splitted_line = line.split('-')
        start = int(splitted_line[0])
        stop = int(splitted_line[1])
        
        possible_values.append((start, stop))
        index += 1
        line = lines[index]
    
    next_lines = lines[(index+1):]

    for next_line in next_lines:
        for (start, stop) in possible_values:
            if (int(next_line) >= start) and (int(next_line) <= stop):
                count += 1
                break

    print(count)


main()