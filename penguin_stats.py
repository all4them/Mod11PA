# penguin_stats.py
# Tonya Brooks
# 11/15/2026
# Functions for calculating and classifying penguin statistics


# Calculate a species' percentage of the total observations.
def calculate_percentage(count, total):
    return count / total * 100


# Classify a species group according to its percentage.
def classify_species(percent):
    if percent < 25:
        return "small"
    elif percent < 40:
        return "medium"
    else:
        return "large"


# Determine whether a species is largest, smallest, or middle-sized.
def get_position_description(
        selected_species, largest_species, smallest_species):

    if selected_species == largest_species:
        return "largest"
    elif selected_species == smallest_species:
        return "smallest"
    else:
        return "middle-sized"
