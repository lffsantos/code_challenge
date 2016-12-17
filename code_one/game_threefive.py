"""
Write a program that prints the numbers from 1 to 100. But for multiples of three
print "Three" instead of the number and for the multiples of five print "Five".
For numbers which are multiples of both three and five print "ThreeFive".
"""
from functools import partial


def multiple_of(base, number):
    return number % base == 0

multiple_of_3 = partial(multiple_of, 3)
multiple_of_5 = partial(multiple_of, 5)


def robot(number):
    say = str(number)
    if multiple_of_3(number) and multiple_of_5(number):
        say = 'ThreeFive'
    elif multiple_of_3(number):
        say = 'Three'
    elif multiple_of_5(number):
        say = 'Five'

    return say


def three_five():
    for n in range(1, 101):
        print(robot(n))


three_five()