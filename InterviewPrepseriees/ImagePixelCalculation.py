
def calculate_mean(image, radius, r, c):
    # List of directions to calculate neighbors
    directions = [[-1, 1], [1, 0], [1, 1], [0, 1], [1, -1], [0, -1], [-1, 0], [-1, -1]]
    mean_values = []

    # Loop through the radius around the pixel (r, c)
    # for i in range(-radius, radius + 1):
    #     for j in range(-radius, radius + 1):
    #         if i == 0 and j == 0:
    #             continue
    #         if 0 <= r + i < len(image) and 0 <= c + j < len(image[0]):
    #             mean_values.append(image[r + i][c + j])

    for i in range(0,radius):
        for direction in directions:
            if 0 <= r+i+direction[0] < len(image) and 0 <= c+i+direction[1] < len(image[0]):
                mean_values.append(image[r+i+direction[0]][c+i+direction[1]])

    # Return the mean of collected values
    return sum(mean_values) / len(mean_values)

def solution(image, radius):
    res = [[0 for _ in range(len(image[0]))] for _ in range(len(image))]

    for i in range(len(image)):
        for j in range(len(image[0])):
            res[i][j] = int(calculate_mean(image, radius, i, j) + image[i][j]) // 2

    return res

if __name__ == '__main__':
    print(solution([[9,6],[3,0]],1))