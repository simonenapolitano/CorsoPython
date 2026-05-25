print('== ARRAY ==')

pilaArray = []

#Inserimento/lettura/cancellazione
pilaArray.append(4) 
print(pilaArray[-1]) #"-1" significa prendi l'ultimo
del pilaArray[-1] #Cancellazione ultimo elemento

print('== CLASSE ==')

class PilaClasse:
    def __init__(self):
        self.pilaLista = []
    
    def push(self, val): #il self va sempre messo
        self.pilaLista.append(val)
    
    def pop(self):
        val = self.pilaLista[-1]
        del self.pilaLista[-1]
        return val

    def getLenStack(self):
        return len(self.pilaLista)

miaPilaLista = PilaClasse()
miaPilaLista.push(3) #come argomento, il "self" non si passa
print(miaPilaLista.getLenStack(), 'elementi nella lista 1')
miaPilaLista.pop()
print(miaPilaLista.getLenStack(), 'elementi nella lista 1')

miaPilaLista1 = PilaClasse()
miaPilaLista1.push(6)
miaPilaLista1.push('abc')

miaPilaLista2 = PilaClasse()
miaPilaLista2.push(7)
miaPilaLista2.push('xyz')
miaPilaLista2.pop()
print(miaPilaLista2.getLenStack(), 'elementi nella lista 2')

print(miaPilaLista1.__dict__) #"__dict__" elenca gli elementi della classe

class PilaAvanzata(PilaClasse): #Ereditarietà, PilaAvanzata è una sottoclasse di PilaClasse
    objectCounter = 0 #Dichiarazione di una variabile di classe, come le variabili statiche in Java
    def __init__(self, a = 0, b = 0, c = 2):
        PilaClasse.__init__(self) #Come il "super" in Java, il costruttore di una sottoclasse si fa sempre così
        PilaAvanzata.objectCounter+=1

        #attributi della classe
        self.primo = a
        self.secondo = b
        self.terzo = c

        self.__quarta = 5 #variabile privata
        if a == 8:
            self.d = 91
        else: 
            self.f = 78 #Si può decidere in runtime se una proprietà esiste oppure no
        
    def pop(): #Se ridefinisco una funzione dentro una sottoclasse faccio l'"@Override" di Java in automatico
        print('altro')

    def getSomma(self):
        sum = 0
        for e in self.pilaLista:
            sum+=e
        return sum

    def getObjectCounter(self):
        return PilaAvanzata.objectCounter


miaPilaAvanzata1 = PilaAvanzata()
miaPilaAvanzata2 = PilaAvanzata()

miaPilaAvanzata1.push(6)
miaPilaAvanzata1.push(7)
print(miaPilaAvanzata1.getSomma())

print(miaPilaAvanzata1.getObjectCounter()) #Oggetti diversi della stessa classe condividono le stesse variabili di classe
miaPilaAvanzata1.pippo = 10 #nuova variabile dell'oggetto, solo di questo oggetto
print(miaPilaAvanzata1.pippo)

'''
miaPilaAvanzata1.pilaAvanzataInterna = PilaAvanzata() #Posso creare pile avanzate dentro pile avanzate all'infinito
miaPilaAvanzata1.pilaAvanzataInterna.push(67) #Avrà anche tutti i metodi della classe!!!
'''

miaPilaAvanzata3 = PilaAvanzata(4, 5, 6) #In ordine
miaPilaAvanzata4 = PilaAvanzata(b=4, c=5, a=6) #Non in ordine, si specifica il nome dei parametri

print(miaPilaAvanzata4.primo)
print(miaPilaAvanzata4.__dict__) #Se invoco __dict__ le variabili private le vedo
#print(miaPilaAvanzata4.__quarta) #"__quarta" NON è visibile, quindi stampabile
print(miaPilaAvanzata4._PilaAvanzata__quarta) #Così si può stampare

miaPilaAvanzata5 = PilaAvanzata(8,6,7)
print(hasattr(miaPilaAvanzata5, 'd')) #"hasattr" restituisce vero se l'oggetto ha quell'attributo