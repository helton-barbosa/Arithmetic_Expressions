from math import sqrt

a = int(input('Entre com o valor de A: '))
b = int(input('Entre com o valor de B: '))
c = int(input('Entre com o valor de C: '))

raiz_01 = (-b + sqrt(b ** 2 - 4 * a * c)) / (2 * a)
raiz_02 = (-b - sqrt(b ** 2 - 4 * a * c)) / (2 * a)
print(f'As raízes são: {raiz_01} e {raiz_02}')
