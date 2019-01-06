from typing import TypeVar, Dict


# NOTE: list -> typevar
# NOTE: int -> str -> union -> typevar
# NOTE: explain union returning union issues
def get_only(l):
    return l[0]


get_only([1, 2, 3])
get_only(['a', 'b', 'c'])
get_only([1, 'a'])  # This probably shouldn't be allowed. Explain why
get_only([])  # what happens here


# NOTE: list -> iterable
# NOTE: what's wrong with this function? If you spot it, keep it to yourself for now
def my_sum(items, start):
    for item in items:
        start = start + item


my_sum([1, 2, 3], 0)
my_sum([1.5, 2.5, 3.5], 0.5)
my_sum([1.5, 2.5, 3.5], 0)  # Should we allow this kind of thing? Discuss.
my_sum(map(int, ['1', '2', '3']), 0)
my_sum(['a', 'b', 'c'], '')  # this will work, but what if we only want our function to work on numbers.
my_sum([1, 2, 3], 'a')  # This should obviously break, but what if we could know about it at compile time.


# NOTE: show off callable
def my_reduce(items, start, join_function):
    for item in items:
        start = join_function(start, item)
    return start


class MyClass:
    # You can optionally declare instance variables in the class body
    attr: int
    # This is an instance variable with a default value
    charge_percent: int = 100


n: int = my_reduce([1, 2, 3], 0, lambda x, y: x + y)

a: bool
bob = 10
if bob < 10:
    a = True
else:
    a = 0

b: Dict[str, int] = {'a': 0, 'b': 1, 'c': 2}

if __name__ == '__main__':
    print(get_only([]))
