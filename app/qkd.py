import random

def generate_qkd_key():
    return "".join([str(random.randint(0, 1)) for _ in range(128)])