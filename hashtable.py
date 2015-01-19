# EPI 13.1 -> fairly easy problem, once you understand what they want

# EPI 13.2
# Remember how to clone a list in Python, geez
def get_palindromes(s):
    # To make shit like this DP, get a hash and store it
    # in the beginning of the function check if we already seen args in hash, if so return that
    # Just before yielding, store args we are passing to recursive func and chain hash the yielded value into hash table 
    def gen_palin(c, odd_char):
        if len(c) == 2:
            yield c[0] + odd_char + c[1]
        else:
            for i in c:
                t = c[:]
                t.remove(i)
                t.remove(i)
                for j in gen_palin(t, odd_char):
                    yield i + j + i

                    
    s = sorted(s)
    idx = 0
    odd_char = None

    while idx <= len(s) - 1:
        if s[idx] == s[idx + 1]:
            idx += 2
        else:
            if odd_char is None:
                odd_char = s[idx]
                idx += 1
            else:
                break

    if idx < len(s) - 1:
        return False

    c = str(''.join(s)).replace(str(odd_char), '', 1)

    return [i for i in gen_palin(list(c), odd_char)]

# EPI 13.3 Really easy

# EPI 13.4
# Interestingly, they use the same technique as in the search algorithm, make a twisted use of the space complexity constraint
# The idea being that if you use more memory than needed, you can get away scotfree with an amortized op argument (ie, we only do this once every n operations)
# The canonical solution is to use a hashmap combined with a linkedlist

# EPI 13.5
# TODO

# EPI 13.6
# Remember that order statistics based question -> heap or selection algorithm first
# Then use the lazy garbage collection method for amortized argument

# EPI 13.7
# For every two points, blah blah blah

# Look at some hashing operations: rolling hash, locality sensitive hash, and for the heck of it consistent hash
