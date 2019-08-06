import pytest


def minByColumn(table, column):
    least_row = {}

    for row in table:
        column_value = row.get(column, 0)

        if least_row:
            if column_value < least_row.get(column, 0):
                least_row = row
        else:
            least_row = row

    return least_row


def test_minByColumn1():
    table = [{"a": 1}, {"a": 2}, {"a": 3}]

    assert minByColumn(table, "a") == {"a": 1}


def test_minByColumn2():
    table = [
        {"a": 1, "b": 2},
        {"a": 3, "b": 0}
    ]

    assert minByColumn(table, "b") == {"a": 3, "b": 0}


def test_minByColumn3():
    table = [
        {"a": 1, "b": -2},
        {"a": 3}
    ]

    assert minByColumn(table, "b") == {"a": 1, "b": -2}


# def test_minByColumn4():
#     table = [
#         {"a": 1.5, "b": 1},
#         {"a": 1, "b": 1}
#     ]
#
#     assert minByColumn(table, "b") == {"a": 1, "b": -2}


def test_minByColumn5():
    table = []

    assert minByColumn(table, "b") == {}

# if __name__ == "__main__":
#     test_minByColumn1()
#     test_minByColumn2()
#     test_minByColumn3()
