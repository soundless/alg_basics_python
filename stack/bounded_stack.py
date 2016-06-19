#!/usr/bin/env python

class BoundedStack:
    def __init__(self, capacity=10):
        self.__capacity = capacity
        self.__size = 0
        self.__array = [None for i in xrange(capacity)]

    def push(self, item):
        if self.__size == self.__capacity:
            raise Exception("cannot push to full stack")
        self.__array[self.__size] = item
        self.__size += 1

    def pop(self):
        if self.__size == 0:
            raise Exception("cannot pop from empty stack")
        item = self.__array[self.__size - 1]
        self.__size -= 1
        self.__array[self.__size] = None
        return item

    def peek(self):
        if self.__size == 0:
            raise Exception("cannot peek to empty stack")
        return self.__array[self.__size - 1]

    def size(self):
        return self.__size

    def isEmpty(self):
        return self.__size == 0


if __name__ == '__main__':
    bs = BoundedStack(capacity=5)

    # stack is empty on construction
    assert bs.isEmpty()

    # stack size is 0 on construction
    assert bs.size() == 0

    for i in 'ABCDE':
        bs.push(i)

    # after n pushes to an empty stack, n > 0
    # the stack is not empty and its size is n  
    print(bs.size()) == 5

    try:
        bs.push("F")
    except Exception as e:
        print(str(e)) == "cannot push to full stack"

    print(bs.pop()) == 'E'
    print(bs.size()) == 4
    print(bs.peek()) == 'D'
    print(bs.size()) == 4

    bs.push("F")
    print(bs.peek()) == 'F'

    for i in xrange(5):
        bs.pop()

    print(bs.size()) == 0
    print(bs.isEmpty()) == True
   
    try:
        bs.peek()
    except Exception as e:
        print(str(e)) == "cannot peek to empty stack" 

    try:
        bs.pop()
    except Exception as e:
        print(str(e)) == "cannot pop from empty stack"