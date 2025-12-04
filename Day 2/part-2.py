filename = "Day 2\input.txt"


def main():
    """The solution to the problem"""
    total = 0

    file = open(filename)
    lines = file.readlines()
    values = lines[0]
    
    ids = values.split(",")
    for id in ids:
        split_id = id.split("-")
        start = int(split_id[0])
        end = int(split_id[1])

        for i in range(start, end + 1):
            if check_number(i):
                total += i
        
    print(total)

def check_number(num):
    """Checks if the number is an invalid ID"""
    if num < 10:
        return False
    str_num = str(num)
    str_num_length = len(str_num)

    for i in range(1, str_num_length):
        if (str_num_length % i == 0):

            first_component = str_num[:i]
            is_invalid = True

            for j in range(i, str_num_length, i):
                if ((str_num[j:j+i]) != first_component):
                    is_invalid = False
                    break

            if is_invalid:
                return True

    return False


main()