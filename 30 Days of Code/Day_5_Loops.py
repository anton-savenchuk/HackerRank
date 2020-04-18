"""Objective
In this challenge, we're going to use loops to help us do some simple
math. Check out the Tutorial tab to learn more.

Task
Given an integer, n, print its first 10 multiples. Each multiple
n x i(where 1 <= i <= 10) should be printed on a new line in the form:
n x i = result.
"""


if __name__ == '__main__':
    n = int(input())
    for i in range(1, 11):
        print(f'{n} x {i} = {n * i}')
