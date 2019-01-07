from typing import TypeVar, Optional, Generic


class Character(object):
    name: Optional[str]

    def __init__(self):
        self.name = None

    def set_name(self, name):
        self.name = name


class Player(Character):
    pass


def f1(a: Character) -> Character:
    return a


v1 = f1(Player())

C = TypeVar('C', bound=Character)


def f2(a: C) -> C:
    return a


v2 = f2(Player())

T = TypeVar('T')


class Tree(Generic[T]):
    def __init__(self, value: T, left: Optional['Tree[T]'] = None,
            right: Optional['Tree[T]'] = None):
        self.left = left
        self.right = right
        self.value = value


Tree(1, Tree(0), Tree(1))
# It can work out that this is invalid for you!
Tree(1, Tree(0), Tree(1.0))

# If we get to this stage, show off python stubs.
