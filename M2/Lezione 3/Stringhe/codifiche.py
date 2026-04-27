phrase = "Hello \nworld!"
print(len(phrase)) #len(stringa) restituisce la lunghezza di una stringa
print(phrase)

print(ord('A')) #lettera -> codepoint
print(chr(65)) #codepoint -> lettera
print(ord('\n'))

stringaMultilinea = """Oggi e' una bella giornata di sole e 
noi siamo qui a studiare Python!!!""" #così si fanno le stringhe multilinea

print(len(stringaMultilinea)) #stampa il numero dei caratteri + 1(il carattere a capo)