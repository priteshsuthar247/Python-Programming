from scipy.linalg import det

matrix = [[1, 2],
          [3, 4]]

determinant = det(matrix)

print("Matrix:")
for row in matrix:
    print(row)

print(f"\nDeterminant: {determinant}")