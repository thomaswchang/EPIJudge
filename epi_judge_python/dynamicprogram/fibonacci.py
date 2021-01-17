from test_framework import generic_test


def fibonacci(n: int) -> int:

    def fib_inefficient(n) -> int:
        if n <= 1:
            return n
        return fib_inefficient(n-1) + fib_inefficient(n-2) # if look at call graph, will call fib_inefficient multiple times; wasting runtime and space (due to call stack)

    def fib_dp():
        if n<= 1:
            return n

        r_minus_2, r_minus_1 = 0, 1

        for i in range(1, n):
            tmp = r_minus_1 + r_minus_2
            r_minus_2, r_minus_1 = r_minus_1, tmp

        return r_minus_1

    return fib_dp()


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('fibonacci.py', 'fibonacci.tsv',
                                       fibonacci))
