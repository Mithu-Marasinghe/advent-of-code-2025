"""
Idea 1
    - Dyanmic Progamming
    - Going to have to follow 1 line
    - End condition: If it is at the end of file
    - Branch condition: If there is a splitter 
    - Edit (Works but too slow)
    - Must implement cache system

Idea 2
    - Implement it the part-1 way (line by line)
    - Have (index, count) pairs for the amount of diversions for each index
    - Sum up all the counts
"""

filename = "Day 7\input.txt"

def main():
    """The solution to the problem"""
    file = open(filename)
    lines = file.readlines()

    for i in range(len(lines)):
        if (lines[i][-1] == '\n'):
            lines[i] = lines[i][:-1]
    
    start_index = 0
    cache = dict()

    #Start line
    start_line = lines[0]
    for i in range(len(start_line)):
        if start_line[i] == 'S':
            start_index = i

    count = follow_particle(start_index, lines[1:], 0, cache)
    print(count)


def follow_particle(line_index, lines, row, cache):
    """Follows the particle to the bottom of the file,
       recursively splitting"""
    #Check cache
    if (line_index, row) in cache:
        return cache[(line_index, row)]

    #Reach end of file
    if (row >= len(lines)):
        return 1
    
    #case: "."
    if lines[row][line_index] == ".":
        return follow_particle(line_index, lines, row + 1, cache)
    
    #case: "^"
    if lines[row][line_index] == "^":
        left_path =  follow_particle(line_index - 1, lines, row + 1, cache)
        right_path =  follow_particle(line_index + 1, lines, row + 1, cache)

        total = left_path + right_path
        cache[(line_index, row)] = total
        return total

    raise SyntaxError(f"Unexpected token: '{lines[row][line_index]}'")

main()