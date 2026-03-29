## Counts by 1 to 99
def print_numbers():
    for i in range (0,100):
        print(i)

## Counts by 1 from 5
def print_numbers_from_five_to(end):
    for i in range(5, end):
        print(i)

## Counts down by 1
def count_down(start, end):
    for i in range(start, end, -1):
        print(i)

## Loops number by summing them Numbers
def sum_of_numbers(start, end):
    total = 0
    for i in range(start, end):
        total += i
    return total
