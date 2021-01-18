from test_framework import generic_test

# [PROBLEM_TYPE=DP]
# Step1: How to recognize a problem is a DP? What is the recurrence?

# Step2: Decide the state. What is the key to the lookup table?

# Step3: Formulate a relation among the states

# Step4:  Optimize by adding tabulation or memoization

def compute_binomial_coefficient(n: int, k: int) -> int:
    # TODO - you fill in here.
    return 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('binomial_coefficients.py',
                                       'binomial_coefficients.tsv',
                                       compute_binomial_coefficient))
