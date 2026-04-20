'''
import math as m #alias del modulo, invece di scrivere math scrivo m

print(m.pi)
print(m.sin(m.pi/2))
'''

from math import pi, sin #dal modulo posso importare solo certe entities

from math import pi as pigreco, sin as seno #posso usare gli alias anche su entities importate

def sin(x):
    print("hello", x)

print(seno(pigreco/2))
sin("Pippo")



 