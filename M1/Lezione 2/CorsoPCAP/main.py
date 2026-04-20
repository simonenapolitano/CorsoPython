import myModule1 #i moduli sono dei file, quando vengono importati vengono anche eseguiti
import myModule2 #se il modulo è già importato da un altro modulo non verrà eseguito 2 volte

'''
myModule1.miaFunzione() #chiamo la funzione dal modulo creato da me
print(myModule1.a) #"a" è stata inizializzata come 4, quindi stamperà 4
'''

'''
print(dir(myModule1))
print(myModule1.__name__) #se invoco la variabile main da un altro file che importa quel modulo __name__ avrà il nome del modulo
print(myModule1._b) #stampa comunque anche se secondo la convenzione è privata
'''

#adesso spostiamo i moduli in una directory diversa
import sys #per re-importarli dobbiamo agire sul sys
sys.path.append("..\\modules") #alla lista sys.path gli aggiungiamo la cartella modules per farla vedere da "main.py"
import modules.myModule1 #adesso per importarlo devo anche specificare la directory modules

