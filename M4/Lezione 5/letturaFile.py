try:
    stream = open("Lezione 5\\mieiFile\\prova.txt", "rt") #Aprire file in modalità lettura(rt)
    content = stream.read() #Leggere tutto quello nel file
    print(content)
    stream.close()
    stream = open("Lezione 5\\mieiFile\\provaScrittura.txt", "wt") #Aprire file in modalità scrittura(wt)
    for i in range(10):
        stream.write(str(i))
    stream.close()
except Exception as exc:
    print('cannot open file')