#!/usr/bin/env python

from random import randint


class Sorter(object):
    # pick the smallest one and put in the right place
    def selection(self, a):
        # Time:  O(n^2)
        # Space: O(1) 
        n = len(a)
        for i in range(n-1):
            small = i
            for j in range(i+1, n):
                if a[j] < a[small]:
                    small = j
            if i != small:
                a[small], a[i] = a[i], a[small]
        return a

    # like cards, move the position up for inserting the new card
    def insertion(self, a):
        # Time:  O(n^2) - linear if already sorted
        # Space: O(1)
        n = len(a)
        for i in range(1, n):
            current = a[i]
            j = i
            while j > 0 and current < a[j]:
                a[j] = a[j-1]
                j -= 1
            a[j] = current
        return a

    def bubble(self, a):
        # Time: O(n^2)
        # Space: O(1)
        swapped = False
        n = len(a)
        for i in range(n-1):
            for j in range(i+1, n):
                if a[i] > a[j]:
                    a[i], a[j] = a[j], a[i]
                    swapped = True
            if not swapped:
                return a

    def gnome(self, a):
        for i in range(len(a)):
            if i == 0 or a[i-1] < a[i]:
                i += 1
            else:
                a[i-1], a[i] = a[i], a[i-1]
                i -= 1
        return a

    def shell(self, a):
        n = len(a) // 2
        while n > 0:
            for i in range(n):
                self.shell_sort_helper(a, i, n)
            n //= 2 
        return a

    def shell_sort_helper(self, a, start, gap):
        for j in range(start + gap, len(a), gap):
            cur = a[j]
            pos = j
            while pos >= gap and a[pos - gap] > cur:
                a[pos] = a[pos - gap]
                pos -= gap
            a[pos] = cur

    def quick(self, a):
        less = []
        equal = []
        greater = []
        n = len(a)
        if n > 1:
            pivot = a[random.randint(n)]
            for i in a:
                if i < pivot:
                    less.append(i)
                elif i == pivot:
                    equal.append(i)
                else:
                    greater.append(i)
        return self.sort(less) + equal + self.sort(greater)

    def heap(self, a):
        end = len(a) - 1
        self.heapify(a, end)
        while end >= 0:
            a[0], a[end] = a[end], a[0]
            end -= 1
            self.siftDown(a, 0, end)
        return a

    def heapify(self, a, end):
        start = (end - 1) /2
        while start >= 0:
            self.siftDown(a, start, end)
            start -= 1

    def siftDown(self, a, start, end):
        while start * 2 + 1 <= end:
            child = start * 2 + 1
            if child < end and a[child] < a[child+1]:
                child += 1
            if a[start] < a[child]:
                a[start], a[child] = a[child], a[start]
                start = child
            else:
                return

    def merge(self, a):
        if len(a) > 1:
            mid = len(a) // 2
            left = a[:mid]
            right = a[mid:]

            self.merge(left)
            self.merge(right)

            i = j = k = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    a[k] = left[i]
                    i += 1
                else:
                    a[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                a[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                a[k] = right[j]
                j += 1
                k += 1

        return a

    # Non-negative sort
    # Time:  O(n + k)
    # Space: O(n + k)
    def counting(self, a):
        from collections import defaultdict
        d = defaultdict(int)
        for n in range(len(a)):
            d[n] += 1
       
        result = []
        for i in d:
            result += [i] * d[i] 
        return result

    # Time : O(ns)
    # Space: O(n)
    def radix(self, a):
        base = 10
        stop = False
        factor = 1

        while not stop:
            stop = True
            buckets = [list() for _ in range(base)]
            for n in a:
                reminder = (n // base ** factor) % base
                buckets[reminder].append(n)
                if stop and reminder > 0:
                    stop = False
            a = sum(buckets, [])
            factor += 1
        return a


if __name__ == '__main__':
    a = []
    global max
    max = 10000
    for i in xrange(100):
        a.append(randint(0, max))

    print("Selection", Sorter().selection(a))
    print("Insertion", Sorter().insertion(a))
    print("Bubble", Sorter().bubble(a))
    print("Gnome", Sorter().gnome(a))
    print("Shell", Sorter().shell(a))
    print("Quick", Sorter().shell(a))
    print("Heap", Sorter().heap(a))
    print("Merge", Sorter().merge(a))
    print("Radix", Sorter().radix(a))
