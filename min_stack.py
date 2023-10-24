class Node:
    def __init__(self):
        self.value = None
        self.next = None
        self.occurances = 1

class Stack:

    def __init__(self):
        self.stack = None

    def push(self, val: int) -> None:
        old = self.stack
        self.stack = Node()
        self.stack.value = val
        self.stack.occurances = 1
        self.stack.next = old

    def pop(self) -> None:
        if self.stack is not None:
            self.stack = self.stack.next

    def top(self):
        if self.stack is not None:
            return self.stack.value
        return None


class MinStack:

    def __init__(self):
        self.stack = Stack()
        self.min_stack = Stack()

    def push(self, val: int) -> None:
        self.stack.push(val)
        top_min = self.min_stack.top()
        if top_min is not None:
            if val < top_min:
                self.min_stack.push(val)
            elif val == top_min:
                self.min_stack.stack.occurances += 1
        else:
            self.min_stack.push(val)

    def pop(self) -> None:
        value_to_delete = self.stack.top()
        self.stack.pop()
        top_stack = self.stack.top()
        if top_stack is None:
            self.min_stack.pop()
        else:
            top_min = self.min_stack.top()
            if value_to_delete == top_min:
                if self.min_stack.stack.occurances == 1:
                    self.min_stack.pop()
                else:
                    self.min_stack.stack.occurances -= 1

    def top(self):
        return self.stack.top()

    def getMin(self):
        return self.min_stack.top()

if __name__ == '__main__':
    minStack = MinStack()
    minStack.push(0)
    minStack.push(1)
    minStack.push(0)
    print(minStack.getMin())
    minStack.pop()
    print(minStack.getMin())
