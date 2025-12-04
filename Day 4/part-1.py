"""
Ideas
    - Format into 2-D array
    - Scan around the points

    - Else use string as an array and scan around the points
"""

filename = "Day 4\input.txt"

def main():
    """The solution to the problem"""
    file = open(filename)
    lines = file.readlines()

    count = 0

    for i in range(len(lines)):
        if (lines[i][-1] == '\n'):
            lines[i] = lines[i][:-1]

    for i in range(len(lines)):
        line = lines[i]

        for j in range(len(line)):
            if line[j] == '@':
                if check_valid(i, j, lines):
                    count += 1
    print(count)


def check_valid(i, j, lines):
    """Scans aroundt the point (i,j) to check if it's valid"""
    count = 0

    #Check top 3
    if (i > 0):
        if (j > 0) and (lines[i-1][j-1] == '@'):
            count+=1

        if (lines[i-1][j] == '@'):
            count+=1

        if (j < (len(lines) - 1)) and (lines[i-1][j+1] == '@'):
            count+=1

    #Check sides
    if (j > 0) and (lines[i][j-1] == '@'):
        count+=1
    if (j < (len(lines) - 1)) and (lines[i][j+1] == '@'):
        count+=1

    #Check bottom 3
    if (i < (len(lines) - 1)):
        if (j > 0) and (lines[i+1][j-1] == '@'):
            count+=1

        if (lines[i+1][j] == '@'):
            count+=1

        if (j < (len(lines) - 1)) and (lines[i+1][j+1] == '@'):
            count+=1

    if count < 4:
        return True
    return False

main()