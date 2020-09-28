f = open(r'/home/theo/cursos/python/basico/03-modulo/x.txt', 'w')
for linha in range(1, 101):
    f.write(f'{linha}\n')
f.close()