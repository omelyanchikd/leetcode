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
        self.stack = Node(value)
        self.stack.next = old

    def pop(self):
        if not self.is_empty():
            value = self.stack.value
            self.stack = self.stack.next
            return value
        return None


def isValid(s: str) -> bool:
    brackets = Stack()
    OPEN_BRACKETS = ['(', '[', '{']
    CLOSE_BRACKETS = [')', ']', '}']
    BRACKET_PAIRS = {']': '[', '}': '{', ')': '('}
    for bracket in s:
        if bracket in OPEN_BRACKETS:
            brackets.push(bracket)
        if bracket in CLOSE_BRACKETS:
            bracket_to_delete = brackets.pop()
            if bracket_to_delete != BRACKET_PAIRS[bracket]:
                return False
    if not brackets.is_empty():
        return False
    return True


if __name__ == '__main__':
    s = "{[]}"
    print(isValid(s))
