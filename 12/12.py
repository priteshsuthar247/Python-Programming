import numpy as np

scores = np.array([
    [85, 78, 92],
    [70, 88, 95],
    [95, 90, 85],
    [60, 65, 70],
    [80, 82, 78],
])

mean_scores = np.mean(scores, axis=0)

above_average_students = scores[(scores[:, 0] > mean_scores[0]) | 
                                 (scores[:, 1] > mean_scores[1]) | 
                                 (scores[:, 2] > mean_scores[2])]

print("Mean Scores:")
print(mean_scores)

print("\nScores:")
print(scores)

print("\nAbove Average Students:")
print(above_average_students)