import fun

print("inserisci la lunghezza minima della password:")
min = int(input())
print("inserisci ora la lunghezza massima:")
max = int(input())

psw = fun.generate(min,max)
print("La tua password è: {0}".format(psw))