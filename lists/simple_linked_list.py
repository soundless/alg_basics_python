#!/usr/bin/env python

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    
    def __repr__(self):
        return "{}".format(self.data)


class SimpleLinkedList(object):
    def __init__(self):
        self.head = Node(None)
        self._size = 0
        self.changes = 0
        self.head.next = self.head.prev = self.head

    def nodeAt(self, index):
        if index < 0 or index > self._size:
            raise Exception("index is out of bound")
        node = self.head
        for i in xrange(index + 1):
            node = node.next
        return node

    def addBefore(self, item, node):
        newNode = Node(item)
        newNode.next = node
        newNode.prev = node.prev
        newNode.prev.next = newNode
        newNode.next.prev = newNode
        self._size += 1
        self.changes += 1

    def remove(self, node):
        if not node or node is self.head:
            raise Exception("No such element")
        node.prev.next = node.next
        node.next.prev = node.prev
        self._size += 1
        self.changes += 1

    def size(self):
        return self._size

    def addFirst(self, item):
        self.addBefore(item, self.head.next)

    def addLast(self, item):
        self.addBefore(item, self.head)

    def add(self, index, item):
        if index == self._size:
            self.addLast(item)
        else:
            self.addBefore(item, self.nodeAt(index))

    def removeAt(self, index):
        self.remove(self.nodeAt(index))

    def indexOf(self, item):
        index = 0
        node = self.head.next
        while node and node is not self.head:
            if node.data == item:
                return index
            index += 1
            node = node.next
        return -1

    def __repr__(self):
        values = []
        node = self.head
        while node.next is not self.head:
            values.append(node.next.data)
            node = node.next
        return str(values)

    def next(self):
        pass

    def hasNext(self):
        pass


if __name__ == '__main__':
    sll = SimpleLinkedList()
    sll.addFirst(0)
    for i in xrange(1, 11):
        sll.add(i, i)
    sll.addLast(11)
    print sll.size()
    print sll.indexOf(5)
    print sll.nodeAt(9)
    sll.removeAt(9)
    print repr(sll)
    print sll.nodeAt(9)
