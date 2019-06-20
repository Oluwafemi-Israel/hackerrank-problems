# Good resource for solving this
# https://codereview.stackexchange.com/a/186390
# however this specific questions has a little mix, sort in descending order


def generate_cycles(ratings):
    unvisited = ratings[:]
    num_items = len(ratings)

    while unvisited:
        start_item = unvisited.pop()
        cycle = [start_item]
        next_item = start_item
        while True:
            next_item = ratings[num_items - next_item]
            if start_item == next_item:
                break
            cycle.append(next_item)
            unvisited.remove(next_item)

        yield cycle


def minimum_swaps(ratings):
    return sum(len(cycle) - 1 for cycle in generate_cycles(ratings))


if __name__ == "__main__":
    print(minimum_swaps([3, 1, 2, 4]))
    print(minimum_swaps([3, 1, 2]))
