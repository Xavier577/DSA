class Stack:
    def __init__(self):
        self.store = []

    def push(self, value):
        self.store.append(value)

    def pop(self):
        return self.store.pop()

    def peek(self):
        return self.store[len(self.store) - 1]

    def contains(self, value):
        return value in self.store

    def values(self):
        return list(self.store)

    def isEmpty(self):
        return True if len(self.store) < 1 else False
