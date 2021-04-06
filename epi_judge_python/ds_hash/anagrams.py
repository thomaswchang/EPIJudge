from typing import List

from test_framework import generic_test, test_utils
import collections
from typing import DefaultDict, List

# PROBLEM_TYPE=HASH
# PG 165
# Given a list of strings, return a list of grouped anagrams


def find_anagrams(dictionary: List[str]) -> List[List[str]]:
    infos: DefaultDict[str, List[str]] = collections.defaultdict(list)

    for s in dictionary:
        infos[''.join(sorted(s))].append(s)

    return [
        grp for grp in infos.values()
        if len(grp) >= 2
    ]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'anagrams.py',
            'anagrams.tsv',
            find_anagrams,
            comparator=test_utils.unordered_compare))
