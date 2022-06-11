def transformar(x):
    aux1 = x[0:4]
    aux2 = x[5:7]
    aux3 = x[8:]
    y = aux3 + '-' + aux2 + '-' + aux1
    return y
x = input('escreva ')
y = x + 'added'
print(transformar(x))
