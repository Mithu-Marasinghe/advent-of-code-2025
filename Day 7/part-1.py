"""
Idea
    - Iterate through each line and split and keep count of splits
"""

filename = "Day 7\input.txt"

def main():
    """The solution to the problem"""
    file = open(filename)
    lines = file.readlines()

    for i in range(len(lines)):
        if (lines[i][-1] == '\n'):
            lines[i] = lines[i][:-1]
    
    indexes = set()
    count = 0

    #Start line
    start_line = lines[0]
    for i in range(len(start_line)):
        if start_line[i] == 'S':
            indexes.add(i)
    
    #Remaining lines
    for i in range(1, len(lines), 1):
        line = lines[i]
        
        for j in range(len(line)):
            character = line[j]
            
            if j in indexes:
                match character:
                    case ".":
                        continue
                    case "^":
                        count += 1
                        indexes.remove(j)
                        
                        if j > 0:
                            indexes.add(j - 1)
                        if j < (len(line) - 1):
                            indexes.add(j + 1)
    
    print(count)

main()