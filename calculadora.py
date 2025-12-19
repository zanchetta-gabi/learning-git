def soma(x,y):
    return x+y

def subtracao(x,y):
    return x-y

def multiplicacao(x,y):
    return x*y

def divisao(x,y):
    return x/y

def calculadora():
    n1string = input("Insira o 1 numero: ")
    n2string = input("Insira o 2 numero: ")

    num1 = int(n1string)
    num2 = int(n2string)
    
    prompt = "Insira a operacao desejada [soma, subtacao, multiplicacao, divisao]: "
    operacao = input(prompt)

    if operacao == "soma":
        resultado = soma(x=num1,y=num2)

    if operacao == "subtracao":
        resultado = subtracao(x=num1,y=num2)

    if operacao == "multiplicacao":
        resultado = multiplicacao(x=num1,y=num2)
        
    if operacao == "divisao":
        resultado = divisao(x=num1,y=num2)
    
    print(f"tcharammm, seu resultado é: {resultado}")


calculadora()