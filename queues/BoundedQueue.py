#!/usr/bin/env python

class BoundedQueue(object):
    def __init__(self, capacity=10):
        self.array = [None for i in xrange(capacity)]
        self.size = 0
        self.head = 0
        self.tail = 0

    def __repr__(self):
        return repr(self.array)

    def enqueue(self, item):
        if self.isFull():
            raise Exception("Cannot add to full queue")
        self.array[self.tail] = item
        self.tail = (self.tail + 1) % len(self.array)
        self.size += 1

    def dequeue(self):
        if self.isEmpty():
            raise Exception("Cannot remove from empty queue")
        item = self.array[self.head]
        self.array[self.head] = None
        self.head = ( self.head + 1 ) % len(self.array)
        self.size -= 1
        return item

    def peek(self):
        if self.isEmpty():
            raise Exception("Cannot peek into empty queue")
        return self.array[self.head]

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == len(self.array)

    def size(self):
        return self.size


if __name__ == '__main__':
    bq = BoundedQueue(capacity=5)
    bq.enqueue("A")
    bq.enqueue("B")
    bq.enqueue("C")
    bq.enqueue("D")
    bq.enqueue("E")
    print bq.dequeue() == "A"
    bq.enqueue("F")

    print bq.peek() == "B"
    print bq
    print bq.size
    for i in xrange(5):
        print bq.dequeue()

    # should be empty queue
    print bq

    try:
        print bq.peek()
    except Exception as e:
        print str(e)
