# Identificando o Tipo de Dado

# Como saber o tipo de dado da variável?

4, 765, -307, 1992353543.13, -0.09, 110.44, "Noel", "Olá", "SENAI", "-307"

# @title O Código de Teste

print('4 é o do tipo...')
print(type(4))

print('-307 é o do tipo...')
print(type(-307))

print('1992353543.13 é do tipo...')
print(type(1992353543.13))

print('-0.09 é do tipo...')
print(type(-0.09))

print('110.44 é do tipo...')
print(type(110.44))

print('Noel'  ' é do tipo...')
print(type("Noel"))

print('Olá'  ' é do tipo...')
print(type('Olá'))

print('SENAI'  ' é do tipo...')
print(type('SENAI'))

print("-307'  ' é do tipo...')
print(type("-307'))    # Apresenta erro, pois o texto deve ter apenas aspas duplas ou apenas aspas simples

# ---------------------------------------------------------------------------------------------------------------------------------------

# @title Entendendo o Tipo de Dado Gerado Pela Função input()

obiwan = input('Digite um valor inteiro: ')    # Solicitando o número

print('Obiwan é considerado como...')
print(type(obiwan))

# ---------------------------------------------------------------------------------------------------------------------------------------

# @title Entendendo o Tipo de Dado Gerado Pela Funçã input()

obiwan = input('Digite um valor inteiro: ')    # Solicitando o número

print('Obiwan é considerado como...')
print(type(obiwan))

# ---------------------------------------------------------------------------------------------------------------------------------------

# @title Corrigindo o Tipo de Dado Gerado Pela Função input()

obiwan = int(input('Digite um valor inteiro: '))
print('Obiwan é considerado como...')
print(type(obiwan))


darthvader = float(input('Digite um valor qualquer: '))
print('Obiwan é considerado como...')
print(type(darthvader))    # É considerado como tipo de dado float pois foi determinado em input como dado float
# Erro de valor pode ser apresentado caso seja escrito um texto. Exemplo: digitar "um"

# ---------------------------------------------------------------------------------------------------------------------------------------

# @title Um Exemplo com Booleano

yoda = bool(input('Digite um valor booleano: '))    # Valor booleano vai determinar true ou false. False quando não haver conteúdo e True quando houver (qualquer nome)
print('Yoda é considerado como...')
print(yoda)


