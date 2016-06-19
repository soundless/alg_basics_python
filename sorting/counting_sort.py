#!/usr/bin/env python

# Time:  O(n + k)

class Solution:
    # k means value range from 0 to k
    def countingSort(self, a, k):
        counter = [0] * (k + 1)
        for i in a:
            counter[i] += 1

        j = 0
        for i in range(len(counter)):
            while counter[i] > 0:
                a[j] = i
                j += 1
                counter[i] -= 1
        return a

if __name__ == '__main__':
    print(Solution().countingSort([1, 2, 3, 1, 3, 2, 0, 1, 3, 2], 3))
    print(Solution().countingSort([0, 1, 2, 3], 3))

