# Python program to implement Alpha-Beta Pruning Algorithm

import math

# Alpha-Beta function
def alphabeta(depth, nodeIndex, isMax, values, alpha, beta, height):

    # Base case: If leaf node is reached
    if depth == height:
        return values[nodeIndex]

    if isMax:
        best = -math.inf

        # Left child
        best = max(best, alphabeta(depth + 1, nodeIndex * 2,
                                   False, values, alpha, beta, height))
        alpha = max(alpha, best)

        # Pruning
        if beta <= alpha:
            return best

        # Right child
        best = max(best, alphabeta(depth + 1, nodeIndex * 2 + 1,
                                   False, values, alpha, beta, height))
        alpha = max(alpha, best)

        return best

    else:
        best = math.inf

        # Left child
        best = min(best, alphabeta(depth + 1, nodeIndex * 2,
                                   True, values, alpha, beta, height))
        beta = min(beta, best)

        # Pruning
        if beta <= alpha:
            return best

        # Right child
        best = min(best, alphabeta(depth + 1, nodeIndex * 2 + 1,
                                   True, values, alpha, beta, height))
        beta = min(beta, best)

        return best


# Main Program
values = [3, 5, 2, 9, 12, 5, 23, 23]

height = 3

result = alphabeta(0, 0, True, values, -math.inf, math.inf, height)

print("The optimal value is:", result)
