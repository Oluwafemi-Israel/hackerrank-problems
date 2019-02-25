# https://www.hackerrank.com/challenges/the-quickest-way-up/problem


def construct_board(row_width, end):
    k = 0
    board = []
    for i in range(row_width, end + 1, row_width):
        row = []
        for k in range(k + 1, i + 1):
            row.append(k)
        board.append(row)
    return board


def add_sliders(board, sliders):
    for slider in sliders:
        row = slider[0] // 10
        column = (slider[0] % 10) - 1
        board[row][column] = slider[1]

    return board


def quickestWayUp(ladders, snakes):
    row_width, board_end = 10, 100
    board = construct_board(row_width, board_end)
    board = add_sliders(board, ladders)
    board = add_sliders(board, snakes)
    print("Board", board)

    source = board[0][0]
    levels = {source: 0}

    queue = []
    visited = [False] * board_end

    queue.append(source)
    visited[source - 1] = True

    while queue:
        source = queue.pop(0)
        print ("Visiting", source)
        current_node_row = source // 10
        current_node_column = (source % 10) - 1
        current_level = levels[source]

        for i in range(1, 7):
            if (current_node_row + 1) <= 10:
                if (current_node_column + i) > 9 and (current_node_row + 1) < 10:
                    adjacent_node = board[current_node_row + 1][(current_node_column + i) - 10]
                elif (current_node_column + i) > 9 and (current_node_row + 1) == 10:
                    continue
                else:
                    adjacent_node = board[current_node_row][current_node_column + i]
            else:
                continue

            if not visited[adjacent_node - 1]:
                queue.append(adjacent_node)
                visited[adjacent_node - 1] = True
                levels[adjacent_node] = current_level + 1

        print("Levels", levels)

    if levels.get(100):
        return levels[100]
    else:
        return -1


if __name__ == "__main__":
    quickestWayUp(
        [[32, 62], [42, 68], [12, 98]],
        [[95, 13], [97, 25], [93, 37], [79, 27], [75, 19], [49, 47], [67, 17]]
    )
    quickestWayUp(
        [[8, 52], [6, 80], [26, 42], [2, 72]],
        [[95, 13], [97, 25], [93, 37], [79, 27], [75, 19], [49, 47], [67, 17]]
    )
