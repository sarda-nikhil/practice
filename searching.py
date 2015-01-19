# EPI 14.1
# This algorithm is easy. The only trick is for when array sizes are similar. The algorithm proposed is a "catch up" algorithm.
# The idea is check a[i] against b[j]. If a[i] < b[j], increment i till a[i] >= b[j], elif a[i] > b[j], increment j till they catch up.

# EPI 14.2
# In place merge sort
# Idea, start from the very end and maintain various pointers to track state
# My friend: PLEASE PLEASE PLEASE _THINK_ *HARD* about IF conditions
def inplace_merge(arr1, arr2):
    last_idx = len(arr1) - 1
    last_idx_t = len(arr1) - 1 - len(arr2)

    last_idx_2 = len(arr2) - 1

    while last_idx >= 0:
        if arr1[last_idx_t] <= arr2[last_idx_2] and last_idx_2 >= 0:
            arr1[last_idx] = arr2[last_idx_2]
            last_idx -= 1
            last_idx_2 -= 1
        else:
            arr1[last_idx] = arr1[last_idx_t]
            last_idx_t -= 1
            last_idx -= 1

    print arr1

# EPI 14.3
# Count frequencies of characters
def count_freq(s):
    s = list(sorted(s))

    current = s[0]
    count = 1

    for i in s[1:]:
        if i == current:
            count += 1
        else:
            print current, count
            current = i
            count = 1

    print current, count

# EPI 14.4
# easy problem

# EPI 14.5

# EPI 14.6
# The merge_ival is really tricky. This problem is designed to
# test how well you handle edge cases.
# Also the reduce is rather clever and voo doo ey
def add_interval(ivals, U):
    ivals = sorted(ivals, key=lambda x: x[0])

    def merge_ival(x, y):
        if x[0] <= y[0]:
            if x[1] <= y[1] and x[1] >= y[0]:
                return [(x[0], y[1])]
            elif x[1] >= y[1]:
                return [(x[0], x[1])]
        else:
            if y[1] >= x[0] and y[1] <= x[1]:
                return [(y[0], x[1])]
            elif y[1] >= x[1]:
                return [(y[0], y[1])]
        return [x, y]

    s = reduce(lambda x, y: x + merge_ival(U, y), ivals, [])
    return reduce(lambda x, y: x[:-1] + merge_ival(x[-1], y), s[1:], [s[0]])

# EPI 14.7
def union_interval(ivals):
    ivals = sorted(ivals, key=lambda x: x[0])

    def merge_ival(x, y):
        if x[0] <= y[0]:
            if x[1] <= y[1] and x[1] >= y[0]:
                return [(x[0], y[1])]
            elif x[1] >= y[1]:
                return [(x[0], x[1])]
        else:
            if y[1] >= x[0] and y[1] <= x[1]:
                return [(y[0], x[1])]
            elif y[1] >= x[1]:
                return [(y[0], y[1])]
        return [x, y]

    return reduce(lambda x, y: x[:-1] + merge_ival(x[-1], y), ivals[1:], [ivals[0]])

# EPI 14.9
# Another easy problem. Intuition was right

# EPI 14.11
# Team photo day -> easy problem, sort and make sure each elem is less than corresponding elem in other array

# EPI 14.18
# Got the right intuition. Got too caught up in ordering though, remember we just need to find the best and that's it.
# Everything else was solid. Read up on finding the second best again.

# Another slick binary search problem
def find_peak(arr, low, high):
    mid = low + (high - low) / 2

    if arr[mid] >= arr[mid - 1] and arr[mid] >= arr[mid + 1]:
        return arr[mid]

    if arr[mid] >= arr[mid - 1] and arr[mid] <= arr[mid + 1]:
        return find_peak(arr, mid, high)
    else:
        return find_peak(arr, low, mid)


def find_smallest_circular(arr, low, high):
    if low > high:
        return arr[high]
    mid = low + (high - low) / 2

    if arr[mid] < arr[mid - 1] and arr[mid] <= arr[mid + 1]:
        return arr[mid]

    if arr[mid] < arr[high]: # Right of mid is sorted
        return find_smallest_circular(arr, low, mid - 1)
    else: # Left of mid is sorted
        return find_smallest_circular(arr, mid + 1, high)
