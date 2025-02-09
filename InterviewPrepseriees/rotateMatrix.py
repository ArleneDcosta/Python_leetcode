def rotate_matrix(matrix):
    # Get the number of rows and columns
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Create an empty matrix for the rotated result
    rotated = [[0] * rows for _ in range(cols)]

    # Fill the rotated matrix
    for i in range(rows):
        for j in range(cols):
            rotated[j][rows - 1 - i] = matrix[i][j]

    return rotated

# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

rotated = rotate_matrix(matrix)
for row in rotated:
    print(row)


if __name__ == '__main__':
    rotate_matrix([[1,2,3],[4,5,6]])