import math

"""
try:
    x=float(input("Inserisci un numero: "))
    y = math.sqrt(x)
    print("La radice quadrata di [" + x + "] e' [" + y + "]")
except ValueError: #come il try-catch di java, cattura la "ValueError"
    print("Valore inserito non numerico!")
except:
    print("Si è vericato un errore!")
"""

try:
    value = 3
    value /= 0

except ZeroDivisionError:
    print("Divisione per zero non consentita!")
except:
    print("Si è verificato un errore!")

raise #"raise" 'solleva' un'eccezione, cioè la chiama

assert x >= 0 #"assert" serve per il testing, si accerta che dell'espressione che segue