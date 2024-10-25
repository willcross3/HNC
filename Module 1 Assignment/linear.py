# Python3 code to linearly search x in arr[].
def linear(arr, N, x):

    for i in range(0, N):
        if (arr[i] == x):
            return i
    return -1

