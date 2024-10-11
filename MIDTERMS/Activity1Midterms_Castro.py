class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        print("Pushed:", self.items)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def len(self):
        return len(self.items)

    def top(self):
        if not self.is_empty():
            return self.items[-1]

    def get_items(self):
        print("Stack content:", self.items)


S = Stack()

print("Part 1")
S.push(5)
S.push(3)
print("Size:", S.len())
print("Popped:", S.pop())
print("Is empty:", S.is_empty())
print("Popped:", S.pop())
print("Is empty:", S.is_empty())

try:
    print("Popped:", S.pop())
except Exception as e:
    print(e)

S.push(7)
S.push(9)
print("Top element:", S.top())
S.push(4)
print("Size:", S.len())
print("Popped:", S.pop())
S.push(6)
S.push(8)
print("Popped:", S.pop())
S.get_items()

X = Stack()
print("\nPart 2")
X.push(5)
X.push(3)
print("Popped:", X.pop())
X.push(2)
X.push(8)
print("Popped:", X.pop())
print("Popped:", X.pop())
X.push(9)
X.push(1)
print("Popped:", X.pop())
X.push(7)
X.push(6)
print("Popped:", X.pop())
print("Popped:", X.pop())
X.push(4)
print("Popped:", X.pop())
print("Popped:", X.pop())
X.get_items()

