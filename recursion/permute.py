#!/usr/bin/env python

class Solution:
    def permute(self, s):
        results = []
        self.helper("", s, results)
        return results

    def helper(self, prefix, leftOver, results):
        if not leftOver:
             results.append(prefix)
        
        for i in xrange(len(leftOver)):
            self.helper(prefix + leftOver[i], leftOver[:i] + leftOver[i+1:],
                    results)

if __name__ == '__main__':
    print(Solution().permute("hi"))
    print(Solution().permute("how"))
    print(Solution().permute("hello"))
