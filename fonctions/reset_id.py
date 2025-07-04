### 04/07/2025
### Reset the current prime id and return the next prime number 
import os

def reset_id(index_file="txt/last_prime_id.txt"):
    with open(index_file, "w") as f:
        f.write("1")
