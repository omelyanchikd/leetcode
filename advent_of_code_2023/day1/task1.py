def find_digits(line):
    first_digit = None
    last_digit = None
    for c in line:
        if c.isdigit():
            if first_digit is None:
                first_digit = c
            last_digit = c
    return first_digit, last_digit

def solution(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        code = 0
        for line in lines:
            first_digit, last_digit = find_digits(line)
            code += int(first_digit + last_digit)
        return code

if __name__ == '__main__':
    print(solution('input1.txt'))