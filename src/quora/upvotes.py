# def is_non_decreasing(arr):
#     for p in xrange(len(arr) - 1, 0, -1):
#         if arr[p] < arr[p - 1]:
#             return False
#     return True
#
#
# def is_non_increasing(arr):
#     for q in xrange(len(arr) - 1):
#         if arr[q] < arr[q + 1]:
#             return False
#     return True
#
#
# if __name__ == "__main__":
#     n_and_k = list(map(int, raw_input().rstrip().split(" ")))
#     up_votes = list(map(int, raw_input().rstrip().split(" ")))
#
#     n = n_and_k[0]
#     k = n_and_k[1]
#
#     i = 0
#     while k + i <= len(up_votes):
#         result = 0
#
#         window = up_votes[i:k + i]
#         i += 1
#
#         for a in xrange(len(window)):
#             for b in xrange(len(window), a+1, -1):
#                 sub_range = window[a:b]
#                 if is_non_decreasing(sub_range):
#                     result += 1
#                 if is_non_increasing(sub_range):
#                     result -= 1
#         print(result)
#
# # if a window is non decreasing, there are k(k-1)/2 non decreasing sub ranges
# # if the prev window is non decreasing and the last element in the next window is greater than the last element in the
# # previous window, there are k(k-1)/2 new non decreasing sub ranges
# # if the prev window is non decreasing and the last element in the next window is lesser than the last element in the
# # previous window, there are (k-1)(k-2)/2 new non decreasing sub ranges
#
# # if a window iss non increasing, there are k(k-1)/2 non increasing sub ranges
# # if the prev window is non increasing and the last element in the next window is lesser than the last element in the
# # previous window, there are k(k-1)/2 new non increasing sub ranges
# # if the prev window is non increasing and the last element in the next window is greater than the last element in the
# # previous window, there are (k-1)(k-2)/2 new non decreasing sub ranges
#
# # if the previous window is neither non decreasing nor non increasing
#
# # 1 2 3 1 1
# # 231
# # 311


# This file solves the upvotes challenge on Quora Engineering Challenges
# https://www.quora.com/challenges#upvotes

# Find all Non-decreasing range in a window and append them into a list
# parameters: start, end: starting and ending point of the window
# return: a list containing all non-decreasing subranges in the window, subranges are in the form of [first, last]
def findAllNonDecr(start, end):
    output = []
    # first = starting point of an subrange
    # last = ending pointer of an subrange
    first = last = start

    for num in range(start + 1, end ):
        if list[num] >= list[last]:
            last = num
        else:
            # append the subrange to the subrange list if the length is at least 2 days
            if first != last:
                output.append([first, last])
            # reset first and last to the pointer
            first = last = num

    # if subrange continues through the last element
    if first != last:
        output.append([first, last])

    return output

# Same function as last one, but find all non-increasing range
def findAllNonIncr(start, end):
    output = []
    first = last = start

    for num in range(start + 1, end):
        if list[num] <= list[last]:
            last = num
        else:

            if first != last:
                output.append([first, last])

            first = last = num

    # if subrange continues through the last element
    if first != last:
        output.append([first, last])

    return output

# calculate the number of subranges within the non-Decr/Incr range, given the start and the end of the subrange
def sumSubrange(output):
    if (len(output) ==0): return 0
    sum = 0
    # find the number of subranges for each subrange in the list
    for pair in output:
        diff = pair[1] - pair[0] + 1
        # The number of subrange in a N-length subrange is 1 + 2 + ... + N - 1 = (N - 1) * N/2
        sum += (diff - 1) * diff / 2

    return sum


# move the window down the list, updating the non-decreasing range list as well as the number of non-decreasing subranges
def moveNonDecr(start, end, output, sum):

    # If there weren't any subranges from last window, do a brand new search in current window
    if len(output) == 0:
        newOutput = findAllNonDecr(start + 1, end + 1)
        newSum = sumSubrange(newOutput)
        return newOutput, newSum

    firstSubrange = output[0] # first subrange of previous window
    lastSubrange = output[-1] # last subrange of previous window

    # take care of boundary condition in the back
    if firstSubrange[0] == start:

        # if the start of the window was the start of the first subrange, then the subrange will shift by one
        sum -= (output[0][1] - output[0][0])
        output[0][0] += 1

    # # take care of boundary condition in the front
    # if the end of the window was the end of the last subrange
    if lastSubrange[1] == end - 1:

        # if the end of the subrange continues, shift the subrange by one
        if list[end] >= list[end-1]:
            sum += (output[-1][1] - output[-1][0] + 1)
            output[-1][1] += 1

    # if the end of the window was not the end of the last subrange, see if the last element from last window and the new element would form a new subrange
    else:
        if list[end] >= list[end -1]:

            output.append([end-1, end])
            sum += 1

    # if boundary condition in the back makes the first subrange of only length 1, delete that subrange from list

    if output[0][0] == output[0][1]:
        output.pop(0)

    return output, sum

# Same function as last one, but update all non-increasing range
def moveNonIncr(start, end, output, sum):

    if len(output) == 0:
        newOutput = findAllNonIncr(start + 1, end + 1)
        newSum = sumSubrange(newOutput)
        return newOutput, newSum

    firstSubrange = output[0] # first subrange of previous window
    lastSubrange = output[-1] # last subrange of previous window

    # take care of left edge condition
    if firstSubrange[0] == start:

        # if the start of the window was the start of the first subrange, then the subrange will shift by one
        sum -= (output[0][1] - output[0][0])
        output[0][0] += 1

    # take care of right edge condition
    # if the end of the window was the end of the last subrange
    if lastSubrange[1] == end - 1:

        # if the end of the subrange continues, shift the subrange by one
        if list[end] <= list[end-1]:
            sum += (output[-1][1] - output[-1][0] + 1)
            output[-1][1] += 1

    # if the end of the window was not the end of the last subrange, try if the last two element would form a new subrange
    else:
        if list[end] <= list[end -1]:

            output.append([end-1, end])
            sum += 1

    # if that makes the subrange only 1 number, delete that subrange from list
    if output[0][0] == output[0][1]:
        output.pop(0)

    return output, sum

# input for N and K as int
n, k = raw_input().split()
n, k = int(n), int(k)

# input for N positive Integers of upvote counts as int list
global list
list = raw_input().split()
list = [int(i) for i in list]

# initialize a pointer for the start and end of the size K window
start = 0
end = 0 + k
outputNonDecr = findAllNonDecr(start, end)
outputNonIncr = findAllNonIncr(start, end)
sumNonDecr = sumSubrange(outputNonDecr)
sumNonIncr = sumSubrange(outputNonIncr)
print sumNonDecr - sumNonIncr

while end != n:
    outputNonDecr, sumNonDecr = moveNonDecr(start, end, outputNonDecr, sumNonDecr)
    outputNonIncr, sumNonIncr = moveNonIncr(start, end, outputNonIncr, sumNonIncr)
    start += 1
    end += 1
    print sumNonDecr - sumNonIncr
