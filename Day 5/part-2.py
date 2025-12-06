"""
Idea 1 (deemed too slow)
    - Add all possible values to a set
    - Find the length of the set

 Idea 2
    - Keep track of ranges 
    - Update ranges if the start, stop values are different
        without having to iterate through every number
    Cases
        - 3-5 => 4-6 => 4-6 is added
        - 3-5 => 2-4 => 2-5 is added  
    - Thinking of whether to update it for each value input
        or get the full list then iterate and update
    
    - EDIT  - Went with iterate as you add instead of add all then iterate through
            - I think this is easier although the logic would work the same
"""

filename = "Day 5\input.txt"

def main():
    """The solution to the problem"""
    file = open(filename)
    lines = file.readlines()

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
        
        add_range(start, stop, possible_values)

        index += 1
        line = lines[index]
    
    total = calc_total(possible_values)
    print(total)

def calc_total(possible_values: list):
    """Find the total of the ranges in possible_values list"""
    total = 0

    for (start, stop) in possible_values:
        total += (stop - start + 1)
    
    return total
    


def add_range(start: int, stop: int, possible_values: list):
    """Adds the range from start to stop to possible_values
        and updates every other entry to match
        (that doesnt make sense but idc)
        """
    for i in range(len(possible_values)):
        list_start, list_stop = possible_values[i]
        
        #Check if any values are in between the added range
        if (start <= list_start) and (stop >= list_stop):
            possible_values.pop(i)
            return add_range(start, stop, possible_values)


        #Case when start value is between an existing range
        if (start >= list_start) and (start <= list_stop):
            if (stop <= list_stop):
                return
            else:
                possible_values.pop(i)
                return add_range(list_start, stop, possible_values)

        #Case when start is not between the range but stop is 
        elif (stop >= list_start) and (stop <= list_stop):
            possible_values.pop(i)
            return add_range(start, list_stop, possible_values)
    
    return possible_values.append((start, stop))


main()