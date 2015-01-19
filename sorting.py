# EPI 12.1
def bin_search(arr, k, low, high):
    if low > high:
        return -1

    mid = low + (high - low) / 2

    if arr[mid] == k:
        return mid
    elif arr[mid] > k:
        return bin_search(arr, k, low, mid - 1)
    else:
        return bin_search(arr, k, mid + 1, high)

def bin_search_g(arr, k, low, high):
    if low > high:
        return low

    mid = low + (high - low) / 2

    if arr[mid] == k:
        return mid
    elif arr[mid] > k:
        return bin_search_g(arr, k, low, mid - 1)
    else:
        return bin_search_g(arr, k, mid + 1, high)

def first_oc(arr, k):
    idx = bin_search(arr, k, 0, len(arr))

    if idx == -1:
        return -1

    while arr[idx - 1] == k:
        idx -= 1

    return idx

# EPI 12.2
def first_greater(arr, k):
    if k < arr[0]:
        return arr[0]
    elif k > arr[-1]:
        return -1

    idx = bin_search_g(arr, k, 0, len(arr))

    return arr[idx]


# EPI 12.3
# Supa tricky problem but you got it right. Read the problem statement carefully, requirement is that it is distinct.
# The structure of solution is VERY similar to bin search in rotated array
def bin_search_i(arr, low, high):
    if low > high:
        return -1

    mid = low + (high - low) / 2

    print arr[mid], mid

    if arr[mid] == mid:
        return mid
    elif arr[mid] < mid:
        if arr[low] > low:
            return bin_search_i(arr, low, mid - 1)
        else:
            return bin_search_i(arr, mid + 1, high)
    else:
        if arr[high] < high:
            return bin_search_i(arr, mid + 1, high)
        else:
            return bin_search_i(arr, low, mid - 1)


def search_sorted_fori(arr):
    return bin_search_i(arr, 0, len(arr) - 1)


# EPI 12.4
# Another supa tricky problem, required several attempts to get it right
# General principles for twists on binary search
# Think about stopping condition first
# Think about what the recursion condition on mid is
# Think about the impact on array structure or problem structure on the two elses (does the > and < require nested ifs?)
def bin_search_cyc(arr, low, high):
    if low > high:
        return high

    mid = low + (high - low) / 2
    
    if arr[mid] < arr[mid - 1] and arr[mid] < arr[high]:
        return mid

    if arr[mid] < arr[high]:
        # lower half
        return bin_search_cyc(arr, low, mid - 1)
    else:
        # upper half
        return bin_search_cyc(arr, mid + 1, high)

def search_cyc(arr):
    return arr[bin_search_cyc(arr, 0, len(arr) - 1)]

# EPI 12.5
# This is an unfair problem because it involves exception handling. The idea we had of incrementing high index by powers of 2 is the right way to go.
# Wait till we hit an exception and then bin search in it to get high and then do a regular binary search

# EPI 12.6
# Doing this in logk is easy. But can we do better?
# Yes, use the equations
# When solving problems like these, once done try to use them on test cases
def find_t(k):
    p = 0
    while (2 ** p < k):
        p += 1

    low = 2 ** ((p - 1) / 2)
    high = 2 ** (p/2 + 1)

    mid = low + (high - low) / 2

    while (mid ** 2 != k):
        if (mid + 1) ** 2 > k and mid ** 2 <= k:
            return mid
        elif (mid + 1) ** 2 == k:
            return mid + 1

        if mid**2 > k:
            mid = (mid + low) / 2
        else:
            mid = (mid + high) / 2

    return mid

# EPI 12.7
# Look at solution, i don't even want to...

# EPI 12.8
# Black ninja problem
def search_in_2(arr1, arr2, k):
    m = len(arr1)
    n = len(arr2)

    # Fucking complicated
    # TODO
    pass

# EPI 12.9
# Did this already

