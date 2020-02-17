def primeF(n):
    i = 2
    while i*i < n:
        while n%i == 0:
            n /= i
        i += 1
    return n
primeF(600851475143)