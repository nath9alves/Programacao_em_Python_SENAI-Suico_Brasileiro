"""# Um Outro Uso do Print"""

print('Meu nome é', 'Python', 'Ok?')    # Ele exibe as três strings de forma unida

print('Meu nome é', 'Python', 'Ok?', sep=' $$ ')     # com sep='texto' ao final do código é realizada a separação

print('Meu nome é Python', 'Ok?')
print('Monty Python', end='   ....!')     # o comando end='texto' insere um texto ao final do código

# Programa para receber dois valores e mostrar a soma
soma1 = 5    # Exemplo de declaração de outra variável
soma2 = 4    # outro exemplo

soma = soma1 + soma2    # exemplo de operação de soma

# print(soma)    # exibição do resultado

print('O resultado de soma1 e soma2 é:', soma)    # Exibição do resultado da variável

print('O resultado de', soma1, 'mais' , soma2, 'é', soma)

# Exibindo o valor de cada variável:

print(f'O resultado de {soma1} e {soma2} é {soma}:')     # print(f {conteúdo}) serve para formatar a exibição da variável para o conteúdo dela

"""# Exercício 5 (Variáveis) com input e print(f'')

Crie um programa que recebe um valor do usuário e calcule o quadrado desse número. Em seguida, exibe o resultado.
"""

# Programa que recebe um valor do usuário

print('Início do programa...')

n1 = int(input('Terrícola, forneça um número inteiro:'))    #int para valores inteiros

quadrado = n1**2     # Elevar ao quadrado

print(f'O quadrado de {n1} é {quadrado}!')
print('Fim do programa...')
