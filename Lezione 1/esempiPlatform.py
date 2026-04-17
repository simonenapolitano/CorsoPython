from platform import *
'''
print(platform()) #restituisce informazioni sul sistema operativo

print(machine()) #restituisce il nome generico della CPU
print(processor()) #restituisce informazioni sulla CPU
print(version()) #restitisce la versione del sistema operativo
'''

print(python_implementation()) #restituisce il linguaggio in cui e' stato scritto l'interprete, ad esempio CPython in C

for atr in python_version_tuple(): #restituisce la major(3), la minor(14) e la patch(4) della versione di python 3.14.4
    print(atr)