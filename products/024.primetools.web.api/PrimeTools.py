#!/usr/bin/python3
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

if __name__ == "__main__":
    import argparse
    desc = "PrimeTools Python Module - a part of 2019 100 Days of Coding"
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument("-p", type=int, help="determine primality (default)")
    parser.add_argument("-n", type=int,  help="calculate n-th prime number")
    parser.add_argument("--nearest", type=int, help="calculate nearest prime number")
    parser.add_argument("--neighbors", type=int, help="calculate neighboring prime numbers")
    parser.add_argument("-f", "--factorize", type=int, help="calculate prime factors")
    parser.add_argument("-v", action="count", default=0, help="Increase output verbosity")
    args = parser.parse_args()
    if args.n:
        if args.v > 2:
            # TODO: present ordinals as plain text (1st, 2nd, 3rd, 4th, etc)
            print("Where n=" + str(args.n) +", the n-th prime number is", get_nth(args.n))
        elif args.v == 2:
            print("get_nth("+str(args.n)+"): "+str(get_nth(args.n)))
        elif args.v == 1:
            print(str(args.n)+": "+str(get_nth(args.n)))
        else:
            print(get_nth(args.n))
    elif args.neighbors:
        if args.v > 2:
            print("The prime numbers neighboring "+str(args.neighbors)+" are:", get_neighbors(args.neighbors))
        elif args.v == 2:
            print("get_neighbors("+str(args.neighbors)+"): "+str(get_neighbors(args.neighbors)))
        elif args.v == 1:
            print(str(args.neighbors)+": "+str(get_neighbors(args.neighbors)))
        else:
            print(get_neighbors(args.neighbors))
    elif args.factorize:
        if args.v > 2:
            # TODO: present list list as plain text
            print("The prime factors of "+str(args.factorize)+" are:", factorize(args.factorize))
        elif args.v == 2:
            print("factorize("+str(args.factorize)+"): "+str(factorize(args.factorize)))
        elif args.v == 1:
            print(str(args.factorize)+": "+str(factorize(args.factorize)))
        else:
            print(factorize(args.factors))
    elif args.nearest:
        if args.v > 2:
            print("The prime number nearest "+str(args.nearest)+" is", get_nearest(args.nearest)[0])
        elif args.v == 2:
            print("get_nearest("+str(args.nearest)+"): "+str(get_nearest(args.nearest)[0]))
        elif args.v == 1:
            print(str(args.nearest)+": "+str(get_nearest(args.nearest)[0]))
        else:
            print(get_nearest(args.nearest)[0])
    elif args.p:
        if args.v == 0:
            print(is_prime(args.p))
        elif args.v == 1:
            print(str(args.p)+": "+str(is_prime(args.p)))
        elif args.v == 2:
            print("is_prime("+str(args.p)+"): "+str(is_prime(args.p)))
        elif args.v > 2:
            if is_prime(args.p):
                print(str(args.p), "is a prime number.")
            else:
                print(str(args.p), "is not a prime number.")
