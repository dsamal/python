__author__ = 'DEBASISH'

def str_reverse(s):
    r = ''
    for v in s:
        r=v+r
    return r

def str_reverse_quick(s):
    return s[::-1]


def find_digit(s):
    return "".join([x for x in s if x.isdigit()])


def exponent(x, n):
    return x**n

