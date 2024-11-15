from LinkedQueue import LinkedQueue as Queue
from LinkedDeque import LinkedDeque as Deque


D = Deque()
Q = Queue()

for i in range(1, 9):
    D.insert_last(i)

for i in range(3):
    Q.enqueue(D.delete_last())#[8,7,6]

D.insert_first(D.delete_last())#[5,1,2,3,4]
Q.enqueue(D.delete_last())#[8,7,6,4]
D.insert_last(D.delete_first())#[1,2,3,5]

for i in range(4):
    D.insert_last(Q.dequeue())
for i in range(4):
    Q.enqueue(D.delete_last())
for i in range(4):
    D.insert_last(Q.dequeue())

while not D.is_empty():
    print(D.delete_first())






