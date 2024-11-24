# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.
def multiplier(*args):
    total = 1
    for num in args:
        total *= num
    return total

print(multiplier(1,2,3,4,10))

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.
def is_pair_odd(num):
    if num % 2 == 0:
        return 'Par'
    else:
        return 'Ímpar'
    
print(is_pair_odd(3))