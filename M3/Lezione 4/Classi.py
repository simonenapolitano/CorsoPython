class ClasseProva: #Per dichiarare una classe si usa la parola chiave "class"
    def __init__(self): #Costruttore della classe, il self è come il this, è obbligatorio
        print('Hello world!')

oggetto = ClasseProva() #Così si istanzia un oggetto

class ClasseDue:
    def __init__(self, val = 1): #Se l'utente non passa nessun parametro nel costruttore val è gia inizializzato a 1
        print(val)