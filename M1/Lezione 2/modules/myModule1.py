import myModule2 #quando importo questo modulo(myModule1) viene eseguito anche myModule2 perchè lo importo qua

print("Hello world!")
a = 4
_b = 5 #convenzione per dichiare le variabili private, non è veramente privata in realtà, tutti possono accedervi

print(__name__) #viene inizializzato a __main__

if(__name__ == "__main__"):
    print("Sono stato invocato dall'interno")
else:
    print("Sono stato invocato da qualcun altro")

def miaFunzione():
    print("Hello function!")

__counter = 0

def somma(lista):
    global __counter #"global" serve per fare riferimento alla "__counter" sopra
    __counter += 1
    somma = 0
    for elemento in lista:
        somma += elemento
    return somma