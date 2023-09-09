class Queue:
    def __init__(self):
        self.store = []

    def enqueue(self, value):
        self.store.append(value)

    def dequeue(self):
        return self.store.pop(0)

    def peek(self):
        return self.store[0]

    def contains(self, value):
        return value in self.store

    def values(self):
        return list(self.store)

    def is_empty(self):
        return True if len(self.store) < 1 else False
