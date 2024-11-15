from LinkedStack import LinkedStack as Stack
from LinkedDeque import LinkedDeque as Deque

D = Deque()
S = Stack()

for i in range(1, 9):
    D.insert_last(i)

for i in range(3):
    S.push(D.delete_last())#[8,7,6]

D.insert_first(D.delete_last())#[5,1,2,3,4]
S.push(D.delete_last())#[8,7,6,4]
D.insert_last(D.delete_first())#[1,2,3,5]

for i in range(4):
    D.insert_last(S.pop())

while not D.is_empty():
    print(D.delete_first())
