import os
from .generate_prime import generate_prime

def save_prime(limit, dossier="txt", filename="list_prime_numbers.txt"):
    # Crée le dossier s'il n'existe pas
    if not os.path.exists(dossier):
        os.makedirs(dossier)

    path = os.path.join(dossier, filename)
    prime = generate_prime(limit)
    with open(path, "w") as f:
        for p in prime:
            f.write(str(p) + "\n")