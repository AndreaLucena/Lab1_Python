def real(valor):
    a = "{:,.2f}".format(float(valor))
    b = a.replace(',', 'v')
    c = b.replace('.', ',')

    return c.replace('v', '.')

moeda=float(input('DIGITE O VALOR: '))
print(f'VOCÊ DIGITOU O VALOR DE R$ {real(moeda)} REAIS..')


