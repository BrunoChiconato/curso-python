"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com
erros de índices inexistentes na lista.
"""
import os

shopping_list = []

while True:
    print('Selecione uma opção:')
    user_ans = input('[i]nserir, [a]pagar, [l]istar: ').lower().strip()

    try:
        if user_ans == 'a' and shopping_list:
            delete_index = int(input('Escolha o índice para apagar: '))
            shopping_list.pop(delete_index)
        elif user_ans == 'l' and shopping_list:
            for index, product in enumerate(shopping_list):
                print(index, product)
        elif user_ans == 'i':
            os.system('clear')
            insert_product = input('Qual produto desejar adicionar? ')
            if insert_product.isalpha():
                shopping_list.append(insert_product)
            else:
                print('Insira apenas produtos!')
        else:
            print('Sua lista está vazia!')

    except IndexError:
        print('Não foi possível apagar este índice.')
    except ValueError:
        print('Insira apenas números!')