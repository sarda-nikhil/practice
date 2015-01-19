def is_isomorphic(str1, str2):
    for i in xrange(len(str1)):
        str2 = str2[:i] + str2[i:].replace(str2[i], str1[i], 1)

    if str1 == str2:
        return 1

def is_valid_binstring(str1):
    s = []
    depth = 0
    if str1 == '':
        return 1

    if str1[0] != '(':
        return -1

    for i in str1:
        print i
        if i not in '()0':
            return -1

        if i == '(':
            s.append(i)
            if s.count('(') > depth:
                depth = s.count('(')

        if i == '0':
            if s[len(s) - 1] not in '(0':
                return -1
            s.append(i)
            print s

        if i == ')':
            t = ''
            try:
                t = s.pop()
                t = s.pop() + t
                t = s.pop() + t
            except:
                return -1
            
            if str(t) != '(00':
                print t
                return -1

            s.append('0')

    if len(s) > 1 or s.pop() not in '0':
        return -1

    return depth - 1

def boyer_moore(s):
    count = 0
    current = None

    for i in s:
        if current != i:
            count -= 1
        else:
            count += 1

        if count <= 0:
            current = i
            count = 1
            continue

    print current

def min_abs_diff(arr1, arr2):
    # CRAP
    """
    You have two arrays of integers, where the integers do not repeat and the two arrays have no common integers. 
    
    Let x be any integer in the first array, y any integer in the second. Find min(Abs(x-y)). That is, find the smallest difference between any of the integers in the two arrays. """
    current_min = 100000

    arr2 = list(reversed(arr2))
    i = 0
    j = 0

    while True:
        if i == len(arr1) and j == len(arr2):
            break

        if abs(arr2[j] - arr1[i]) < current_min:
            current_min = abs(arr2[j] - arr1[i])

        if (arr2[j] - arr1[i]) < (arr1[i] - arr2[j]):
            if i < len(arr1) - 1:
                i += 1
        else:
            if j < len(arr2) - 1:
                j += 1

    print i, j

def print_arr_cols(arr, n):
    i = 0

    while i < n:
        j = i
        tmp = []
        while j < len(arr):
            tmp += [arr[j]]
            j += n
        print tmp
        i += 1

        
def reverse_words(sent):
     tmp = ''
     for i in sent.split(' '):
         tmp += reduce(lambda x, y: x + y, reversed(i), '') + ' '
         
     print tmp[:len(tmp) - 1]        

def generate_all_factors(n):
    for i in xrange(1, n / 2 + 1):
        if n % i == 0:
            print i

    print n

def gen_comb_factors(n):
    def gen_fac(n, factors):
        if n == 1:
            print factors
            return

        for i in xrange(2, n/2 + 2):
            if n % i == 0:
                gen_fac(n/i, factors + [i])

    gen_fac(n, [])

def max_succ_sum(arr):
    current_total = arr[0]
    current_max = -10000

    for i in xrange(1, len(arr)):
        current_total += arr[i]

        if current_total > current_max:
            current_max = current_total

        if current_total < 0:
            current_total = 0

    print current_max

def max_succ_prod(arr):
    current_min = arr[0]
    current_max = arr[0]

    maxval = 0
    
    for i in xrange(1, len(arr)):
        t_max = current_max
        t_min = current_min
        current_max = max(t_min * arr[i], t_max * arr[i], 1)
        current_min = min(t_max * arr[i], t_min * arr[i], 1)

        if current_max > maxval:
            maxval = current_max

    print maxval

def is_number(num):
    if num[0] not in '+-.0123456789':
        return False

    if num[0] in '+-.' and len(num) < 2:
        return False

    if num.count('.') > 1:
        return False

    for s in num[1:]:
        if s not in '0123456789':
            return False

    return True

def dist_between_words(sent, w1, w2):
    t = sent.split(' ')

    if w1 not in t or w2 not in t:
        return -1

    return abs(t.index(w1) - t.index(w2))

def smallest_substring(str1, chars):
    pass #Thinking of an O(n) time and O(1) space algorithm


def array_interleaving(arr):
    """
    a1,a2,a3,...,an,b1,b2,...,bn => a1,b1,a2,b2,...an,bn

    Linear time, linear space
    """
    assert len(arr) % 2 == 0

    arr_f = []

    for i in xrange(len(arr) / 2):
        arr_f += [arr[i]]
        arr_f += [arr[i + len(arr) / 2]]

    return arr_f

def remove_dup_char1(s):
    """
    Strings are immutable, so work with them as lists

    Looks more difficult

    This is an unordered solution
    """
    s = list(s)
    sorted(s) # Can't sort it mate

    prev_char = s[0]
    for i in xrange(1, len(s)):
        if s[i] == s[i - 1]:
            s[i - 1] = ''

    return "".join(s)

def remove_dup_char2(s):
    """
    This is an O(n2) solution
    """
    s = list(s)

    def ret(x, y):
        if y in x:
            return x
        else:
            return x + [y]

    return ''.join(reduce(ret, s, []))

def rotated_binary_search(arr, n):
    """
    Phenomenal problem. This binary search is more general
    than a regular binary search.
    """
    def find(arr, n, low, high):
        if low > high:
            return None

        mid = low + (high - low) / 2

        if arr[mid] == n:
            return mid

        # Is lower half sorted
        if arr[mid] > arr[low]: 
            if n < arr[mid] and n >= arr[low]:
                # Regular bin search
                high = mid - 1
            else:
                low = mid + 1
        else:
            if n > arr[mid] and n <= arr[high]:
                # Regular bin search
                low = mid + 1
            else:
                high = mid - 1

        return find(arr, n, low, high)

    return find(arr, n, 0, len(arr) - 1)

