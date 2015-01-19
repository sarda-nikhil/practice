def count_bits(n):
    cnt = 0
    while n:
        cnt += n & 1
        n = n >> 1

    print cnt

def count_bits_kr(n):
    cnt = 0
    while n:
        cnt += 1
        n = n & (n - 1)

    print cnt

