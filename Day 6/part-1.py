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
    
    formatted_input = []

    for i in range(len(lines)):
        line = lines[i].split(" ")
        actual_lines = []
        
        for chars in line:
            if chars != " " and chars != "" and chars != "\n":
                actual_lines.append(chars)
        
        formatted_input.append(actual_lines)

    result_array = []

    for col in range(len(formatted_input[0])):
        operator = formatted_input[-1][col]
        for row in range(len(formatted_input) - 1):
            value = int(formatted_input[row][col])
            if row == 0:
                result = value
            else:
                match operator:
                    case "*":
                        result *= value
                    case "+":
                        result += value
                    case _:
                        print("Incorrect Symbol entered")
        result_array.append(result)
    
    print(sum(result_array))

main()