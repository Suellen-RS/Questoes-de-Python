'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
def calcula_area(base_maior,base_menor,altura):
    return ((base_maior + base_menor) * altura)/2

altura = int(input("Entre com o valor da altura: "))
base_maior = int(input("Entre com o valor da base maior: "))
base_menor = int(input("Entre com o valor da base menor: "))

area = calcula_area(base_maior,base_menor,altura)
print(area)

