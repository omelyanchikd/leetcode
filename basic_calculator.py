import math

class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class Stack:
    def __init__(self):
        self.stack = None

    def is_empty(self):
        return self.stack is None

    def push(self, value):
        old = self.stack
        self.stack = Node(value, old)

    def pop(self):
        if not self.is_empty():
            value = self.stack.value
            self.stack = self.stack.next
            return value
        return None

    def top(self):
        if not self.is_empty():
            return self.stack.value
        return None


def calculate(s: str) -> int:
    numbers_stack = Stack()
    operators_stack = Stack()
    number_string = ""
    negative = False
    evaluate_next = False
    for character in s:
        if character.isdigit():
            number_string += character
        else:
            if number_string:
                if negative:
                    numbers_stack.push(-int(number_string))
                    negative = False
                else:
                    numbers_stack.push(int(number_string))
                number_string = ""
                if evaluate_next:
                    second = numbers_stack.pop()
                    first = numbers_stack.pop()
                    evaluate_next = False
                    operator = operators_stack.pop()
                    if operator == '*':
                        numbers_stack.push(first * second)
                    elif operator == '/':
                        numbers_stack.push(math.trunc(first /second))
            if character == '-':
                negative = True
                operators_stack.push('+')
            elif character in ['*', '/']:
                operators_stack.push(character)
                evaluate_next = True
            elif operator == '+':
                operators_stack.push(character)
    if number_string:
        if negative:
            numbers_stack.push(-int(number_string))
            negative = False
        else:
            numbers_stack.push(int(number_string))
    while not operators_stack.is_empty():
        operator = operators_stack.pop()
        second = numbers_stack.pop()
        first = numbers_stack.pop()
        if operator == '+':
            numbers_stack.push(first + second)
        elif operator == '*':
            numbers_stack.push(first * second)
        elif operator == '/':
            numbers_stack.push(math.trunc(first/second))
    return numbers_stack.pop()

if __name__ == '__main__':
    s = "14-3/2"
    print(calculate(s))

