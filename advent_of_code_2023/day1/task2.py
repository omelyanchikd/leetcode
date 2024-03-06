def find_digits(line):
    digits = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    digit_characters = ['z', 'e', 'r', 'o', 'n', 't', 'w', 'h', 'f', 'u', 'i', 'v', 's', 'x', 'g']
    first_characters = {
        'z': ['e'],
        'o': ['n'],
        't': ['w', 'h'],
        'f': ['o', 'i'],
        's': ['i', 'e'],
        'e': ['i'],
        'n': ['i'],
        'ze': ['r'],
        'on': ['e'],
        'tw': ['o'],
        'th': ['r'],
        'fo': ['']
    }
    first_digit = None
    last_digit = None
    digit = None
    for c in line:
        if c.isdigit():
            if first_digit is None:
                first_digit = c
            last_digit = c
            if digit is not None:
                digit = None
        elif c not in digit_characters:
            if digit is not None:
                try:
                    last_digit = int(digit)
                except:
                    digit = None
                if first_digit is None:
                    first_digit = last_digit
                digit = None
        else:
            if digit is None:
                if digit in first_characters:
                    digit = c
            elif len(digit) == 1:
               if first_characters[digit] == c:
                   digit += c

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