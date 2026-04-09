nota = float(input('Insira a nota: '))
frequencia = float (input('Informe a frequencia: '))

if nota >= 7:
    if frequencia >= 75:
         print('Aluno aprovado por nota e frequencia.')
    else:
         print('Reprovado por frequencia baixa.')
else:
    print('Reprovado por nota baixa.')
 