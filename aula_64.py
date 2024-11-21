# Faça com que uma string qualquer fique envolvido por asteriscos, exemplo: *L*u*i*z* *O*t*a*v*i*o
name = 'Luiz Otávio'
counter = 0
new_name = ''

while counter < len(name):
    new_name += f'*{name[counter]}'
    counter += 1

print(new_name)