"""Objective
Today, we're learning about Key-Value pair mappings using a Map or
Dictionary data structure.

Task
Given n names and phone numbers, assemble a phone book that maps friends' names
to their respective phone numbers. You will then be given an unknown
number of names to query your phone book for. For each name queried,
print the associated entry from your phone book on a new line in the
form name=phoneNumber; if an entry for name is not found, print
Not found instead.

Note: Your phone book should be a Dictionary/Map/HashMap data structure.
"""


# Enter your code here. Read input from STDIN. Print output to STDOUT
def get_phone_book(n):
    phone_book = {}
    for x in range(n):
        line = input().strip().split(' ')
        name = line[0]
        number = line[1]
        phone_book[name] = number
    return phone_book


if __name__ == '__main__':
    number_of_entries = int(input())
    phone_book = get_phone_book(number_of_entries)

    while True:
        try:
            name = input()
            if name in phone_book.keys():
                print(name, '=', phone_book[name], sep='')
            else:
                print('Not found')
        except EOFError as eof:
            break
