# The sequence of triangle numbers is generated by adding the natural numbers.
# So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
# The first ten terms would be:
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

# Let us list the factors of the first seven triangle numbers:
#  1: 1
#  3: 1,3
#  6: 1,2,3,6
# 10: 1,2,5,10
# 15: 1,3,5,15
# 21: 1,3,7,21
# 28: 1,2,4,7,14,28

# We can see that 28 is the first triangle number to have over five divisors.

# What is the value of the first triangle number to have over 500 divisors?

# This seems like a perfect chance to try a generalized approach and
# make a tool to get all of the divisors of a given number. But first, let's
# make a thing to generate triangle numbers.

import datetime


def get_nth_triangular_number(n):
    return n * (n+1) / 2

# Let's test this against the example data:


def test_nth_triangular_number():
    checklist = (1, 3, 6, 10, 15, 21, 28, 36, 45, 55)
    for i in range(1, 11):
        if checklist[i-1] != get_nth_triangular_number(i):
            return "Test Failed: nth triangular number"
        return "Test Passed: nth triangular number"


print(test_nth_triangular_number())

# Now let's try the divisor thing


def get_divisors(n):
    # now my stupid array is mixed up so i will build and concatenate two
    divisor_set1 = []
    divisor_set2 = []
    i = 1
    # We learned that a divisor shouldn't be greater than the sqrt
    while i <= n**.5:
        if n % i == 0:
            if n / i == i:
                divisor_set1.append(i)
            else:
                divisor_set1.append(i)
                divisor_set2.append(int(n / i))
        i += 1
    # now the list is backwards!
    # also, l.reverse() doesn't make a list object
    return divisor_set1 + divisor_set2[::-1]


def test_divisors():
    checklist = [1, 2, 4, 7, 14, 28]
    divisors = get_divisors(28)
    if divisors != checklist:
        return "Test Failed: get divisors"
    return "Test Passed: get divisors"


print(test_divisors())


def solve(n):
    i = 1
    divisor_count = 1
    first_triangle = 1
    while divisor_count <= n:
        divisor_count = len(get_divisors(get_nth_triangular_number(i)))
        first_triangle = get_nth_triangular_number(i)
        i += 1
    return int(first_triangle)


def test_solve():
    if solve(5) != 28:
        return "Test Failed: solution"
    return "Test Passed: solution"


print(test_solve())

print("Attempting to solve exercise: Highly Divisible Triangular Number...")
start_time = datetime.datetime.utcnow()
print(f"Solution found: {solve(500)}")
finish_time = datetime.datetime.utcnow()
print(f"Elapsed time: {finish_time - start_time}")
