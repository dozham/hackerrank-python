import random
import string

PASSWORD_LENGTH = 28
random_password = ''.join(random.choices(string.printable[:-6], k=PASSWORD_LENGTH))
print(random_password)
