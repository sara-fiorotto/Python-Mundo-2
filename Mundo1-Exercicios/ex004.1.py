a = input('Digite algo: ')
print('O tipo primitivo desse valor é', type(a))
print('Só tem espaços? {}'.format(a.isspace()))
print('É um número?', a.isnumeric())
print('É alfabético?', a.isalpha())
print('É alfanumérico ?', a.isalnum())
print('Esta em maiusculas', a.isupper())
print('Esta em minusculas ', a.islower())
print('Está capitalizada?', a.istitle())
print('Cpitalize' , a.capitalize())