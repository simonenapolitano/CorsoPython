import math

'''
print(math.pi)
print(math.sin(math.pi/2))
'''

#print(dir(math)) stampo la directory della libreria math con tutte le sue entities

'''
miaLista = [1, 5, 6, 'pippo']

for mioElemento in dir(math): #come il for-each di java, stampa ogni elemento nella lista di entities dentro la libreria math
    print(mioElemento)
'''

'''
for i in range(2, 9, 2): #range(inizio(incluso), fine(escluso), step(numero che aggiunge ogni ciclo al valore iniziale))
    print(i)
'''

'''
print("Pigreco:", math.pi)
pi = 5 #tratta come una variabile diversa da math.pi
print("Variabile pi:", pi)
print("Pigreco non modificato", math.pi)
math.pi = 7 #in python NON esistono costanti, tutto è modificabile
print("Pigreco modificato:", math.pi)
'''

'''
COSTANTE = 5 #due convenzioni per dichiare le "costanti"
_costante = 5
'''

'''
def sin(x): #dichiarazione della funzione
    print("Ciao", x, sep="--") #sep="--" è il separatore tra le due stringhe concatenate, in questo caso --

sin("Pippo") #chiamo la funzione sin

math.sin = 8 #tratta la funzione sin(del modulo math) come una variabile 
print(math.sin) 
'''

