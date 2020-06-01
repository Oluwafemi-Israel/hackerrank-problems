"""
https://leetcode.com/problems/reorder-data-in-log-files/
"""


class Solution:
    def reorderLogFiles(self, logs):
        def sorter(log):
            identifier, remainder = log.split(" ", 1)

            if remainder[0].isdigit():
                return (1,)
            return 0, remainder, identifier

        return sorted(logs, key=sorter)


if __name__ == "__main__":
    logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]

    solution = Solution()
    assert solution.reorderLogFiles(logs) == ["let1 art can", "let3 art zero", "let2 own kit dig", "dig1 8 1 5 1",
                                              "dig2 3 6"]
