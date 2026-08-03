from itertools import permutations

# List of unique letters
letters = ['R', 'E', 'A', 'D', 'W', 'I', 'T', 'S', 'K', 'L']

# Generate all possible digit assignments
for p in permutations(range(10), 10):

    # Assign digits to letters
    R = p[0]
    E = p[1]
    A = p[2]
    D = p[3]
    W = p[4]
    I = p[5]
    T = p[6]
    S = p[7]
    K = p[8]
    L = p[9]

    # Leading letters cannot be zero
    if R == 0 or W == 0 or S == 0:
        continue

    # Convert words into numbers
    READ = R * 1000 + E * 100 + A * 10 + D
    WRITE = W * 10000 + R * 1000 + I * 100 + T * 10 + E
    SKILL = S * 10000 + K * 1000 + I * 100 + L * 10 + L

    # Check the equation
    if READ + WRITE == SKILL:

        print("Solution Found!\n")

        print("READ  =", READ)
        print("WRITE =", WRITE)
        print("SKILL =", SKILL)

        print("\nLetter Assignments")
        print("R =", R)
        print("E =", E)
        print("A =", A)
        print("D =", D)
        print("W =", W)
        print("I =", I)
        print("T =", T)
        print("S =", S)
        print("K =", K)
        print("L =", L)

        break

else:
    print("No solution found.")
