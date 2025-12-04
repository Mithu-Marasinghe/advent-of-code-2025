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
    str_num_length = len(str_num) // 2

    if str_num[:str_num_length] == str_num[str_num_length:]:
        return True

    return False


main()