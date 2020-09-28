f = open (r'/home/theo/cursos/python/basico/03-modulo/x.txt')
for linha in f.readline():
    print (linha.strip())
f.close()

with open (r'/home/theo/cursos/python/basico/03-modulo') as f:
    print (f.read())