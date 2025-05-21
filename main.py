import random

key = "BACON-" + str(random.randint(1000, 9999))
with open("key.txt", "w") as f:
    f.write(key)
