from random import *

#seed(4) il seed è la base da cui genera i numeri random

'''
for i in range(5):
    # print(random())
    print(randrange(1, 7)) #(inizio(incluso), fine(escluso))
    print(randint(1, 7)) #(inizio, fine) entrambi inclusi
'''

miaLista = [2, 6, 567, 'pippo', 'ciao']
print(choice(miaLista)) #"choice(miaLista)" fa una scelta casuale di un elemento della lista
print(sample(miaLista, 2)) #"sample(miaLista, n)" prendi n valori a caso da una lista e li scrivi