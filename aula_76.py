"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
secret_word = 'perfume'
guessed_word = len(secret_word) * '*'
attempts = 0

while True:
    attempt = input('Digite uma letra: ')
    attempts += 1

    new_guessed_word = ''

    for i in range(len(secret_word)):
        if attempt == secret_word[i]:
            new_guessed_word += attempt
        else:
            new_guessed_word += guessed_word[i]

    guessed_word = new_guessed_word

    if guessed_word == secret_word:
        break

    print(f'Palavra formatada: "{guessed_word}"')

print(f'Você ganhou! Parabéns. A palavra era "{secret_word}".\nVocê tentou {attempts} vezes até acertar.')

    


