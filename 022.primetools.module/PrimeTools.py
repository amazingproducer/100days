# All the stuff is here, but it doesn't exactly make it a module yet

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(n**.5) + 1, 2):
            if n % i == 0:
                return False
        return True

def generate():
    j = [2]
    i = 3
    while i:
        if is_prime(i):
            j.append(i)
            yield [j, j[-1]]
        i += 2

def factorize(n):
    if n <= 1:
        return ValueError("Integer must be greater than 1")
    r = n
    factors = []
    while r % 2 == 0:
        factors.append(2)
        r /= 2
    for i in range(3, int(r**.5) + 1, 2):
        while r % i == 0:
            factors.append(int(i))
            r /= i
    if r > 2:
        factors.append(int(r))
    return factors

def get_nth(n):
    if n < 1:
        return ValueError("Input must be a positive integer.")
    j = [2]
    i = 3
    while len(j) < n:
        if is_prime(i):
            j.append(i)
        i += 2
    return j[-1]

def get_neighbors(n):
    if n < 3:
        return ValueError("Integer must be greater than 3.")
    p = generate()
    q = []
    l = 0
    g = 0
    while g <= n:
        q = next(p)
        g = q[-1]
        if q[-1] == n:
            l = q[0][-2]
            q = next(p)
            g = q[-1]
        elif q[-1] > n:
            l = q[0][-3]
    return l, g

# TODO: optimize the building of r to minimize generator calls
def get_nearest(n, y=1):
    if n < 1:
        # Integer must be positive - using 1 instead
        n = 1
    p = generate()
    r = []
    s = y
    g = 0
    c = y
    z = []
    # Just grabbing up the y additional primes that are greater than n is
    # probably not the smartest approach
    while s > 0:
        q = next(p)
        r.append((q[-1], abs(q[-1] - n)))
        if q[-1] > n:
            q = next(p)
            r.append((q[-1], abs(q[-1] - n)))
            s -= 1
    for i in range(len(r) - 1):
        if r[i][1] == 0:
            r.pop(i)
    for prime, distance in sorted(r, key=lambda x: x[1]):
        if c > 0:
            z.append(prime)
            c -= 1
    return sorted(z)
