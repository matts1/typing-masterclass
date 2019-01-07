

# ME: The computer can determine types for us
from typing import TypeVar

a = list(map(str, range(5)))
# ME: But it needs certain info
b = list(range(5))

# ME: Try autocompleting these
a[0]
b[0]

# ME: even when it can determine types for us, typing can still be handy.

i: int = 0
j: bool
if i < 5:
    j = False
else:
    j = i
print(j)

T = TypeVar('T')


# ME: what is the type of this
d = {'a': 0, 'b': 1, 'c': 2}


class MyClass:
    # You can optionally declare instance variables in the class body
    attr: int
    # This is an instance variable with a default value
    charge_percent: int = 100


c: bool
bob = 10
if bob < 10:
    c = True
else:
    c = 0

# ME: *args
# ME: **kwargs

