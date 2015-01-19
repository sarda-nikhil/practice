class Tree():
    left = None
    right = None

    value = None

    def __init__(self, left, right, value):
        self.left = left
        self.right = right
        self.value = value

def create_tree():
    a = Tree(Tree(Tree(None, None, 1), Tree(None, None, 3), 2),Tree(Tree(None, None, 5), Tree(None, None, 7), 6),4)

    return a

def in_order(t):
    if t is None:
        yield
    else:
        for i in in_order(t.left):
            yield i
        yield t.value
        for i in in_order(t.right):
            yield i

def in_order_stack(t):
    # This is a really bad implementation
    # See how this is done in test_generators
    stack = []
    stack.append(t)

    while len(stack) > 0:
        if t.left is not None:
            stack.append(t.left)
            t = t.left
            continue
        
        yield t.value

        try:
            t = stack.pop()
        except:
            return

        while t.right is None:
            try:
                t = stack.pop()
            except:
                return
            yield t.value

        stack.append(t.right)
        t = t.right

