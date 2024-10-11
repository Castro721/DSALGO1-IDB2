
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)
        print("Enqueued:", item)
        print("Que After Enqueue():", self.items)
        print()

    def dequeue(self):
        try:
            print("Dequeued:", self.items[0])
            que = self.items.pop(0)
            print("Que after dequeue():", self.items)
            print()
            return que
        except Exception as e:
            print("Dequeued from an empty queue")

    def is_empty(self):
        return self.items == []

    def len(self):
        return len(self.items)

    def first(self):
        try:
            return self.items[0]
        except Exception as e:
            print(e)

    def get_items(self):
        print("Queue content:", self.items)


Q = Queue()

Q.enqueue(5)
Q.enqueue(3)
print("Length:", Q.len())
Q.dequeue()
print("Is_Empty:", Q.is_empty())
Q.dequeue()
print("Is_Empty:", Q.is_empty())
Q.dequeue()
Q.enqueue(7)
Q.enqueue(9)
print("Front:", Q.first())
Q.enqueue(4)
print("Length:", Q.len())
Q.dequeue()
print("\nPart II")
R = Queue()
R.enqueue(5)
R.enqueue(3)
R.dequeue()
R.enqueue(2)
R.enqueue(8)
R.dequeue()
R.dequeue()
R.enqueue(9)
R.enqueue(1)
R.dequeue()
R.enqueue(7)
R.enqueue(6)
R.dequeue()
R.dequeue()
R.enqueue(4)
R.dequeue()
R.dequeue()
