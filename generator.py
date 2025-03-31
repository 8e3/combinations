import itertools
import string

def generate_combinations(filename="combinations.txt"):
    chars = string.ascii_lowercase
    with open(filename, "w") as f:
        f.writelines("".join(combo) + "\n" for combo in itertools.product(chars, repeat=5))

if __name__ == "__main__":
    generate_combinations()
