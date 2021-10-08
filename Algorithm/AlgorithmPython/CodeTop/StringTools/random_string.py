import random
import string


def random_string_generator(size=10, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
	return ''.join(random.SystemRandom().choice(chars) for _ in range(size))
