"""
Idea 1:
    
first number - 0
    need 0 - (len() - 12)

"""

filename = "Day 3\input.txt"
TOTAL_NUMS = 12

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
    result = ""
    indexes = [-1]

    for i in range(TOTAL_NUMS, 0, -1):
        number = 0
        last_index = 0
        
        for j in range(0, len(line) - i + 1):
            value = line[j]
            if (value > number) and (j > indexes[-1]) and (j not in indexes):
                number  = value
                last_index = j
        
        indexes.append(last_index)
        result += str(number)
    
    return int(result)

main()
