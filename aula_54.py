"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

# Exercício 1
num = input("Insira um número inteiro: ")

try:
    num_int = int(num)
    if num_int == 0:
        print(f"O número '{num_int}' não é par nem impar.")
    elif num_int % 2 == 0:
        print(f"O número '{num_int}' é par.")
    else:
        print(f"O número '{num_int}' é impar.")
except:
    print(f"'{num}' não é um número inteiro.")

# # Exercício 2
time = input("Que horas são? (Escreva apenas a hora) ")

try:
    time_int = int(time)
    if time_int >= 0 and time_int < 12:
        print("Bom dia!")
    elif time_int >= 12 and time_int < 18:
        print("Boa tarde!")
    elif time_int >= 18 and time_int < 24:
        print("Boa noite!")
    else:
        print(f"O horário '{time_int}' não existe.")
except:
    print("Informe apenas números que representem a hora!")

# Exercício 3
first_name = input("Insira seu nome: ")

try:
    if any(letter.isdigit() for letter in first_name) or first_name.isspace() or not first_name:
        raise Exception
    if len(first_name) <= 4:
        print("Seu nome é curto")
    elif len(first_name) > 4 and len(first_name) <= 6:
        print("Seu nome é normal")
    else:
        print("Seu nome é grande")
except:
    print("Insira apenas letras")


