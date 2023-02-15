print('Primeiro Comando')
print('Segundo Comando')
print('Terceiro Comando')

### Seleção

condicao = False

if condicao:
    print('passou por aqui 1')
condicao = True
if condicao:
    print('passou por aqui 2')

###Iteração

lista = list(range(1,10))
for numero in lista:
    print(numero)

###Função

def caixinha_magica(numero1, numero2):
    numero_magico = numero1 + numero2
    return numero_magico

print(caixinha_magica(2,5))

###

