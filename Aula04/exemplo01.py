# Estrutura IF
idade = int(input('Ingrese a idade da pessoa: '))
if idade >= 18:
    print('Voce e adulto')
else:
    print('voce nao e adulto')

# -------------------------------------------------

pontos = int(input('Informe os pontos: '))
if pontos >= 100:
    print('Exelente!')
elif pontos >= 50:
    print('Bom desempenho')
elif pontos >= 25:
    print('Satisfatorio')
else:
    print('Pratique mais...')

# ------------------------------------------------
# Operadores AND e OR

usuario = input('Nome: ')
senha = input('Senha: ')

if usuario == 'admin' and senha == '1234':
    print('Login realizado con sucesso')
else:
    print('Usuario ou senha incorretos')


# Exemplo IFs encadiado

nota = 10
if nota >= 9:
    print('A')
elif  nota >=7:
    print('B')
elif nota >= 5:
    print('C')
elif nota >= 3:
    print('D')
else: 
    print('E')


# Exemplo IFs nao encadiado


nota = 10
if nota >= 9:
    print('A')
if  nota >=7:
    print('B')
if nota >= 5:
    print('C')
if nota >= 3:
    print('D')
else: 
    print('E')



# Ifs aninhados

nota = float(input('Insira a nota: '))
frequencia = float (input('Informe a frequencia: '))

if nota >= 7:
    if frequencia >= 75:
         print('Aluno aprovado por nota e frequencia.')
    else:
         print('Reprovado por frequencia baixa.')
else:
    print('Reprovado por nota baixa.')
 