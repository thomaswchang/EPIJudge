from test_framework import generic_test

# TYPE=PRIMITIVETYPES

def is_palindrome_number(x: int) -> bool:
    # TODO - you fill in here.
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_number_palindromic.py',
                                       'is_number_palindromic.tsv',
                                       is_palindrome_number))
