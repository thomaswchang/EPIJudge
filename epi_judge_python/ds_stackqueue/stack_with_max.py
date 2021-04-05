from test_framework import generic_test
from test_framework.test_failure import TestFailure

# [PROBLEM_TYPE=STACKQUEUE]

import collections
from dataclasses import dataclass


@dataclass
class ElementWithCachedMax:
    value: float
    max: float


# Implement a stack to include a max operation, which returns the maximum value stored in the stack
# Each element contains a reference to its max element.
class Stack:
    #ElementWithCachedMax = collections.namedtuple('ElemenWithCachedMax', ('value', 'max'))

    def __init__(self) -> None:
        #self._cache : List[Stack.ElementWithCachedMax] = []
        self._cache: List[ElementWithCachedMax] = []

    def empty(self) -> bool:
        return len(self._cache) == 0

    def max(self) -> int:
        return self._cache[-1].max

    def pop(self) -> int:
        return self._cache.pop().value

    def push(self, x: int) -> None:
        self._cache.append( ElementWithCachedMax(x, x if self.empty() else  max(x, self.max())))
        return


def stack_tester(ops):
    try:
        s = Stack()

        for (op, arg) in ops:
            if op == 'Stack':
                s = Stack()
            elif op == 'push':
                s.push(arg)
            elif op == 'pop':
                result = s.pop()
                if result != arg:
                    raise TestFailure('Pop: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'max':
                result = s.max()
                if result != arg:
                    raise TestFailure('Max: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'empty':
                result = int(s.empty())
                if result != arg:
                    raise TestFailure('Empty: expected ' + str(arg) +
                                      ', got ' + str(result))
            else:
                raise RuntimeError('Unsupported stack operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('stack_with_max.py',
                                       'stack_with_max.tsv', stack_tester))
