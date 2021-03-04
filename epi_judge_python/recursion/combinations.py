from typing import List

from test_framework import generic_test, test_utils

# [PROBLEM_TYPE=RECURSION] P15.6 PG233

# Generate all subsets of size k.  Given a list of size n, generate ALL subsets of size k from the list
# Ex: n=3, k=2 -> { (1,2), (1,3), (2,1), ... (3,4) (3,5), (4,5) }

""" 
    i=1: 
        j:       2,      3,      4,      5
            (2,[1])      

    i=2
        j:      3,      4,      5
            (3,[1,2])
        
    i=3
        j:      4,      5 
            S[1,2]        
        

    i=4
        j:      5

"""

def combinations(n: int, k: int) -> List[List[int]]:
    def recurse(offset, curr_candidate):
        if len(curr_candidate) == k:
            solutions.append(curr_candidate.copy())
            return

        # How much do you not cover from the end
        remaining = k - len(curr_candidate)
        i = offset

        while i <= n and remaining <= n -i +1 :
            recurse(i+1, curr_candidate + [i])
            i += 1

    solutions: List[List[int]] = []
    recurse(1, [])      # Reframe the problem from base 1 to make it easier
    return solutions

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'combinations.py',
            'combinations.tsv',
            combinations,
            comparator=test_utils.unordered_compare))
