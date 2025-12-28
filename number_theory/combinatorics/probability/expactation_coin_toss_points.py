"""
    Calculate the expected score of tossing 2 coins.

    Problem:
        Toss 2 fair coins. Assign points as follows:
            - Head (H) = 2 points
            - Tail (T) = 0 points

    Solution:
        Possible outcomes and their scores:
            - HH -> 4 points
            - HT -> 2 points
            - TH -> 2 points
            - TT -> 0 points

        Each outcome has probability 1/4. The expected value is:

            E[X] = 4*(1/4) + 2*(1/4) + 2*(1/4) + 0*(1/4) = 2

    Returns:
        float: Expected score of tossing 2 coins, which is 2.
    """
    
scores = [4,2,2,0]
prob = 1/4

expected_score = sum(s*prob for s in scores)
print(f"Expected Score: {expected_score}")
