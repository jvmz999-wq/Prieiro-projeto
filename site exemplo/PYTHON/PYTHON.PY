n = cont = resp = 0
n = int(input('Qual é o numero que você quer ver a tabuada: '))
while True:
    if cont == 10:
        print('-=' * 20)
        print('Digite 0 para finalizar')
        n = int(input('Qual numero quer ver a tabuada?: '))
        if n == 0:
            break
        else:
            cont =0
    cont += 1
    resp = n * cont
    print(f'{n} x {cont} = {resp}')
print('Fim')