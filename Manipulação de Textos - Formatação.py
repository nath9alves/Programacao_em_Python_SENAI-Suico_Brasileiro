# Manipulação de Textos - Formatação

> Entendendo a Concatenação

print('Olá'+'tudo'+'bem?')
print('Olá! '+'Tudo '+'bem?')     # o símbolo de + une os textos
print('Olá!', 'Tudo', 'bem?')     # NÃO é concatenação

# -----------------------------------------------------------------------------------------------------------------------------------------------------------

# @title Vários Jeitos de Escrita

etbilu = int(input('Digite o primeiro número inteiro: '))    # não podemos usar texto com string pois a concatenação não aceita
r2d2 = int(input('Digite o segundo número inteiro: '))

soma = etbilu + r2d2    # Operação de adição

print('A soma de etbilu e r2d2 é:', soma, '!')    # exibindo o resultado
print('A soma de', etbilu, 'e', r2d2, ' é:', soma, '!')    # diferente
print('A soma de {} e {} vale {}!', format(etbilu, r2d2, soma))
print(f'A soma de {etbilu} e {r2d2} vale {soma}!')

# -----------------------------------------------------------------------------------------------------------------------------------------------------------

# Textos e Seus Segredos

# @title Descobrindo Quantas Letras há na Palavra

xandao = "Supremo tribunal federal"
len(xandao)

 # :) Exercício  ☕

 > Descubra quantas letras tem em: "O rato roeu da roupa do rei" , " João tem 22 anos de idade e R$ 156,45 no bolso" e " ''(aspas vazias)

rato = "O rato roeu da roupa do rei"
len(rato)

joao = "João tem 22 anos de idade e R$ 156,45 no bolso"
len(joao)
          # o resultado vai ser sempre do último
aspas = ''
len(aspas)    # aspas vazias é resultante em 0 pois não contém texto

# -----------------------------------------------------------------------------------------------------------------------------------------------------------

# Acessando uma Letra na Frase

Acessamos um dos caracteres da frase usando os colchetes [ ] e nele o índice do caractere que queremos usar.
Assim, para acessar o elemento de índice 3 na frase usamos a seguinte forma:

nome_da_vari_ável[3]

exemplo = 'Araçoiaba da Serra'
len(exemplo)

exemplo[3]    # [] vai me trazer a letra correspondente a essa posição

exemplo[0:8]    # [0:8] vai me trazer ambas posições correspondentes e assim por diante, porém sempre será desconsiderado o último número, fazendo com que nesse caso o resultado seja até o 7

print(exemplo[0:8])
exemplo[0:9]    # Vai me trazer a palavra completa
exemplo[:9]     # Vai me trazer a palavra completa, pois o espaço em branco já é considerado como 0
exemplo[13:]    # Vai mostrar a frase da posição 13 em diante (todo o resto)
exemplo[1:2]    # O último dígito não é contado, precisa incluir um dígito a mais
exemplo [-1]    # apresenta o último dígito da frase
exemplo [-2]    #apresenta o penúltimo dígito da frase e assim por diante
exemplo[-5]
exemplo[-10:]    # apresenta desde o último dígito até a posição 10 contada de trás pra frente
