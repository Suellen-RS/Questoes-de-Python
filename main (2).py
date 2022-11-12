'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
def hora_convert(hora):
    if hora == 0:
        hora = 12 - 12
    elif hora <=11:
        hora = hora
    elif hora == 12:
        hora = 12
    elif hora > 12:
        hora = hora - 12
    
    return(hora)
        

def saida_hora(A,P):
    if hora < 12 and minuto < 10:
        print(f"\n0{hora_convert(hora)}:0{minuto} {A}")
    elif hora < 12 and minuto >= 10:
        print(f"\n0{hora_convert(hora)}:{minuto} {A}")
    elif hora == 12 and minuto < 10:
        print(f"\n{hora_convert(hora)}:0{minuto} {P}")
    elif hora == 12 and minuto >= 10:
        print(f"\n{hora_convert(hora)}:{minuto} {P}")    
    elif hora > 12 and minuto < 10:
        print(f"\{hora_convert(hora)}:0{minuto} {P}")
    elif hora > 12 and minuto >= 10:
        print(f"\n{hora_convert(hora)}:{minuto} {P}")


hora = int(input("Informe a hora: "))
minuto = int(input("Informe o minuto: "))
A = "A.M."
P = "P.M."
hora_convert(hora)
saida_hora(A,P)

while True:
    hora = int(input("\nInforme a hora: "))
    if hora < 0:
        print('\nACABOU POR AQUI')
        break
    minuto = int(input("Informe o minuto: "))
    hora_convert(hora)
    saida_hora(A,P)