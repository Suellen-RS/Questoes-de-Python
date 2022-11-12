'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
def soma_imposto(taxa, custo_do_produto):
    return  custo_do_produto + (custo_do_produto * (taxa/100))
taxa = int(input("Entre com o valor da taxa: "))
custo_do_produto = int(input("Entre com o valor do produto: "))
print(soma_imposto(taxa, custo_do_produto))