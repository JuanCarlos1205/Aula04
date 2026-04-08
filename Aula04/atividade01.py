a = float(input('Insira o valor da compra: '))
if a > 250.00:
    d = 0.16*a
    v = a - d
    print(f'O valor com o desconto aplicada e: {v}')
else:
    print(f'O valor da compra e: {a}')

