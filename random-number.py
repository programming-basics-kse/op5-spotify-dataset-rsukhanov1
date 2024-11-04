import random


def random_number_in_base(base, length):
    digits = '0123456789ABCDEF'[:base]  # Valid digits for the base
    return ''.join(random.choice(digits) for _ in range(length))

def main():
    base = random.randint(2, 16)
    length = random.randint(1, 8)
    random_number = random_number_in_base(base, length)
    print(f"Generated base: {base}")
    print(f"Random number in base {base}: {random_number}")


if __name__ == "__main__":
    main()
#https://numeral-systems.com/converter/

# Generated base: 15
# Random number in base 15: A7047D