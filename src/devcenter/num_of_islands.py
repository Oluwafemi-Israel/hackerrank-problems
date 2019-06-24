# Given a matrix of 1s and 0s, return the number of "islands" in the matrix. A 1 represents land and 0 represents
# water, so an island is a group of 1s that are neighboring whose perimeter is surrounded by water.
#
# For example, this matrix has 4 islands.
#
# 1 0 0 0 0
# 0 0 1 1 0
# 0 1 1 0 0
# 0 0 0 0 0
# 1 1 0 0 1
# 1 1 0 0 1

# https://www.youtube.com/watch?v=CLvNe-8-6s8


def change_adjacent_lands_to_water(matrix, row, col):
    if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[row]) or matrix[row][col] == 0:
        return

    # change land to water
    matrix[row][col] = 0

    # previous row
    change_adjacent_lands_to_water(matrix, row - 1, col - 1)  # north-west
    change_adjacent_lands_to_water(matrix, row - 1, col)  # north
    change_adjacent_lands_to_water(matrix, row - 1, col + 1)  # north-east

    # current row
    change_adjacent_lands_to_water(matrix, row, col - 1)  # west
    change_adjacent_lands_to_water(matrix, row, col + 1)  # east

    # next row
    change_adjacent_lands_to_water(matrix, row + 1, col - 1)  # south-west
    change_adjacent_lands_to_water(matrix, row + 1, col)  # south
    change_adjacent_lands_to_water(matrix, row + 1, col + 1)  # south-east


def num_of_islands(matrix):
    islands = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            # when we find some land
            if matrix[row][col] == 1:
                # increment the island count
                islands += 1
                # recursively change adjacent lands to water
                change_adjacent_lands_to_water(matrix, row, col)
    return islands


if __name__ == "__main__":
    assert (
            num_of_islands([
                [1, 0, 0, 0, 0],
                [0, 0, 1, 1, 0],
                [0, 1, 1, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 1, 0, 0, 1],
                [1, 1, 0, 0, 1]
            ]) == 4
    )
