def dnf(arr, i):
    assert i < len(arr)

    return list(filter(lambda x: x < arr[i], arr)) + list(filter(lambda x: x == arr[i], arr)) + list(filter(lambda x: x > arr[i], arr))

def dnf_in_place(arr, i):
    """
    In place solution to dutch national flag problem in O(n) time and const space
    """
    assert i < len(arr)

    num_greater = 0
    num_lesser = 0
    for j in arr:
        if j > arr[i]:
            num_greater += 1
        elif j < arr[i]:
            num_lesser += 1

    arr[i], arr[num_lesser] = arr[num_lesser], arr[i]

    i = 0
    j = len(arr) - 1

    while i < j:
        if arr[i] < arr[num_lesser]:
            i += 1
        if arr[j] > arr[num_lesser]:
            j -= 1

        if arr[i] > arr[num_lesser] and arr[j] < arr[num_lesser]:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    print arr

def wavy_arr(arr):
    # 1 2 3 4
    arr = sorted(arr)

    result = []
    for i in xrange(0, len(arr)/2):
        result += [arr[i]]
        result += [arr[len(arr)/2 + i]]

    print result
