from typing import List

from test_framework import generic_test, test_utils

# [PROBLEM_TYPE=RECURSION]

# We use a tuple, the index represents the phone number
MAPPING = ('0', '1', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ')

def phone_mnemonic(phone_number: str) -> List[str]:
    def helper(digit):
        if digit == len(phone_number): # don't need +1 because we are zero based
            results.append(''.join(curr))
        else:
            # BUG: for c in MAPPING[digit]:
            for c in MAPPING[int(phone_number[digit])]:
                curr[digit] = c
                helper( digit+1)

    # we are reusing the this variable to store the current candidate; don't waste space
    curr = [0] * len(phone_number)
    results: List[str] = []
    helper(0)
    return results


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'phone_number_mnemonic.py',
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))
