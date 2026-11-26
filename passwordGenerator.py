import random
upper = chr(random.randint(65,90))
upper2 = chr(random.randint(65,90))
lower = chr(random.randint(97,122))
lower2 = chr(random.randint(97,122))
digit = chr(random.randint(48,57))
digit2 = chr(random.randint(48,57))
punctuation = chr(random.randint(33,152))
punctuation2 = chr(random.randint(33,152))
password = upper + upper2 + lower + lower2 + digit + digit2 + punctuation + punctuation2
print(password)