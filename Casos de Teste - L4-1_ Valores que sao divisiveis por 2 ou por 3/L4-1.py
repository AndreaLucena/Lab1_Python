inicio = int(input())
fim = int(input())

while inicio <= fim:

    if (inicio % 2 == 0) or (inicio % 3 == 0):
        print(inicio)

    inicio = inicio + 1

