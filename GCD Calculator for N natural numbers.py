import math


def gcd(a, b):
    if a == 0 or b == 0:
        return 1
    if a == b:
        return a
    else:
        n1 = min(a, b)
        n2 = max(a, b)
        if n2 % n1 == 0:
            return n1
        rem = n2
        r = []
        while (rem != 0):
            rem = n2 % n1
            q = n2 // n1
            r += [rem]
            print(n2, ' = ', q, '*', n1, ' + ', rem)
            n2 = n1
            n1 = rem
        return r[len(r) - 2]


def generalizedGCD(n, a):
    if n == 1:
        return a[0]
    elif n > 1:
        pairs = int(math.ceil(n / 2))
        i = 0
        a2 = []
        while (i < n):

            if i != n - 1:
                a2 += [gcd(a[i], a[i + 1])]
                #print('\n\n', a[i], a[i + 1])
                i += 2
            else:
                a2 += [a[i]]
                i += 1
        #print(pairs, a2)

        return (generalizedGCD(len(a2), a2))


print('GCD = ', generalizedGCD(3, [12, 24, 48, 96]))
print('GCD = ', generalizedGCD(5, [2, 3, 4, 5, 6]))
print('GCD = ', generalizedGCD(5, [2, 4, 6, 8, 10]))
