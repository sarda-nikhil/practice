def all_subsets(arr, k):
    if k == 0 or arr is None:
        yield []

    for i in arr:
        # Be careful when writing python
        # Lessons: Shallow copy vs deep copy
        # Also remember that most mutations are in place and return void
        temp = list(arr)
        temp.remove(i)
        for j in all_subsets(temp, k - 1):
            yield [i] + j

def all_permutations(arr):
    if arr is None or arr == []:
        yield []

    for i in arr:
        temp = list(arr)
        temp.remove(i)
        for j in all_permutations(temp):
            yield [i] + j            

def subset_sum(arr, k):
    if k == 0:
        yield []

    if arr == [] and k > 0:
        yield None

    for i in arr:
        temp = list(arr)
        temp.remove(i)
        for j in subset_sum(temp, k - i):
            if j is None:
                continue

            yield sorted([i] + j)

#set([tuple(i) for i in recursion.subset_sum([1,2,3,4,5,6,7], 8)])

def gen_parantheses(n):
    """
    The invocation below yields catalan numbers. This code is correct but how can it be improved
    """
    if n == 1:
        yield '()'
    else:
        for i in xrange(1, n):
            if i == 1:
                for j in gen_parantheses(n-1):
                    yield '(' + j + ')'

            for j in gen_parantheses(n-i):
                for k in gen_parantheses(i):
                    pre = j + k
                    post = j + k
                    if pre == post:
                        yield pre
                    else:
                        yield pre
                        yield post

#len(set([i for i in recursion.gen_parantheses(4)]))

class Sudoku():
    """
    Sudoku solver using backtracking
    Simple but not so simple shit
    """
    def __init__(self, grid):
        self.grid = grid

    def _used_in_row(self, num, row):
        for col in xrange(len(self.grid)):
            if self.grid[row][col] == num:
                return True
        return False

    def _used_in_col(self, num, col):
        for row in xrange(len(self.grid)):
            if self.grid[row][col] == num:
                return True
        return False

    def _used_in_box(self, num, row_box, col_box):
        for row in xrange(0, 3):
            for col in xrange(0, 3):
                if self.grid[row_box + row][col_box + col] == num:
                    return True
        return False

    def _all_filled(self):
        for i in xrange(len(self.grid)):
            for j in xrange(len(self.grid)):
                if self.grid[i][j] == 0:
                    return False

        return True

    def _print_board(self):
        for i in self.grid:
            print i

    def solve(self):
        for row in xrange(len(self.grid)):
            for col in xrange(len(self.grid)):
                if self.grid[row][col] is not 0:
                    continue

                for i in xrange(1, 10):
                    if not self._used_in_row(i, row) and \
                            not self._used_in_col(i, col) and \
                            not self._used_in_box(i, row - row % 3, col - col % 3):

                        self.grid[row][col] = i

                        if self._all_filled():
                            return True

                        if not self.solve():
                            self.grid[row][col] = 0
                        else:
                            return True

                return False


class NQueens():
    """
    NQueens solver. Simple but not so simple shit.
    """
    def __init__(self, n):
        self.n = n
        self.grid = [[0] * n for i in xrange(n)]

    def print_board(arr):
        for i in arr:
            print i

    def _row_valid(self, row):
        for col in xrange(self.n):
            if self.grid[row][col] == 1:
                return False
        return True

    def _col_valid(self, col):
        for row in xrange(self.n):
            if self.grid[row][col] == 1:
                return False
        return True

    def _check_diagonal(self, row, col):
        t_row = row
        t_col = col

        while t_row >= 0 and t_col >= 0:
            if self.grid[t_row][t_col] == 1:
                return False
            t_row -= 1
            t_col -= 1

        t_row = row
        t_col = col

        while t_row >= 0 and t_col < self.n:
            if self.grid[t_row][t_col] == 1:
                return False
            t_row -= 1
            t_col += 1

        return True

    def _print_board(self):
        for i in self.grid:
            print i

    def solve(self, r):
        if r == self.n:
            return True

        for row in xrange(r, self.n):
            for col in xrange(self.n):
                if self._row_valid(row) and self._col_valid(col) and self._check_diagonal(row, col):
                    self.grid[row][col] = 1
                else:
                    continue

                if not self.solve(row + 1):
                    self.grid[row][col] = 0
                else:
                    return True

            return False

def interleave(s1, s2):
    if s1 == []:
        yield s2
    elif s2 == []:
        yield s1
    else:
        for j in interleave(s1[1:], s2):
            yield s1[:1] + j

        for i in interleave(s1, s2[1:]):
            yield s2[:1] + i

def allsubstrings(s):
    for i in xrange(len(s)):
        for j in xrange(i, len(s) + 1):
            print s[i:j]

# The basic idea of this is simple. Do not bother going over
# elements that we have seen before. Also note the trick
# used to not have to create a temp array
def all_unique_permutations(s):
    s = sorted(s)

    def gen_perm(s):
        if len(s) == 1:
            yield s
        else:
            for i in xrange(len(s)):
                if s[i] == s[i - 1] and i > 0:
                    continue
                for j in gen_perm(s[:i] + s[(i + 1):]):
                    yield [s[i]] + j

    return [''.join(i) for i in gen_perm(s)]

# Print combination of words
def all_combinations_words(s):
    if len(s) == 1:
        for i in s[0]:
            yield i
    else:
        for i in s[0]:
            for j in all_combinations_words(s[1:]):
                yield i + ' ' + j

def merge(seq1, seq2):
    s1 = seq1.next()
    s2 = seq2.next()

    while True:
        # Try to understand why the nexts CANNOT be in s1 and s2
        if s1 > s2:
            yield s2
            s2 = seq2.next()
        elif s1 < s2:
            yield s1
            s1 = seq1.next()
        else:
            yield s1
            s1 = seq1.next()
            s2 = seq2.next()

def times(n, seq):
    for i in seq:
        yield n * i

# Sequence 235
def m235():
    yield 1
    times2 = times(2, m235())
    times3 = times(3, m235())
    times5 = times(5, m235())
    for i in merge(times2, merge(times3, times5)):
        yield i
