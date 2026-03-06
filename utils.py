import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, math.isqrt(n)):
        if n % i == 0:
            return False

    return True

if __name__ == '__main__':
    print(is_prime(6))
    print(is_prime(7))