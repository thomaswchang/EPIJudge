from test_framework import generic_test

# [PROBLEM_TYPE=STACKQUEUE]

# Evaluate RPN expressions (pg 102)
# str = '1729,3,+'
def evaluate(expression: str) -> int:

    intermediate_results = [] #: List[int]
    delimiter = ','
    operators = {
        '+': lambda y, x: x+y,   # order of parameter y, x matters. For div and sub, rpn stack latest eleemnt is bigger
        '-': lambda y, x: x-y,
        '*': lambda y, x: x*y,
        '/': lambda y, x: x//y
    }

    for token in expression.split(delimiter):
        if token in operators:
            intermediate_results.append(
                operators[token](intermediate_results.pop(), intermediate_results.pop())
            )
        else:
            intermediate_results.append(int(token))

    return intermediate_results[-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv',
                                       evaluate))