# EPI 12.10
# This is a fairly standard algo question (esp asked in question papers)
def find_min_max(arr):
    def find_min_max_s(arr):
        if len(arr) <= 3:
            return min(arr), max(arr)

        min_low, max_low = find_min_max_s(arr[0:len(arr)/2])
        min_high, max_high = find_min_max_s(arr[len(arr)/2:])

        return min(min_low, min_high), max(max_low, max_high)

    return find_min_max_s(arr)


# EPI 12.11
# Quickselect median finding algorithm
# JESUS FUCKING CHRIST DOGSHIT I CANNOT IMPLEMENT THIS!!!!! TODO, BIGTIME TODO
def quickSelect(seq, k):
    # this part is the same as quick sort
    len_seq = len(seq)

    if k <= 0:
        return seq[0]

    pivot = seq[len_seq / 2]

    smallerList = list(filter(lambda x: x <= pivot, seq))
    largerList = list(filter(lambda x: x > pivot, seq))

    # here starts the different part
    m = len(smallerList)

    if k == m:
        return pivot
    elif k < m:
        return quickSelect(smallerList, k)
    else:
        return quickSelect(largerList, k-m-1)

# EPI 12.12
# Difficult arguments. Problems with really tight corner cases is going to be hellish

# EPI 12.13
# Helpful tip: If the problem says space complexity of O(k) it means you are _allowed_ to keep storage of even 2k - 1 :/
# The solution is a bit tricky
# The heap solution is obvious

# EPI 12.14
# Jeez man...

# EPI 12.15
# So this solution is completely different from whats there in the book. Read both
# This solution also has the problem of overflow. One way to get around that is to use
# modular arithmetic
def find_missing(arr):
    diff = sum(xrange(len(arr))) - sum(arr)

    xorp = reduce(lambda x, y: x ^ y, arr + list(xrange(len(arr))))

    for i in xrange(len(arr)):
        s = i
        e = abs(diff) + s

        if s ^ e == xorp:
            if s - e == diff:
                return s, e
            elif e - s == diff:
                return e, s

    return ":("

#EPI 12.16
# Extremely tricky problem
# At each step, a descent into hell happens. If you see a problem whose variant can be solved
# with bitwise ops, see if you can solve it using their binary representations
# Here, the initial idea of doing a mod 3 was a step in the right direction. Just needed to
# identify that the unique bit for each position can be identified by doing a bitwise mod 3
# operation
def find_missing_three(arr):
    pass


def merge_sort(arr):
    def merge(arr1, arr2):
        i = 0
        j = 0

        merged_arr = []

        while (i <= len(arr1) - 1 and j <= len(arr2) - 1):
            if arr1[i] <= arr2[j]:
                merged_arr += [arr1[i]]
                i += 1
            else:
                merged_arr += [arr2[j]]
                j += 1

        merged_arr += arr1[i:] + arr2[j:]

        return merged_arr

    if len(arr) <= 3:
        return sorted(arr)

    return merge(merge_sort(arr[:len(arr)/2]), merge_sort(arr[len(arr)/2:]))

def count_inversions(arr):
    # Interesting problem based on merge sort
    def merge(arr1, arr2):
        i = 0
        j = 0
        inv = 0

        merged_arr = []

        while (i <= len(arr1) - 1 and j <= len(arr2) - 1):
            if arr1[i] <= arr2[j]:
                merged_arr += [arr1[i]]
                i += 1
            else:
                merged_arr += [arr2[j]]
                j += 1
                inv += 1

        merged_arr += arr1[i:] + arr2[j:]

        return (merged_arr, inv)

    if len(arr) == 1:
        return (arr, 0)

    if len(arr) == 2:
        inv = 0
        if arr[0] > arr[1]:
            inv += 1
        return (sorted(arr), inv)

    arr1, inv1 = count_inversions(arr[len(arr)/2:])
    arr2, inv2 = count_inversions(arr[:len(arr)/2])

    arr, inv3 = merge(arr1, arr2)

    return (arr, inv1 + inv2 + inv3)
