# https://www.pramp.com/challenge/2WBx3Axln1t7JQ2jQq96


def find_busiest_period(data):
    max_timestamp, max_people_in_mall, people_in_mall = 0, 0, 0
    data_len = len(data)
    for i in range(data_len):
        timestamp, people, direction = data[i][0], data[i][1], data[i][2]

        if direction == 1:  # entry
            people_in_mall += people
        else:  # exit
            people_in_mall -= people

        # if next data_point has same timestamp as current data_point, no need to compare max_people_in_mall
        # we need to add up all entries and exits of the same timestamp, before comparison
        if i < data_len - 1 and timestamp == data[i + 1][0]:
            continue

        # when the loop reaches this conditional, we are sure entry/exit deltas for the same timestamp have been added
        if people_in_mall > max_people_in_mall:
            max_people_in_mall = people_in_mall
            max_timestamp = timestamp

    return max_timestamp


if __name__ == "__main__":
    assert (find_busiest_period([[1487799426, 21, 1]]) == 1487799426)

    assert (find_busiest_period([[1487799425, 21, 0], [1487799427, 22, 1], [1487901318, 7, 0]]) == 1487799427)

    assert (find_busiest_period([[1487799425, 21, 1], [1487799425, 4, 0], [1487901318, 7, 0]]) == 1487799425)

    assert (find_busiest_period(
        [[1487799425, 14, 1], [1487799425, 4, 0], [1487799425, 2, 0], [1487800378, 10, 1], [1487801478, 18, 0],
         [1487801478, 18, 1], [1487901013, 1, 0], [1487901211, 7, 1], [1487901211, 7, 0]]) == 1487800378)

    assert (find_busiest_period(
        [[1487799425, 14, 1], [1487799425, 4, 1], [1487799425, 2, 1], [1487800378, 10, 1], [1487801478, 18, 1],
         [1487901013, 1, 1], [1487901211, 7, 1], [1487901211, 7, 1]]) == 1487901211)

    assert (find_busiest_period(
        [[1487799425, 14, 1], [1487799425, 4, 0], [1487799425, 2, 0], [1487800378, 10, 1], [1487801478, 18, 0],
         [1487801478, 19, 1], [1487801478, 1, 0], [1487801478, 1, 1], [1487901013, 1, 0], [1487901211, 7, 1],
         [1487901211, 8, 0]]) == 1487801478)
