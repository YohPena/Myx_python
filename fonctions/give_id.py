### 04/07/2025
### Read the current prime id and return the next prime number 

from sympy import prime
import os

def give_id(index_file="txt/last_prime_id.txt"):
    if os.path.exists(index_file):
        with open(index_file, "r") as f:
            index = int(f.read().strip())
    else:
        index = 1

    prime_id = prime(index)

    with open(index_file, "w") as f:
        f.write(str(index + 1))

    return prime_id
