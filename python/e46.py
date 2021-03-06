"""
Finds the smallest number that disproves the Goldbach conjecture.
"""
from primegen import prime_by_trial
import numpy as np

def Euler_46():
    i = 2
    pr = prime_by_trial()
    while True:
        print(i)
        goldbach = False
        if ((primegen.is_prime(i)) or (i % 2 == 0)):
            goldbach = True
        for j in range(1, (int(np.sqrt((i - 2) / 2))+1)):
            if goldbach == True:
                break
            else:
                for k in primes.primes:
                    if (i == 2*(j**2) + k):
                        goldbach = True
                        break
        if goldbach == True:
            i += 1
        else:
            return i

if __name__ == "__main__":
    print(Euler_46())
