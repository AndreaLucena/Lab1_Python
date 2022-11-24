#entrada de dados
inicio = int(input())
fim = int(input())
n = int(input())

if n % 3 != 0:
    n = int(input())
    continue

else:

    start = 11
    end = 25

    for i in range(inicio, fim + 1):
        if i > 1:
            for j in range(2, i):
                if (i % j == 0):
                    break
            else:
                print(i)

