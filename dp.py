class getCombinations():
    """
    Not clear how the DP algorithm works
    """
    def __init__(self, arr, n):
        self.arr = arr
        self.n = n

    def gen_combination(self, arr, n, comb):
        if n < 0:
            yield None
        elif n == 0:
            yield comb
        else:
            for i in arr:
                if n - i < 0:
                    continue

                for c in self.gen_combination(arr, n - i, comb + [i]):
                    if c is not None:
                        yield c

    def get_combination(self, arr, n):
        a = set([tuple(sorted(c)) for c in self.gen_combination(arr, n, [])])
        return a


    def get_combinations_dp(self, arr, n):
        comb = [0] * (n + 1)
        comb[0] = 1

        for i in arr:
            for j in xrange(i, n + 1):
                comb[j] += comb[j-i]

        return comb

# EPI 17.4
def get_paths_dp(m, n):
    """
    Given a mxn matrix, calculate ways to get from 0,0 to m,n

    This is a DP solution

    Note the recurrence. Sometimes we can save on space complexity if
    if the recurrence does not extend to members that are too far out.
    """
    arr = [[0] * n for i in xrange(m)]

    for i in xrange(m):
        for j in xrange(n):
            if i == 0 or j == 0:
                arr[i][j] = 1
            else:
                arr[i][j] += arr[i - 1][j] + arr[i][j - 1]

    print arr[m - 1][n - 1]

def get_paths_db_opt(m, n):
    """
    This is a space optimized version. Note that we do not need two rows
    """
    prev = [0] * n
    curr = [0] * n

    for i in xrange(m):
        for j in xrange(n):
            if i == 0:
                curr[j] = 1
            else:
                curr[j] += prev[j] + curr[j - 1]
        prev = curr
        curr = [0] * n

    print prev[n - 1]


# EPI variant
def get_monotone_numbers(k):
    """
    A number is monotone if subsequent digits are >= to each other

    let P[i][j] = number of i digits whose last digit is at most j
    so P[t][4] = all monotone numbers of t digits whose last digit is at most 4

    P[t][4] = P[t][3] + P[t - 1][4]

    When dealing with DP problems, start drawing the matrix out for base cases
    if you have the recurrence figured out. In this problem, while the recurrence
    is the same, the base case is completely different.
    """

    arr = [[0] * 10 for i in xrange(k)]

    for i in xrange(k):
        for j in xrange(10):
            if i == 0:
                arr[i][j] = j + 1
            else:
                arr[i][j] += arr[i - 1][j] + arr[i][j - 1]

    print arr[k - 1][9]

# The below two ways get the ways to score when the order matters
def get_ways_to_score_naive(n, ways):
    def gen_ways(n, ways):
        if n <= 0:
            yield []
        else:
            for i in ways:
                if n - i < 0:
                    continue
                for j in gen_ways(n - i, ways):
                    yield [i] + j

    return [i for i in gen_ways(n, ways)]

def get_ways_to_score(n, ways):
    arr = [0] * (n + 1)

    for i in xrange(n + 1):
        if i in ways:
            arr[i] += 1

        for j in ways:
            if i - j > 0:
                arr[i] += arr[i - j]

    print arr

# The below ways get the way to score when the order does not matter
# Look at the key difference between the two. In the first one we do not
# modify the ways array while entering the recursion but in the second
# we do modify it, once we have moved on to the next element, we don't
# bother with previous elements in the ways array
def get_ways_score_no_order_naive(n, ways):
    def gen_ways(n, ways):
        if n <= 0:
            yield []
        else:
            for i in xrange(len(ways)):
                if n - ways[i] < 0:
                    break
                for j in gen_ways(n - ways[i], ways[i:]):
                    yield [ways[i]] + j
 
    return [i for i in gen_ways(n, ways)]

# EPI 17.1
def get_ways_score_no_order(n, ways):
    arr = [0] * (n + 1)

    for i in ways:
        for j in xrange(i, len(arr)):
            arr[j] += arr[j - i]

    print arr

# EPI 17.3
# n c k = n - 1 c k + n - 1 c k - 1
# Seriously, think really carefully before you add some dumbfuck
# if, else for loop logic
# for instance you were thinking of iterating j from _i_ to k + 1!
def binomial(n, k):
    arr = [[0] * (k + 1) for i in xrange(n + 1)]

    for i in xrange(n + 1):
        for j in xrange(k + 1):
            if j > i:
                arr[i][j] = 0
            elif j == 0 or i <= 1:
                arr[i][j] = 1
            else:
                arr[i][j] = arr[i-1][j] + arr[i-1][j-1]

    return arr[n][k]

