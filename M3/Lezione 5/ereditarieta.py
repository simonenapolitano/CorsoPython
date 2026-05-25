class Veicolo:
    def __init__(self): 
        self.targa = 'AA000BB'
        self.velocitaMax = 50
    def __str__(self): #uguale al toString() di Java
        return 'La targa è ' + self.targa + ' - ' + str(self.velocitaMax) + 'km/h'
    def IncrementaVelocitaMax(self):
        self.velocitaMax += 10
    
class Casa:
    def __init__(self):
        self.postiLetto = 4

class VeicoloMare(Veicolo, Casa):
    def __init__(self):
        super().__init__ #Si deve sempre chiamare il costruttore della classe padre
        self.targa = 'AA000BC'
        self.velocitaMax = 70
        self.postiLetto = 4
    def aggiornaTarga(self, nuovaTarga):
        self.targa = nuovaTarga
    def IncrementaVelocitaMax(self): #Per fare l'override si ridefinisce il metodo
        self.velocitaMax += 5
    def __str__(self):
        return self.targa + ' - ' + str(self.velocitaMax) + 'km/h - '+ ' posti letto ' + str(self.postiLetto)

'''    
veicolo = Veicolo()
print(veicolo)

motoscafo = VeicoloMare()
print(motoscafo)
motoscafo.aggiornaTarga('CC00AA')
motoscafo.IncrementaVelocitaMax() #Dovrebbe aumentare di 10 ma aumenta solo di 5 perchè ho fatto l'override del metodo
print(motoscafo)

print(issubclass(VeicoloMare, Veicolo)) #"issubclass(x, y)" restituisce se la classe x è figlia della classe y
print(isinstance(motoscafo, VeicoloMare)) #"isistance(x, y)" restituisce se la l'oggetto x è istanza della classe y

veicoloMare1 = VeicoloMare()
veicoloMare2 = VeicoloMare()
veicoloMare3 = veicoloMare1
print(veicoloMare1 is veicoloMare3) #"x is y" restituisce se x ha la stessa area di memoria di y
'''

veicoloMare = VeicoloMare()
print(veicoloMare)

