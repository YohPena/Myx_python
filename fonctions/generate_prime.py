from .is_prime import is_prime

def generate_prime(limit):
    prime = []
    num = 2
    while len(prime) < limit:
        if is_prime(num):
            prime.append(num)
        num += 1
    return prime