# EPI 17.2
# Levenshtein distance, how does it work. Have not completely grasped DP thinking

# EPI 17.5
# arr[i][j] = max(arr[i][j] + arr[i][j - 1], arr[i][j] + arr[i-1][j])
def max_fish(arr):
    dp_arr = [[0] * (len(arr[0])) for i in xrange(len(arr))]

    for i in xrange(len(arr)):
        for j in xrange(len(arr[0])):
            if i == 0 or j == 0:
                dp_arr[i][j] = arr[i][j]
            else:
                dp_arr[i][j] = max(arr[i][j] + dp_arr[i][j - 1], arr[i][j] + dp_arr[i-1][j])

    return dp_arr[len(arr) - 1][len(arr[0]) - 1]

# EPI 17.6 -> Come back to this 

# EPI 17.7
# V[i, w] = max(V[i-1, w], V[i - 1, w - wi] + vi)
# Dimag ki batti jali
# When you have to take a few items out of a bag to construct an optimal score
# do-> for over items, for over max_value, max_weight
# look at the score combinations problem
# still come back to completely understand
def knapsack(w, knapsack):
    V = [[0] * (w + 1)]
    for i in knapsack:
        for j in xrange(w, i[0], -1):
            V[j] = max(V[j], V[j - i[0]] + i[1])

    return V[w]

# EPI 17.9
# This is the redneck method
def test_for_tie(arr):
    def test_tie(arr, v, w, f):
        if arr == []:
            return v == w
        for i in arr:
            t = arr[:]
            t.remove(i)
            if f == 0:
                if test_tie(t, v + i, w, 1) is True:
                    return True
            else:
                if test_tie(t, v, w + i, 0) is True:
                    return True

        return False

    return test_tie(arr, 0, 0, 0)


# EPI 17.10

# EPI 17.13
# Given c cases and d drops, how many floors can we test
# if c = 1, we can test one floor
# if d = 1, we can test one floor
# in general, if d < c, we can test d floors
# Intuition for this is that with c cases and d drops
# you have either the case that c - 1 cases got destroyed with d - 1 drops and you have one more
# shot left
# or you made if all the way to d drops with c - 1 cases destroyed.
# T[c][d] = T[c-1][d] + (T[c][d-1] + 1)
# should be a simple bit of code

# EPI 17.17
# For t to be an interleaving, t[0:i] must also be an interleaving
# T[i, p, q] = T[i - 1, p - 1, q] && s1[p] == t[i] || T[i - 1, p, q - 1] && s2[q] == t[i]
# The recurrence is probably correct
def test_interleaving(s1, s2, t):
    T = {}

    for i in xrange(len(t)):
        for j in xrange(len(s1)):
            for k in xrange(len(s2)):
                if j == 0 and k > 0 and i > 0:
                    T[(i,j,k)] = T[(i - 1, j, k - 1)] and s2[k] == t[i]
                elif k == 0 and j > 0 and i > 0:
                    T[(i,j,k)] = T[(i - 1, j - 1, k)] and s1[j] == t[i]
                elif i > 0 and j > 0 and k > 0:
                    T[(i,j,k)] = (T[(i - 1, j - 1, k)] and s1[j] == t[i]) or (T[(i - 1, j, k - 1)] and s2[k] == t[i])
                else:
                    T[(i,j,k)] = True

    print T
    return T[(len(t) - 1,len(s1) - 1,len(s2) - 1)]

# EPI 17.18
# Booyah!
def boardgame(n, k):
    arr = [0] * (n + 1)

    for i in xrange(1, k + 1):
        arr[i] = 1

    for i in xrange(1, n + 1):
        for j in xrange(1, k + 1):
            arr[i] += arr[i - j]

    return arr[n]

# EPI 17.21
# Look at the geeksforgeeks page
def longest_inc_subseq(arr, lis):
    liseq = {}

    for i in xrange(len(arr)):
        for j in xrange(i, len(arr)):
            if not liseq.has_key((i, j)):
                liseq[(i, j)] = []
            if i == j:
                liseq[(i, j)] = [arr[i]]
            else:   
                if liseq[(i, j - 1)] == [] or arr[j] > liseq[(i,j - 1)][-1]:
                    liseq[(i, j)] = liseq[(i, j - 1)] + [arr[j]]

    print liseq

# Number of ways to reach nth steps if one or 2 steps at a time
def numways(n):
    arr = [0] * (n + 1)

    arr[0] = 0
    arr[1] = 1
    arr[2] = 2

    for j in xrange(3, n + 1):
        arr[j] += arr[j - 1] + arr[j - 2] 

    print arr