def winnable_game(arr):
    """
    EPI 6.4
    """

    last_index = arr[0]
    steps = [0]
    for i in xrange(1, len(arr)):
        if i > last_index:
            print "Unreachable"
            return
        if arr[i] + i > last_index:
            steps += [i]
            last_index += (arr[i] + i - last_index)
            if last_index >= len(arr) - 1:
                print "Reached", steps
                break

    min_steps = 0
    for j in xrange(1, len(steps)):
        min_steps += steps[j] - steps[j - 1]
    print min_steps
    print last_index

def remove_all_dups(arr, k):
    """
    EPI 6.5
    """

    arr = map(lambda x: 0 if x == k else x, arr)

    curr_index = 0
    zero_index = 0

    while curr_index < len(arr) - arr.count(k):
        if arr[curr_index] != 0:
            curr_index += 1
        elif arr[curr_index] == 0:
            zero_index = curr_index
            while arr[zero_index] == 0:
                zero_index += 1
                if zero_index >= len(arr):
                    return arr
            arr[curr_index], arr[zero_index] = arr[zero_index], arr[curr_index]

    return arr


def remove_dups_sorted(arr):
    """
    EPI 6.6
    """

    for i in xrange(1, len(arr)):
        if arr[i] == arr[i - 1]:
            arr[i - 1] = None

    return remove_all_dups(arr, None)

# EPI 6.7 is a great problem. It shows how you can keep track of the presence or absence of an element in a very clever way. Reread it

# EPI 6.8 and 6.9 tbd

# EPI 6.10
def max_prod_butone(arr):
    is_all_positive = True

    is_all_negative = True

    num_zeros = 0
    max = -10000
    min = 10000
    num_negative = 0
    min_positive = 10000
    max_negative = -10000
    
    for i in arr:
        if i == 0:
            num_zeros += 1

        if i > max:
            max = i

        if i < min:
            min = i

        if i > 0 and i < min_positive:
            min_positive = i

        if i < 0 and i > max_negative:
            max_negative = i

        is_all_positive = is_all_positive & (i >= 0)

        is_all_negative = is_all_negative & (i < 0)

        if i < 0:
            num_negative += 1

    if num_zeros > 1:
        return 0

    if is_all_positive:
        arr.remove(min)
        return reduce(lambda x, y: x * y, arr, 1)

    if is_all_negative:
        arr.remove(max)
        return reduce(lambda x, y: x * y, arr, 1)

    if num_negative % 2 == 0:
        arr.remove(min_positive)
        return reduce(lambda x, y: x * y, arr, 1)
    else:
        arr.remove(max_negative)
        return reduce(lambda x, y: x * y, arr, 1)


# EPI 6.11
def longest_inc_subseq(arr):
    start = 0
    end = 0

    curr_start = 0
    curr_end = 0
    for i in xrange(1, len(arr)):
        if arr[i] >= arr[i - 1]:
            curr_end += 1
        else:
            if curr_end - curr_start > end - start:
                start = curr_start
                end = curr_end
            curr_start = i
            curr_end = i

    print start, end

# EPI 6.12
def get_all_primes(n):
    arr = [0] * (n + 1)

    for i in xrange(2, len(arr)):
        if arr[i] == 0:
            arr[i] = 1 # Indicates prime

            p = 2*i
            while p <= n:
                arr[p] = 2 # Conjugate
                p += i

    for i in xrange(len(arr)):
        if arr[i] == 1:
            yield i

# EPI 6.13
# Difficult problem, refer to solution
def permute(arr, p):
    swaps = 0
    temp = None

    for i in xrange(len(p)):
        temp = arr[p[i]]
        arr[p[i]] = arr[i]
        swaps += 1
        while swaps < len(arr):
            pass


#EPI 6.15
# Your intution that a rotation is basically a permutation was
# correct. Which means that you MUST do 6.13 and 6.14 and completely
# understand the solution AND the variants
# The simpler solution in the book involves reverses
# This is a phenomenal trick and should be investigated whenever
# questions on ordering arise.
def rotate(arr, r):
    arr = list(reversed(arr))
    arr = list(reversed(arr[:r])) + list(reversed(arr[r:]))

    return arr

# EPI 6.24
def pascal(n):
    arr = [1]
    for i in xrange(1, n):
        new_arr = [1]

        # compute pascal
        for j in xrange(1, len(arr)):
            new_arr += [arr[j] + arr[j - 1]]

        new_arr += [1]
        yield new_arr
        arr = new_arr

# EPI 6.26
# There is a matrix of trues and falses
# Find the row that is all false
# Suppose we are at F[i][j]
# if F[i][j] is false, good, move to j + 1
# if F[i][j] is true, it means that i knows j and i cannot be a celeb
# we don't need to move back to something less than j because we couldn't have come
# up all the way to j if F[i][j - 1] (or anything less than j - 1) was true
# This means that our celebrity candidate is now j
# so, check now for F[j][j + 1]
# This bit of code is not completely perfect. If there is no celebrity it doesn't work properly
# Of course, the problem statements state that there is 
def celebrity(F):
    i = 0
    j = 1

    while j < len(F[0]):
        if F[i][j] is False:
            j += 1
        else:
            i = j
            j += 1

    return i
