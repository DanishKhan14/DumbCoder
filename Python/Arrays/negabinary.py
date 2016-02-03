#!/usr/bin/python

def negabase(number, base):
    if 0 == number:
        return '0'

    digits = list()
    while 0 != number:
        number, remainder = divmod(number, base)

        if remainder < 0:
            # N == b*q + (b - b) + r == b*(q + 1) + (r - b)
            number, remainder = number + 1, remainder -	base

        digits.append(str(remainder))

    return ''.join(digits[::-1]) if len(digits) else '0'


def solution(number):
    return negabase(number, -2)


print solution(-15)
print solution(10)
print solution(-5)

"""

assert solution(-15) =='110001'
assert solution(10) ==  '11110'
assert solution(-5) == '1111'
"""