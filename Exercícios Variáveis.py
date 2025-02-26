# @title Exercício 1 - Variáveis (soma) 
#Crie um programa para receber dois valores e em seguida exiba a soma deles


# Programa para receber dois valores e mostrar a soma
soma1 = 5    # Exemplo de declaração de outra variável
soma2 = 4    # outro exemplo

soma = soma1 + soma2    # exemplo de operação de soma

# print(soma)    # exibição do resultado

print('O resultado de soma1 e soma2 é:', soma)    # Exibição do resultado da variável
print('O resultado da soma é:' + soma)     # exibição de erro <--------------

#----------------------------------------------------------------------------------------------

# @title Exercício 2 - Variáveis (diferença)
#Crie um programa que recebe dois valores e em seguida exiba a diferença deles

menosum = 56
meosdois = 23.9

um_menos_dois = menosum - meosdois

print('O resultado da subtração é:', um_menos_dois)

#----------------------------------------------------------------------------------------------

# @title Exercício 3 - Variáveis (divisão)
#Crie um programa que recebe dois valores e em seguida exibe o quociente deles

divide1 = 100
divide2 = 20

divisao = divide1 / divide2

print('O resultado da divisão é:', divisao)

#----------------------------------------------------------------------------------------------

# @title Exercício 4 - Variáveis (multiplicação)
#Crie um programa que recebe dois valores e em seguida exibe o produto deles

vezes_1 = 890
vezes_2 = 3.98

produto = vezes_1 * vezes_2

print('O resultado da multiplicação é:', produto)

#----------------------------------------------------------------------------------------------

# @title Exercício 5 (Variáveis) com input e print(f'')

# Crie um programa que recebe um valor do usuário e calcule o quadrado desse número. Em seguida, exibe o resultado.

# Programa que recebe um valor do usuário

print('Início do programa...')

n1 = int(input('Terrícola, forneça um número inteiro:'))    #int para valores inteiros

quadrado = n1**2     # Elevar ao quadrado

print(f'O quadrado de {n1} é {quadrado}!')
print('Fim do programa...')

#----------------------------------------------------------------------------------------------

# @title Exercício 6 - Biblioteca math
#Crie um programa que pede um número e calcula a raíz quadrada dele usando a biblioteca math.

# Exemplo de programa que usa uma biblioteca externa do python
# Usa a biblioteca math

import math    # Importando a biblioteca math (biblioteca matemática)

numero = int(input('Digite um número'))

raizquadrada = math.sqrt(numero)    #math.sqrt é biblioteca matemática.Raiz Quadrada

print(f'A raíz quadrada de {numero} é {raizquadrada}')

#----------------------------------------------------------------------------------------------

# @title Exercício 7

#*   Subproblema 1: Inserir quatro números do teclado (usuário)
#*   Subproblema 2: Cálculo de multiplicação dos produtos A e B e C e D. O resultado de A e B será X e C e D será Y
#*   Subproblema 3: Efetuar a subtração entre x e y
#*   Subproblema 4: Apresentar o resultado ao usuário


# @title O Código do Exercício
# Exercício 4 números
# Desenvolvido por Nathalia
# Data 01/02/2025

print('Início do programa...\n')

a = int(input('Digite o primeiro número inteiro: '))
b = int(input('Digite o segundo número inteiro: '))
c = int(input('Digite o terceiro número inteiro: '))
d = int(input('Digite o quarto número inteiro: '))

print('O Resultado de a informado foi:', a)
print('O Resultado de b informado foi:', b)
print('O Resultado de c informado foi:', c)
print('O Resultado de d informado foi:', d)

x = a*b
y = c*d

subtracao = x-y

print(f'O resultado de {x} - {y} é {subtracao} \n')

print('Fim do Programa...')6







