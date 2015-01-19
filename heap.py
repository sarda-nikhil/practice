import heapq

# This is the most important heap algorithm!
# This arises in so many contexts its not fucking funny
# Apart from k way merge, your question could be, kth largest/smallest
# element from an nxn array (take a kxk subarray)
def merge_k(arr, n):
    space = []
    for i in xrange(len(arr)):
        heapq.heappush(space, (arr[i][0], i, 0))

    while space:
        value, arr_idx, arr_sub_idx = heapq.heappop(space)

        yield value

        if len(arr[arr_idx]) - 1 > arr_sub_idx:
            heapq.heappush(space, (arr[arr_idx][arr_sub_idx + 1], arr_idx, arr_sub_idx + 1))
