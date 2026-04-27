str1 = 'ciao'
str2 = 'mondo'

print(str1 + str2) #concatenazione di 2 stringhe
print(str2 + str1) 
print(5 * 'a') #ripete per n volte un carattere
print('b' * 4)

string = 'silly walks' #le stringhe NON sono liste ma possono essere trattati come tali
for i in range(len(string)):
    print(string[i], end=' ') #stampa di tutti i caratteri della stringa, posso accedervi con l'indice. "end" è ciò che stampa alla fine di ogni ciclo

#posso farlo anche con un for-each
for character in string:
    print(character, end=' ')

print('\n')
#per fare una sub string, cioè prendere da un carattere a un carattere, si fà così
print(string[:]) #string[:] stampa tutta la stringa
print(string[:10]) #string[:x] stampa fino al x^ carattere
print(string[1:]) #string[x:] stampa dal carattere x fino alla fine
print(string[2:10]) #string[x:y] stampa dal carattere x al carattere y-1
print(string[::2]) #string[::x] stampa un carattere ogni x(ad esempio ogni 2)
print(string[3:-2]) #string[x:-y] stampa dal carattere x fino alla fine ma tolti y caratteri, nell'esempio dal carattere 3 fino alla fine tolti 2 caratteri

print("s" in string) #"in" controlla se c'è quel carattere nella stringa
print("z" not in string) #"in" controlla se non c'è quel carattere nella stringa

#le stringhe sono immutabili, però per cambiare la lunghezza si può:
pippo = "ciao"
pippo = pippo[1:] #tolgo il primo carattere
pippo += " mondo" #gli concateno qualcosa

print(pippo) #stampo la stringa modificata

#le stringhe sono immutabili ma posso cambiare una lettera all'interno così
alphabet = "abcdefghijklmnopqrstuvwxyz"
modificato = alphabet[:3]
modificato += "D"
modificato += alphabet[4:]
print(modificato)

print(min("aAbBcC")) #"min()" stampa la lettera con codepoint minore

t = [0, '1', 2]
#print(min(t)) da errore perchè funziona solo se gli elementi sono omogenei tra loro

print("aAbBcCdD".index('b')) #"index" restituisce l'indice assegnato alla lettera b, se ce ne sono 2 stampa l'indice del primo che trova

lista = list('ciao') #"list" rende l'argomento una lista

print(lista)

