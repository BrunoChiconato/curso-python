"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""
raw_cpf = '746.824.890-70'

first_counter = 10
second_counter = 11
first_cpf_sum = 0
second_cpf_sum = 0

chars = ('.','-')

clean_cpf = raw_cpf

for char in chars:
    clean_cpf = clean_cpf.replace(char, '')

for digit in clean_cpf:
    if first_counter >= 2:
        first_cpf_sum += (int(digit) * first_counter)
        first_counter -= 1

first_valid_digit = (first_cpf_sum * 10) % 11

if first_valid_digit > 9:
    first_valid_digit = 0

if first_valid_digit == int(clean_cpf[9]):
    print('O primeiro dígito do CPF informado é válido!')
    for digit in clean_cpf:
        if second_counter >= 2:
            second_cpf_sum += (int(digit) * second_counter)
            second_counter -= 1
    
    second_valid_digit = (second_cpf_sum * 10) % 11

    if second_valid_digit > 9:
        second_valid_digit = 0

    if second_valid_digit == int(clean_cpf[10]):
        print('O segundo dígito do CPF informado é válido!')
    else:
        print('O segundo dígito do CPF informado não é válido!')
else:
    print('O primeiro dígito do CPF informado não é válido!')