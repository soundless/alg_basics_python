#!/usr/bin/env python

class Recursive:
    def isParlindrome(self, s):
        return len(s) <= 1 or ( s[0] == s[-1] and self.isParlindrome(s[1:-1]) )

    def factorial(self, n):
        if n <= 0:
            return 1
        else:
            return n * self.factorial(n - 1)

    def log(self, n):
        if n <= 0:
            raise Exception("cannot get log for negative number")
        elif n == 1:
            return 0
        else:
            return 1 + self.log(n / 2)

    def sumOfDigits(self, n):
        if n < 0:
            return self.sumOfDigits(-n)
        elif n < 10:
            return n
        else:
            return self.sumOfDigits(n // 10) + n % 10

    def fibonnaci(self, n):
        if n < 0:
            raise Exception("No fibnnaci number for negtive numbers")
        elif n <= 1:
            return n
        else:
            return self.fibonnaci(n - 1) + self.fibonnaci(n - 2)


    # greatest common divisor
    def gcd(self, a, b):
        if a < 0 or b < 0:
            raise Exception("No GCD of negative integers")
        if b == 0:
            return a
        else:
            return self.gcd(b, a % b)

if __name__ == '__main__':
    recursive = Recursive()
    print(recursive.gcd(128, 4)) == 4
    print(recursive.gcd(4, 128)) == 4
    print(recursive.isParlindrome("racecar")) == True
    print(recursive.isParlindrome("raceicar")) == False
    print(recursive.factorial(5)) == 120 
    print(recursive.log(32)) == 5
    print(recursive.sumOfDigits(1234)) == 10
    print(recursive.sumOfDigits(-48729)) == 30
    print(recursive.fibonnaci(5)) == 5
