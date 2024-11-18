"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
cont = 0

if nome and idade:
    for letra in nome:
        if ' ' == letra:
            cont += 1

    print(f"Seu nome é {nome}")
    print(f"Seu nome invertido é {nome[::-1]}")
    print(f"Seu nome contém (ou não) espaços: {' ' in nome}")
    print(f"Seu nome tem {len(nome) - cont} letras")
    print(f"A primeira letra do seu nome é {nome[0]}")
    print(f"A última letra do seu nome é {nome[-1]}")
else:
    print("Desculpe, você deixou campos vazios.")
