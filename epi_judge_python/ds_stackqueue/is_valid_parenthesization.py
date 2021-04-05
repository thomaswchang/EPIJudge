from test_framework import generic_test

# [PROBLEM_TYPE=STACKQUEUE]

# pg 103: P 8.3
# well formed = [()[]()]


def is_well_formed(s: str) -> bool:
    lookup = {'(': ')', '[': ']', '{': '}'}
    left_chars = []

    for c in s:
        if c in lookup:
            left_chars.append(c)
        else: # right chars
            if not left_chars or lookup[left_chars.pop()] != c:
                return False
    return not left_chars


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_parenthesization.py',
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
