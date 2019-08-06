import pytest


def minByOrder(table, columns):
    least_row = {}

    for row in table:
        for column in columns:
            column_value = row.get(column, 0)

            if least_row:
                if column_value < least_row.get(column, 0):
                    least_row = row
                    break
                elif column_value == least_row.get(column, 0):
                    continue
                else:
                    break
            else:
                least_row = row
                break

    return least_row


def test_minByOrder1():
    table = [
        {"a": 1, "b": 2},
        {"a": 1, "b": 3},
        {"a": 1, "b": 4}
    ]

    assert minByOrder(table, ["a"]) == {"a": 1, "b": 2}


def test_minByOrder2():
    table = [
        {"x": 1, "y": 3},
        {"x": 1, "y": 0}
    ]

    assert minByOrder(table, ["x", "y"]) == {"x": 1, "y": 0}


def test_minByOrder3():
    table = [
        {"x": 2, "y": 3},
        {"x": 2, "y": 1},
        {"x": 1, "y": 10}
    ]

    assert minByOrder(table, ["x", "y"]) == {"x": 1, "y": 10}


def test_minByOrder4():
    table = [
        {"x": 3, "y": -1, "z": 0},
        {"x": 1, "y": 10, "z": 1},
        {"x": 1, "y": 10, "z": 0}
    ]

    assert minByOrder(table, ["x", "y", "z"]) == {"x": 1, "y": 10, "z": 0}


def test_minByOrder5():
    table = [
      {"x": 1, "y": 2, "z": 3},
      {"x": 2, "y": 2, "z": 2}
    ]

    assert minByOrder(table, ["x", "y", "z"]) == {"x": 1, "y": 2, "z": 3}


if __name__ == "__main__":
    test_minByOrder5()
