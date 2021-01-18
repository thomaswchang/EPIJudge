from typing import List

from test_framework import generic_test


# [PROBLEM_TYPE=DP] P16.1 PG 246

# Given a final score in American football and a list of type_of_scores, ie (fieldgal->3, safety=2, touchdown=7}
# Return the NUMBER OF COMBINATIONS to get to that score


# Step1: How to recognize a problem is a DP? What is the recurrence?
#   Is DP because each higher score needs the score_optimum - [2, 3, 7]

# Step2: Decide the state. What is the key to the lookup table?
#   final_score; play_type

# Step3: Formulate a relation among the states
#   num_score[j] = num_score[i-1][j]                    //_without_play_type
#                + num_score[i][j-score_of_play_type]   //_with_play_type

# Step4:  Optimize by adding tabulation or memoization
#           0   1   2   3   4   5   6
# 2         A   B   C   D   E   F   G
# 2,3       H   I   J   K   L
# 2,3,7

def num_combinations_for_final_score(final_score: int, # 12
                                     individual_play_scores: List[int]) -> int: #[2, 3, 7

    grid = [ [1] + [0] * final_score ] * len(individual_play_scores)

    for r in range(len(individual_play_scores)):
        for c in range(1, final_score + 1):
            # NICE: interesting syntax; notice we get away from having to define a global variable with if syntax. x = 0 && if x <
            num_scores_without_play = grid[r-1][c] if r>0 else 0

            num_scores_with_play = grid[r][c - individual_play_scores[r]] \
                if c >= individual_play_scores[r] else 0 # do not want negative plays

            grid[r][c] = num_scores_with_play + num_scores_without_play

    return grid[-1][-1]





if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_score_combinations.py',
                                       'number_of_score_combinations.tsv',
                                       num_combinations_for_final_score))
