# Map Coloring using CSP

# Map of Australia
graph = {
    "WA": ["NT", "SA"],
    "NT": ["WA", "SA", "Q"],
    "SA": ["WA", "NT", "Q", "NSW", "V"],
    "Q": ["NT", "SA", "NSW"],
    "NSW": ["Q", "SA", "V"],
    "V": ["SA", "NSW"],
    "T": []
}

# Available colors
colors = ["Red", "Green", "Blue"]

# Store the color assigned to each region
solution = {}

# Check whether a color can be assigned
def is_safe(region, color):

    for neighbor in graph[region]:

        if neighbor in solution and solution[neighbor] == color:
            return False

    return True


# CSP using Backtracking
def map_coloring(regions):

    # If all regions are colored
    if len(regions) == 0:
        return True

    # Select the first region
    region = regions[0]

    # Try each color
    for color in colors:

        if is_safe(region, color):

            # Assign color
            solution[region] = color

            # Solve remaining regions
            if map_coloring(regions[1:]):
                return True

            # Backtrack
            del solution[region]

    return False


# List of regions
regions = list(graph.keys())

# Solve the problem
if map_coloring(regions):

    print("Map Coloring Solution:")
    print("----------------------")

    for region in regions:
        print(region, "->", solution[region])

else:
    print("No solution found")
