"""

"""

filename = "Day 6\input.txt"

def main():
    """The solution to the problem"""
    file = open(filename)
    lines = file.readlines()

    for i in range(len(lines)):
        if (lines[i][-1] == '\n'):
            lines[i] = lines[i][:-1]
    
    result_array = [] #array with all the final values for each operation
    current_array = [] #temp array containing all values until the operator is found
    
    for col in range(len(lines[0]) - 1, -1, -1):
        res = ""
        operater = None
        
        for row in range(len(lines)):
            value = lines[row][col]
            if value in ['*', '+']:
                operater = value
            elif value != " ":
                res += value
        
        if (res != ""):
            current_array.append(int(res))

        if (operater):
            result = current_array[0]
            for value in current_array[1:]:
                match operater:
                    case "*":
                        result *= value
                    case "+":
                        result += value
                    case _:
                        print("Unexpected symbol detected")
            
            result_array.append(result)
            current_array = []
    
    sum = 0
    for value in result_array:
        sum += value

    print(sum)


main()