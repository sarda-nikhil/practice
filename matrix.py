def printspiral(m, n):
    # m rows and n cols
    arr = [[0] * n for i in xrange(m)]

    #val = 1
    val = m * n
    
    def gen_spiral(arr, m, n, x, y, val):
        if x > m or y > n:
            return

        for i in xrange(y, n):
            if arr[x][i] == 0:
                arr[x][i] = val
                val -= 1

        for i in xrange(x + 1, m):
            if arr[i][n-1] == 0:
                arr[i][n-1] = val
                val -= 1

        for i in xrange(n - 1, y, -1):
            if arr[m-1][i] == 0:
                arr[m-1][i] = val
                val -= 1

        for i in xrange(m - 1, x, -1):
            if arr[i][y] == 0:
                arr[i][y] = val
                val -= 1

        gen_spiral(arr, m - 1, n - 1, x + 1, y + 1, val)

    gen_spiral(arr, m, n, 0, 0, val)

    for i in arr:
        print i


def find_sorted(arr, e):
    """
    In a row and col sorted array, find a given element.
    Algorithm is really slick, start at top right and snake down

    We can't really start on 0,0 or m,n because all possible movements
    only lead to increases.
    """
    i = 0
    j = len(arr[0]) - 1

    while i < len(arr) and j >= 0:
        print arr[i][j]
        if e == arr[i][j]:
            return i, j
        elif e > arr[i][j]:
            i += 1
        elif e < arr[i][j]:
            j -= 1

    return "Not found"


def matrix_rot_nxn(arr):
    # Super tricky
    # Do this again
    # Figure out why the fuck do the indices work. In the problem below
    # we pass the full length while out here we pass the length - 1
    n = len(arr)
    
    def rotate_outline(arr, n, x):
        if x >= n:
            return

        for i in xrange(x, n):
            temp = arr[x][i]
            arr[x][i] = arr[n-i][x]
            arr[n-i][x] = arr[n][n+x-i]
            arr[n][n+x-i] = arr[i][n]
            arr[i][n] = temp

        rotate_outline(arr, n - 1, x + 1)

    rotate_outline(arr, len(arr) - 1, 0)

    for i in arr:
        print i


def alternating_matrix(m, n):
    arr = [[None] * n for i in xrange(m)]

    def gen_outline(arr, x, y, m, n, s):
        if x > m or y > n:
            return

        if s == 'X':
            s = 'O'
        else:
            s = 'X'

        for i in xrange(y, n):
            if arr[x][i] is None:
                arr[x][i] = s
            if arr[m-1][i] is None:
                arr[m - 1][i] = s

        for i in xrange(x, m):
            if arr[i][y] is None:
                arr[i][y] = s
            if arr[i][n-1] is None:
                arr[i][n - 1] = s

        gen_outline(arr, x + 1, y + 1, m - 1, n - 1, s)

    gen_outline(arr, 0, 0, m, n, 'O')

    for i in arr:
        print i
