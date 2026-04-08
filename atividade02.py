a = float(input('Insira o valor da compra: '))
p = input('Informe a forma de pagamento (vista o parcelado): ').lower()
if a > 250.00 and p == 'vista':
    d = 0.16*a
    v = a - d
    print(f'O valor com o desconto aplicada e: {v}')
else:
    print(f'O valor da compra e: {a}')