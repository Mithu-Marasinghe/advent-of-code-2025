import math
"""
Implemented nested for loops (O(nlogn))
    - Got the correct answer but took a few minutes

Idea:
    - We have a list of lists
    - This will be length of {lines}
    - You iter through each list -> and compare with each other list
    - Once you find the lowest distance -> append all items to other index -> delete index
    - Go until the length of the list of lists is 2
    - Edit(Was faster but still too slow)

New Idea:
    - Initialize dict of distances
    - Sort by length and iter through each one
    - PS: I realize im stupid for not thinking of this 
"""

filename = "Day 8\input.txt"

MAX_COUNT = 1000

def main():
    """The solution to the problem"""
    file = open(filename)
    lines = file.readlines()

    for i in range(len(lines)):
        if (lines[i][-1] == '\n'):
            lines[i] = lines[i][:-1]

    formatted_lines = []

    for line in lines:
        x, y, z = line.split(',')
        formatted_lines.append((int(x), int(y), int(z)))

    positions = dict()
    distances = dict()

    for i in range(len(formatted_lines)):
        positions[i] = [i]

    for i in range(len(formatted_lines)):
        for j in range(i):
            val1 = formatted_lines[i]
            val2 = formatted_lines[j]

            result = math.cbrt(((val1[0] - val2[0])**2) + ((val1[1] - val2[1])**2) + ((val1[2] - val2[2])**2))

            distances[(i,j)] = result

    sorted_distances = sorted(distances.items(), key=lambda item: item[1])
    
    count = 0
    for key, values in sorted_distances:
        if count == MAX_COUNT:
            break
        i, j = key

        index_j = find_group_index(j, positions)
        index_i = find_group_index(i, positions)
        
        
        if (index_i == index_j):
            count += 1
            continue

        for val in positions[index_j]:
            positions[index_i].append(val)

        positions.pop(index_j)

        count += 1

    max_length = find_max_length(positions)
    print(max_length)


def find_max_length(positions: dict):
    """Find the mult of the maximum 3 lengths of groups"""
    sorted_dict = sorted(positions.items(), key= lambda items: len(items[1]), reverse=True)

    total = len(sorted_dict[0][1]) * len(sorted_dict[1][1]) * len(sorted_dict[2][1])
    return total
   

def find_group_index(j: int, positions: dict):
    """Find the index of the group j belongs to in dict positions"""
    for key, values in positions.items():
        for value in values:
            if value == j:
                return key
 
main()