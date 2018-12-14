'''
# 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
def largest_prime(n):
    def factors(n):
        result = set()
        for i in range(1, int(n ** 0.5) + 1):
            div, mod = divmod(n, i)
            if mod == 0:
                result |= {i, div}
        return result

    primes = []
    all_factors = factors(n)

    for factor in all_factors:
        prime_check = factors(factor)
        if len(prime_check) == 2:
            primes.append(factor)
    print(max(primes))


# Tests
largest_prime(13195)
largest_prime(600851475143)
'''
>>> # 5, 7, 13 ,29 are factors of 13195. 29 is the largest prime
>>> [29]
>>> [5]
'''
