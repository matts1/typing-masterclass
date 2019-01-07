

# ME: The computer can determine types for us
from typing import TypeVar

a = list(map(str, range(5)))
# ME: But it needs certain info
b = list(range(5))

# ME: Try autocompleting these
a[0]
b[0]

# ME: what is the type of this
d = {'a': 0, 'b': 1, 'c': 2}


