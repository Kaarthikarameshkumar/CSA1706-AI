import random
import math

# Sigmoid activation function
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# Training data (AND operation)
X = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]

Y = [0, 0, 0, 1]

# Initialize weights randomly
w1 = random.random()
w2 = random.random()
b = random.random()

# Learning rate
lr = 0.5

# Training
for epoch in range(10000):

    for i in range(len(X)):

        x1 = X[i][0]
        x2 = X[i][1]
        target = Y[i]

        # Feed Forward
        z = (x1 * w1) + (x2 * w2) + b
        output = sigmoid(z)

        # Error
        error = target - output

        # Backpropagation
        derivative = output * (1 - output)

        w1 = w1 + lr * error * derivative * x1
        w2 = w2 + lr * error * derivative * x2
        b = b + lr * error * derivative

# Testing
print("Feed Forward Neural Network")
print("----------------------------")
print("Predictions:")

for i in range(len(X)):

    x1 = X[i][0]
    x2 = X[i][1]

    z = (x1 * w1) + (x2 * w2) + b
    output = sigmoid(z)

    if output >= 0.5:
        prediction = 1
    else:
        prediction = 0

    print(X[i], "->", prediction)

print("----------------------------")
print("Training Completed")
