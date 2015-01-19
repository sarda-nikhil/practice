def op_add():
    a = stack.pop()
    b = stack.pop()
    stack.append(a+b)

def op_min():
    a = stack.pop()
    b = stack.pop()
    stack.append(a-b)

def op_mul():
    a = stack.pop()
    b = stack.pop()
    stack.append(a*b)

def op_div():
    a = stack.pop()
    b = stack.pop()
    stack.append(a/b)

def op_pow():
    a = stack.pop()
    b = stack.pop()
    stack.append(a^b)

op_tokens = {
    '+': op_add,
    '-': op_min,
    '*': op_mul,
    '/': op_div,
    '^': op_pow
    }

stack = []


def evalrpn(rpn_expr):
    for i in rpn_expr:
        if i in op_tokens:
            op_tokens[i]()
        else:
            stack.append(int(i))

    print stack.pop()

ops = ['(', ')', '+', '-', '*', '/', '^']

def tokenize(expr):
    token = ''
    for i in expr:
        if i in ops:
            yield token
            token = ''
            yield i
        else:
            token += i

    if token is not '':
        yield token
