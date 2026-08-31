import math

# Training data
data = [
    ["Sunny", "Hot", "No"],
    ["Sunny", "Hot", "No"],
    ["Overcast", "Hot", "Yes"],
    ["Rain", "Mild", "Yes"],
    ["Rain", "Cool", "Yes"],
    ["Rain", "Cool", "No"],
    ["Overcast", "Cool", "Yes"],
    ["Sunny", "Mild", "No"],
    ["Sunny", "Cool", "Yes"],
    ["Rain", "Mild", "Yes"]
]

# Calculate entropy
def entropy(data):
    total = len(data)
    yes = sum(1 for row in data if row[-1] == "Yes")
    no = total - yes

    result = 0

    if yes > 0:
        p = yes / total
        result -= p * math.log2(p)

    if no > 0:
        p = no / total
        result -= p * math.log2(p)

    return result


# Calculate information gain
def information_gain(data, index):
    total_entropy = entropy(data)
    values = set(row[index] for row in data)

    weighted_entropy = 0

    for value in values:
        subset = [row for row in data if row[index] == value]
        weighted_entropy += (len(subset) / len(data)) * entropy(subset)

    return total_entropy - weighted_entropy


# Find the best attribute
best_attribute = -1
best_gain = -1

for i in range(2):
    gain = information_gain(data, i)

    print("Information Gain for attribute", i + 1, "=", round(gain, 3))

    if gain > best_gain:
        best_gain = gain
        best_attribute = i


# Display the decision tree
attributes = ["Weather", "Temperature"]

print("\nDecision Tree")
print("Root Attribute:", attributes[best_attribute])

values = set(row[best_attribute] for row in data)

for value in values:
    subset = [row for row in data if row[best_attribute] == value]

    yes = sum(1 for row in subset if row[-1] == "Yes")
    no = len(subset) - yes

    if yes >= no:
        result = "Yes"
    else:
        result = "No"

    print(attributes[best_attribute], "=", value, "->", result)


# Prediction
print("\nPrediction:")
test = ["Sunny", "Cool"]

if test[best_attribute] == "Sunny":
    prediction = "No"
elif test[best_attribute] == "Overcast":
    prediction = "Yes"
else:
    prediction = "Yes"

print(test, "->", prediction)
