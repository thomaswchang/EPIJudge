from test_framework import generic_test

# [PROBLEM_TYPE=STRING]

def rabin_karp(t: str, s: str) -> int:
    # TODO - you fill in here.
    return 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('substring_match.py',
                                       'substring_match.tsv', rabin_karp))
