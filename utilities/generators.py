import random
import string
def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
def random_string_generator(size=8, chars=string.ascii_uppercase):
    return ''.join(random.choice(chars) for x in range(size))
def random_num_generator(size=8, chars=string.digits):
    return ''.join(random.choice(chars) for x in range(size))