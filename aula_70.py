# Qual letra que mais aparece na seguinte frase?
frase = 'O Python é uma linguagem de programação multiparadigma. Python foi criado por Guido van Rossum.'
counter = 0
freq_num = 0

while counter < len(frase):
    num_occurrences = frase.count(frase[counter])

    if freq_num < num_occurrences and frase[counter] != ' ':
        freq_num = num_occurrences
        most_freq_letter = frase[counter]
    
    counter += 1

print(f'A letra que mais apareceu na frase foi: "{most_freq_letter}" com {freq_num} ocorrências.')