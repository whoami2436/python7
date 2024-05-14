import random
import math

def numbers ():
    nums = [random.randint(20 , 50) for _ in range(5)]
    return [math.pow (x , 2) for x in nums if x % 2 == 0]

Coders = numbers()
print(Coders)