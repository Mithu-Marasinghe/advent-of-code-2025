import math
"""
 
"""

filename = "Day 8\input.txt"

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
    

    for key, values in sorted_distances:
        i, j = key

        index_j = find_group_index(j, positions)
        index_i = find_group_index(i, positions)
        
        
        if (index_i == index_j):
            continue

        for val in positions[index_j]:
            positions[index_i].append(val)

        positions.pop(index_j)

        if len(positions) == 1:
            display_distance(key, formatted_lines)
            return


def display_distance(pos: tuple, formatted_lines: list):
    """Prints the distance between the two x values in the tuple pos"""
    val1 =  formatted_lines[pos[0]][0]
    val2 = formatted_lines[pos[1]][0]
    print(val1 * val2)


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