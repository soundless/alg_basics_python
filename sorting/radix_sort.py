#!/usr/bin/env python

from math import log

class Solution:
    def radix_sort(self, a, base):
        max_num = max(map(abs, a))
        passes = int(round(log(max_num, base) + 1))
        for digit_num in range(passes):
            buckets = [[] for _ in range(base)]
            for n in a:
                buckets[( abs(n) // base ** digit_num ) % base].append(n)
            a = sum(buckets, [])

        buckets = [[], []]
        for n in a:
            if n < 0:
                buckets[0].append(n)
            else:
                buckets[1].append(n)

        return sum(buckets, [])

if __name__ == '__main__':
    print Solution().radix_sort([4213, 123, -1234, 12, 134, 1, -124], 10)

