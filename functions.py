# ME: Explain what types are
# ME: How can we work out the type of something -> type inferences
# ME: Use standard library functions as examples to quiz students

# ME: list -> union -> explain union returning union issues
# ME: explain that you can still run the code if it doesn't type check correctly
from numbers import Number
from typing import TypeVar, List, Optional, Union, Iterator, Iterable, Callable, \
    overload

T = TypeVar('T')


def get_only(l):
    return l[0]


a = get_only([1, 2, 3])
b = get_only(['a', 'b', 'c'])
# ME: explain why this is a bad idea, shouldn't be allowed, alternatives.
c = get_only([1, 'a'])
# ME: what happens here
# d = get_only([])
# This is why the above is important
# int_list = [1]
# int_list.pop()
# e = get_only(int_list)

# ME: should we allow things like this.
f = get_only({0: 'hello'})


# ME: list -> iterable
# ME: Ask what's wrong with this function?
# STUDENTS: If you spot it, keep it to yourself for now
def my_sum(items, start):
    for item in items:
        start = start + item


my_sum([1, 2, 3], 0)
my_sum([1.5, 2.5, 3.5], 0.5)
# Should we allow this kind of thing? Discuss.
my_sum([1.5, 2.5, 3.5], 0)
my_sum(map(int, ['1', '2', '3']), 0)
# ME: This will work, but explain numeric before this.
my_sum(['a', 'b', 'c'], '')


# This should break, but what if we could know about it at compile time.
# my_sum([1, 2, 3], 'a')


# ME: show off callable
def my_reduce(items: Iterable[T], start: T, joiner: Callable[[T, T], T]):
    for item in items:
        start = joiner(start, item)
    return start


n = my_reduce([1.0, 2.0, 3.0], 0.0, lambda x, y: x + y)


def my_sum2(*args):
    return sum(args)


my_sum2(1, 2.0, 3)
my_sum2(1.0, 2.0, 3.0)
my_sum2(1.0, 2, 3.0)


def most_common_name(**kwargs):
    return max(kwargs, key=kwargs.get)


# Don't try this at home, kids. This is not what you use keyword arguments for.
most_common_name(alice=5, bob=4, eve=3)
