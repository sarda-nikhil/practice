import collections

#Given two strings a and b, find whether any anagram of string a is a sub-string of string b. For eg: 
#if a = xyz and b = afdgzyxksldfm then the program should return true.
# While this solution is correct, we need a check after the for loop (if s1_hash == s2_hash)
def anagram_substr(s1, s2):
    s2_hash = collections.defaultdict(int)
    s1_hash = collections.defaultdict(int)
    for i in s1:
        s1_hash[i] += 1
    for i in s2[:len(s1)]:
        s2_hash[i] += 1

    for i in xrange(len(s1), len(s2)):
        if s1_hash == s2_hash:
            print i - len(s1)
        ev_char = s2[i - len(s1)]
        s2_hash[ev_char] -= 1
        if s2_hash[ev_char] == 0:
            s2_hash.pop(ev_char)
        s2_hash[s2[i]] += 1

#Given a BST and a value x. Find two nodes in the tree whose sum is equal x. Additional space: O(height of the tree). It is not allowed to modify the tree
def inorder_left(tree):
    if tree is None:
        yield
    else:
        for i in inorder_left(tree.left):
            if not i is None:
                yield i
        yield tree.value
        for i in inorder_left(tree.right):
            if not i is None:
                yield i

def inorder_right(tree):
    if tree is None:
        yield
    else:
        for i in inorder_right(tree.right):
            if not i is None:
                yield i
        yield tree.value
        for i in inorder_right(tree.left):
            if not i is None:
                yield i

def two_nodes(tree, x):
    low = inorder_left(tree)
    high = inorder_right(tree)

    lowval = low.next()
    highval = high.next()

    while lowval < highval:
        if lowval + highval == x:
            return (lowval, highval)
        elif lowval + highval > x:
            highval = high.next()
        else:
            lowval = low.next()

#you are given n-strings 1you have to find whether a chain can be termed with all the strings given number n?
#A chain can be formed b/w strings if last char of the 1st string matches with 1st char of second string. For example you are given 
# Make a graph of strings and find DFS of length equal to length of array of strings
# TODO Try this again

# Given a string (1-d array) , find if there is any sub-sequence that repeats itself. 
# Here, sub-sequence can be a non-contiguous pattern, with the same relative order. 
#Eg: 
#1. abab <------yes, ab is repeated 
#2. abba <---- No, a and b follow different order 
#3. acbdaghfb <-------- yes there is a followed by b at two places 
#4. abcdacb <----- yes a followed by b twice 
#The above should be applicable to ANY TWO (or every two) characters in the string and optimum over time. 
#In the sense, it should be checked for every pair of characters in the string.
# TODO -> claims of LCS


#Determine minimum sequence of adjacent values in the input parameter array that is greater than input parameter sum. 
#Eg 
#Array 2,1,1,4,3,6. and Sum is 8 
#Answer is 2, because 3,6 is minimum sequence greater than 8.
# TODO HOLY SHIT, AWESOME PROBLEM!

#Find next higher number with same digits. 
#Example 1 : if num = 25468, o/p = 25486 
#Example 2 : if num = 21765, o/p = 25167 
#Example 3 : If num = 54321, o/p = 54321 (cause it's not possible to gen a higher num than tiz with given digits ).
# This solution is WRONG, TODO
def next_num(n):
    n = list(reversed(list(str(n))))
    curr_smallest = 0
    curr_smallest_idx = 0
    idx = 0
    print n
    while idx < len(n):
        if n[idx] > curr_smallest:
            curr_smallest = n[idx]
            curr_smallest_idx = idx
        if n[idx] < n[idx + 1]:
            n[idx + 1], n[curr_smallest_idx] = n[curr_smallest_idx], n[idx + 1]
        if idx == len(n) - 2:
            break
        idx += 1
    return ''.join(reversed(n))


# Swap with 0
# TODO

# Given a Binary Search tree of integers, you need to return the number of nodes having values between two given integers.
# You can assume that you already have some extra information at each node (number of children in left and right subtrees !!).
def upper_bd_bst(tree, upper):
    if tree.value < upper:
        return tree.num_left + upper_bd_bst(tree.right, upper)
    elif tree.value == upper:
        return tree.num_left + 1
    else:
        return 0

def bdd_bst(tree, lower, upper):
    if tree.value < lower:
        return bdd_bst(tree.right, lower, upper)
    elif tree.value > upper:
        return bdd_bst(tree.left, lower, upper)
    else:
        return upper_bd_bst(tree.right, upper) + lower_bd_bst(tree.left, lower)

# TODO While my solution is kinda ok (we get left -> and right <- and sum them), a better solution is given in careercup
