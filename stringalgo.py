def basic_regex(reg, s):
    # Re read the princeton notes
    # Look really carefully at the match_star. Why does this work?
    # The match_star code can be optimized

    def match_star(reg, s):
        if s == '':
            if len(reg) > 2:
                return False
            return True

        if len(reg) > 2 and (reg[2] == s[0] or reg[2] == '.'):
            return match(reg[2:], s)
        
        if s[0] == reg[0] or reg[0] == '.':
            return match_star(reg, s[1:])
        else:
            return match(reg[2:], s)


    def match(reg, s):
        if reg == '':
            return True

        if len(reg) > 1:
            if reg[1] == '*':
                return match_star(reg, s)

        if reg[0] == '$':
            return s == ''

        if reg[0] == '.' or reg[0] == s[0]:
            return match(reg[1:], s[1:])
        
        return False

    if reg[0] == '^':
        return match(reg[1:], s)

    for i in xrange(len(s)):
        if match(reg, s[i:]):
            return True

    return False

assert (basic_regex(".", "a"));
assert (basic_regex("a", "a"));
assert (not basic_regex("a", "b"));
assert (basic_regex("a.9", "aW9"));
assert (not basic_regex("a.9", "aW19"));
assert (basic_regex("^a.9", "aW9"));
assert (not basic_regex("^a.9", "baW19"));
assert (basic_regex(".*", "a"));
assert (basic_regex(".*b", "abc"));
assert (basic_regex("c*", "c"));
assert (not basic_regex("aa*", "c"));
assert (basic_regex("ca*", "c"));
assert (basic_regex(".*", "asdsdsa"));
assert (basic_regex("9$", "xxxxW19"));


assert (basic_regex(".*a", "ba"));
assert (basic_regex("^a.*9$", "axxxxW19"));

assert (basic_regex("^a.*W19$", "axxxxW19"));
assert (basic_regex(".*a.*W19", "axxxxW19123"));
assert (not basic_regex(".*b.*W19", "axxxxW19123"));
assert (basic_regex("n.*", "n"));
assert (basic_regex("a*n.*", "an"));
assert (basic_regex("a*n.*", "ana"));
assert (basic_regex("a*n.*W19", "anaxxxxW19123"));
assert (basic_regex(".*a*n.*W19", "asdaaadnanaxxxxW19123"));
assert (basic_regex(".*.*.a*n.*W19", "asdaaadnanaxxxxW19123"));

def rle(stri):
    # RLE implementation
    rle = stri[0]
    cnt = 1
    for i in stri[1:]:
        if i == rle[-1]:
            cnt+=1
        else:
            if cnt > 1:
                rle += str(cnt)
                cnt = 1
            rle += i
    
    if cnt > 1:
        rle += str(cnt)

    print rle

def is_palindrome(stri):
    return stri == reduce(lambda x, y: x + y, reversed(stri), '')

def replace_q_with_num(s):
    if s is None or s is '':
        return s

    qs = s.count('?')

    if qs == 0:
        return s

    results = []
    for i in xrange(2**qs):
        bin_repr = bin(i)[2:]
        bin_repr = '0' * (qs-len(bin_repr)) + bin_repr

        q_cnt = 0
        temp_s = s[:]

        for j in xrange(len(temp_s)):
            if temp_s[j] == '?':
                temp_s = temp_s.replace('?', bin_repr[q_cnt], 1)
                q_cnt += 1

        results += [temp_s]

    return results

def kmp(s1, s2): # Matches s1 with s2, ie construct partial match table of s1
    # http://jakeboxer.com/blog/2009/12/13/the-knuth-morris-pratt-algorithm-in-my-own-words/
    def create_match_table(s1):
        t = [0] * len(s1)
        k = 0
        for i in xrange(1, len(s1)):
            if s1[i] == s1[k]:
                k += 1
            else:
                while k > 0 and s1[i] != s1[k]:
                    k = t[k - 1]
            t[i] = k
        return t

    prefix_table = create_match_table(s1)
    offsets = []
    idx = 0

    while idx < len(s1):
        t1_idx = idx
        t2_idx = 0

        while s1[t1_idx] == s2[t2_idx]:
            t1_idx += 1
            t2_idx += 1
        
            if t2_idx == len(s2) or t1_idx == len(s1):
                break

        if t2_idx < len(s2):
            if t1_idx - idx > 0:
                idx += (t1_idx - idx) - prefix_table[t1_idx - idx - 1]
                continue
        else:
            offsets += [idx]

        idx += 1

    return offsets


def boyer_moore(s1, s2): # Forget implementation, too complex. Get the basic idea
    pass

def rabin_karp(s1, s2): # Hashing solution. The tricky thing here are the indices and computing the rolling hash
    def compute_hash(s, base):
        p = len(s) - 1
        h = 0
        for i in s:
            h += ord(i) * (base ** p)
            p -= 1
        return h

    hash_s1 = compute_hash(s1[:len(s2)], 256)
    hash_s2 = compute_hash(s2, 256)
    offsets = []

    for i in xrange(len(s1) - len(s2) + 1):
        if hash_s1 == hash_s2:
            if s1[i:i+len(s2)] == s2:
                offsets += [i]
        if i < len(s1) - len(s2):
            hash_s1 = 256 * hash_s1 + ord(s1[i + len(s2)]) - ord(s1[i]) * (256 ** (len(s2)))

    return offsets

# The algo for matching a set of strings is awesome. It uses a bloom filter

# Understand suffix tries
