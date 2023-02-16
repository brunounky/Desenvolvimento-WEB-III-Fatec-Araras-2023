print('Primeiro Comando')
print('Segundo Comando')
print('Terceiro Comando')

print('__________________________________')

### Seleção

condicao = False

if condicao:
    print('passou por aqui 1')
condicao = True
if condicao:
    print('passou por aqui 2')

print('__________________________________')

###Iteração

lista = list(range(1,10))
for numero in lista:
    print(numero)

print('__________________________________')

###Função

def caixinha_magica(numero1, numero2):
    numero_magico = numero1 + numero2
    return numero_magico

print(caixinha_magica(2,5))


print('__________________________________')

###Teste

assert caixinha_magica(2,2) == 4
### Permite que seja dado os parâmetros que serão utilizados e a resposta que ele deveria ter. Assim é introduzido o teste unitário.
### Teste unitário é mensurar um desenvolvimento

print('__________________________________')

print('Primeiro experimento com TDD')

def caixinha_magica2(parametro1, paramentro2):
    retorno_magico = parametro1 -paramentro2
    return retorno_magico

assert caixinha_magica2(10, 4) == 6
assert caixinha_magica2(10, 5) == 5
### Depois disso pode ser feito a refatoração do código, ou seja, melhorar a forma como o mesmo está estruturado

print('__________________________________')

### String

nome= 'Fatec Araras'
nome= 'Fatec Araras 2'
print(nome)
print(id(nome))
print(nome.upper())

print('__________________________________')

### Tipos de Sequência

lista = []
type(lista)

lista.append('bacon') ###Inserir itens na lista

###NAO TERMINEI NA AULA

print('__________________________________')

def caixinha_magica3(para1, para2):
    return 0;

