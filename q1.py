def c(a):
    temp_high = [None] * len(a) #1, a1, a1*a2, a1*a2*a3
    temp_low = [None] * len(a)  #a2*a3*a4, a3*a4, a4, 1

    for i in xrange(len(a)):
        if i == 0:
            temp_low[0] = 1
            temp_high[len(a) - 1] = 1
        else:
            temp_low[i] = temp_low[i-1]*a[i-1]
            temp_high[len(a) - i - 1] = temp_high[len(a) - i]*a[len(a) - i]

    b = []
    print temp_low
    print temp_high
    for i in xrange(len(a)):
        b += [temp_low[i] * temp_high[i]]

    print b
