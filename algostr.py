#EPI 7.1
def strtonum(s):
    i = len(s) - 1
    num = 0
    pow = 0
    while i >= 0:
        if s[i] == '-':
            if i != 0:
                print "Nope"
                return
            return -num
        num += int(s[i]) * 10 ** pow
        i -= 1
        pow += 1

    return num

# EPI 7.2
def replandrem(s):
    def repl(n):
        if n == 'a':
            return 'dd'
        elif n == 'b':
            return ''
        else:
            return n

    return ''.join(map(repl, list(s)))

# EPI 7.3
def test_palindromicity(s):
    s = s.lower()
    i = 0
    j = len(s) - 1

    alpha = 'abcdefghijklmnopqrstuvwxyz'

    while i < j:
        while s[i] not in alpha:
            i += 1
        while s[j] not in alpha:
            j -= 1

        if s[i] != s[j]:
            return False

        i += 1
        j -= 1

    return True

# EPI 7.4
# Easy problem but gave a lot of trouble. Be careful about
# using too many higher order functions
def reverse_words(s):
    return ' '.join(list(reversed(s.split(' '))))

# EPI 7.5
# This solution uses generators. Revisit problem and see if
# there is a slicker way to solve it
def compute_all_mnemonics(n, M):
    if n is '':
        yield ''
    else:
        for i in M[n[0]]:
            for j in compute_all_mnemonics(n[1:], M):
                yield i + j

# EPI 7.6
def look_and_say(n):
    current = n[0]
    count = 1
    res = ''
    for i in n[1:]:
        if current != i:
            res += str(count) + str(current)
            current = i
            count = 1
        else:
            count += 1

    res += str(count) + str(current)
    return res


# EPI 7.7 Roman to Decimal

# EPI 7.8
# This is a very tricky problem mainly because of the edge cases.
# The enumeration is not that difficult
def get_all_valid(m):
    if len(m) > 12:
        return "Too long"

    def gen_valid(m, d):
        if m == '':
            yield None
        elif m[0] == '0':
            for v in gen_valid(m[1:], d - 1):
                yield '0' + '.' + v
        elif d == 0:
            if len(m) > 3 or int(m) > 255:
                yield None
            else:
                yield m
        else:
            for i in xrange(1, 4):
                if int(m[:i]) > 255:
                    yield None
                else:
                    for v in gen_valid(m[i:], d - 1):
                        if v is not None:
                            yield m[:i] + '.' + v

    return [i for i in gen_valid(m, 3)]

# EPI 7.9
# This is a perfect example of an easy question that once someone is tired enough
# will completely miss the easy solution to.
# While the brute force solution was thought of (maintain 3 arrays), we should have
# noticed the periodicity of the index when it goes into the array

# EPI 7.11
def encode_elias(n):
    res = ''
    for i in n:
        repr = bin(i)[2:]
        res += '0' * (len(repr) - 1) + repr
    return res

# Decode alias had some bugs in it, specifically, missing the cnt_zero + 1 part
def decode_elias(m):
    cnt_zero = 0
    res = []

    i = 0

    while i < len(m) - 1:
        if m[i] == '0':
            cnt_zero += 1
            i += 1
        else:
            n = m[i:i+cnt_zero+1]
            i += cnt_zero + 1
            cnt_zero = 0
            res += [int(n, 2)]

    return res


# EPI 7.12
# Look at the unix tail implementation 0_o

# EPI 7.13
# This is another tricky problem. Note the first if condition. Each word must
# be followed by at least one space. This problem required a few iterations but
# the changes were fairly minute.
def justify(n, L):
    curr_line = []
    curr_size = 0

    for i in n.split(' '):
        if curr_size + len(i) + 1 < L:
            curr_line += [i]
            curr_size += len(i)
        else:
            spaces = L - len(''.join(curr_line))

            space_per_word = spaces / (len(curr_line) - 1)
            line = ''
            for j in curr_line[:len(curr_line) - 1]:
                line += str(j) + ' ' * space_per_word

            line += ' ' * (L - len(line) - len(str(curr_line[-1]))) + curr_line[-1]

            print line

            curr_line = [i]
            curr_size = len(i)

    if curr_line != []:
        l = ' '.join(curr_line)
        l += ' ' * (L - len(l))
        print l

# EPI 7.14
# Hoo boy, string search algorithms. Look at the varieties there are.

