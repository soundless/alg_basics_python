#!/usr/bin/env python

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        if self:
            return "{}->{}".format(self.data, repr(self.next))

class LinkedQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        if self and self.head:
            return repr(self.head)

    def enqueue(self, item):
        node = Node(item)
        if self.isEmpty():
            self.head = node
        else:
            self.tail.next = node
        self.tail = node

    def dequeue(self):
        if self.isEmpty():
            raise Exception("Cannot dequeue an empty queue")
        item = self.head.data
        if self.head is self.tail:
            self.tail = None
        self.head = self.head.next
        return item

    def peek(self):
        if self.isEmpty():
            raise Exception("Cannot peek an empty queue")
        return self.head.data
    
    def isEmpty(self):
        return self.head is None

    def size(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
        return count


if __name__ == '__main__':
    lq = LinkedQueue()
    lq.enqueue("A")
    lq.enqueue("B")
    lq.enqueue("C")
    lq.enqueue("D")
    lq.enqueue("E")

    print lq.size() == 5
    print lq

    print lq.peek() == "A"
    for i in xrange(4):
        lq.dequeue()

    lq.enqueue("F")
    print lq.peek() == "E"
    print lq

    lq.dequeue()
    lq.dequeue()
    print lq.isEmpty() == True
