from string import ascii_letters, punctuation, digits
from random import choice, randint


def generate(min,max):
    string_format = ascii_letters + punctuation
    return "".join(choice(string_format) for x in range(randint(min,max)))