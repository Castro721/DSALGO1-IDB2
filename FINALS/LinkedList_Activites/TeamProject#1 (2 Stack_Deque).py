from LinkedStack import LinkedStack


class LinkedDeque:
    def __init__(self):
        self.front_stack = LinkedStack()
        self.back_stack = LinkedStack()

    def len(self):
        return len(self.front_stack) + len(self.back_stack)

    def is_empty(self):
        return self.len() == 0

    def add_last(self, e):
        self.back_stack.push(e)

    def add_first(self, e):
        self.front_stack.push(e)

    def delete_last(self):
        if self.is_empty():
            raise Exception('Deque is empty')

        if self.back_stack.is_empty():
            while not self.front_stack.is_empty():
                self.back_stack.push(self.front_stack.pop())

        return self.back_stack.pop()

    def delete_first(self):
        if self.is_empty():
            raise Exception('Deque is empty')

        if self.front_stack.is_empty():
            while not self.back_stack.is_empty():
                self.front_stack.push(self.back_stack.pop())

        return self.front_stack.pop()

    def first(self):
        if self.is_empty():
            raise Exception('Deque is empty')

        if self.front_stack.is_empty():
            while not self.back_stack.is_empty():
                self.front_stack.push(self.back_stack.pop())

        return self.front_stack.top()

    def last(self):
        if self.is_empty():
            raise Exception('Deque is empty')

        if self.back_stack.is_empty():
            while not self.front_stack.is_empty():
                self.back_stack.push(self.front_stack.pop())

        return self.back_stack.top()


dq = LinkedDeque()
dq.add_last(1)
dq.add_last(2)
dq.add_last(3)
dq.add_first(0)
print(dq.delete_last())
print(dq.delete_first())
print(dq.first())
print(dq.last())
print(dq.is_empty())
print(dq.len())



