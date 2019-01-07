from typing import TypeVar


class Base(object):
    pass

class Subclass(Base):
    pass

def f1(a: Base) -> Base:
    return a

v1 = f1(Subclass())

T = TypeVar('T', bound=Base)
def f2(a: T) -> T:
    return a

v2 = f2(Subclass())

@overload
class vars
method vars