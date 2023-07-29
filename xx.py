# prime number from 1 to 100

def prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

for i in range(2, 100):
    if prime(i):
        print(i, end=' ')
print()


# Path: xx.py
