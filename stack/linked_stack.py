#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedStack:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, item):
        temp = self.top
        self.top = Node(item)
        self.top.next = temp
        self._size += 1

    def pop(self):
        if self._size == 0:
            raise Exception("cannot pop from empty stack")
        item = self.top.data
        self.top = self.top.next
        self._size -= 1
        return item

    def peek(self):
        if self._size == 0:
            raise Exception("cannot peek into empty stack")
        return self.top.data

    def size(self):
        return self._size
        
    def isEmpty(self):
        return self._size == 0


if __name__ == '__main__':
    ls = LinkedStack()
    for i in 'ABCDEF':
        ls.push(i)

    print(ls.size()) == 6
    print(ls.pop()) == 'F'
    print(ls.peek()) == 'E'
    print(ls.pop()) == 'E'
    print(ls.peek()) == 'D'
    print(ls.size()) == 4

    for i in xrange(4):
        ls.pop()

    try:
        ls.peek()
    except Exception as e:
        assert str(e) == "cannot peek into empty stack"

    try:
        ls.pop()
    except Exception as e:
        assert str(e) == "cannot pop from empty stack"

    item = Node("abcdefghia0中文字符-ederdfa")
    ls.push(item)
    assert ls.size() == 1
    assert ls.peek() == item
    assert ls.pop() == item  
    assert ls.size() == 0
