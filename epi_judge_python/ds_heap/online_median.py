from typing import Iterator, List

from test_framework import generic_test

import heapq

# [PROBLEM_TYPE=HEAP] 10.5 P143

# Compute the running median of a sequence

# Given a sequence of numbers, return the median

def online_median(sequence: Iterator[int]) -> List[float]:
    min_heap: List[int] = []   # Has the higher numbers
    max_heap: List[int] = []   # Has the lower numbers

    # Constraints
    # len(min_heap) = { len(max_heap) +1, len(max_heap) }

    result = []

    for n in sequence:
        heapq.heappush(max_heap, -n)

        if len(max_heap) > len(min_heap):
            heapq.heappush(min_heap, -heapq.heappop(max_heap))

        result.append(0.5 * (-max_heap[0] + min_heap[0]) if len(max_heap) == len(min_heap) else min_heap[0])

    return result


def online_median_wrapper(sequence):
    return online_median(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('online_median.py', 'online_median.tsv',
                                       online_median_wrapper))
