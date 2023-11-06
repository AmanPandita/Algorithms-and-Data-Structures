# import time

def factors(n):
    num = n
    x, res = 2, []
    while x <= n:
        if n % x == 0:
            res.append(x)
            n = n // x
        else:
            x += 1
    if res[-1] == num:
        res.pop()
    return res

if __name__ == '__main__':
    print(factors(23))
