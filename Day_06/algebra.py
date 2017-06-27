import math
import os


# Bu fonksiyon iki sayısal değerin toplamını hesaplamak için kullanılır.
# İki int gibi.
def sum(x, y):
    return x+y


# Variadic function sample
def sum(*numbers):
    if not len(numbers) > 0:
        return 0
    total = 0
    for n in numbers:
        total += n
    return total


# Calculate a Circle space
def circleSpace(r):
    return math.pi*r*r


class player:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def display(self):
        print("Name : ", self.name,  ", Level: ", self.level)

# test scripts
print(sum(2, 3))
print(sum(1, 3, 5, 7, 9, 11))
print(circleSpace(10))
throll = player("Throll", 22)
throll.display()
