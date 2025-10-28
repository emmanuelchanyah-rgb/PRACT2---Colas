class Node:
    def __init__(self, data):
        self.data = data    
        self.next = None     

class LinkedListQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None
    def enqueue(self, item):
        node = Node(item)
        if self.rear is None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node


    def dequeue(self):

        if self.is_empty():
            raise IndexError("No se puede desencolar: la cola está vacía.")
        value = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("No se puede consultar: la cola está vacía.")
        return self.front.data
