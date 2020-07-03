from pythonds.basic.stack import Stack

def divideBy2(decNumber):
    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % 2
        remstack.push(rem)
        decNumber = decNumber // 2

    binString = ""
    while not remstack.isEmpty():
        binString = binString + str(remstack.pop())

    return binString

def CalculaResultado(op,num1,num2):
    d1 = int(num1,2)
    d2 = int(num2,2)
    result = ""
    if operador == "+":
        result = d1+d2
    if operador == "-":
        result = d1 - d2
    if operador == "*":
        result = d1 * d2
    if operador == "/":
        result = d1 / d2
    if operador == "%":
        result = d1 % d2
    return divideBy2(result)

def MudaString(valor):
    cont = 8-len(valor)
    resultado = ""
    while cont>0:
        resultado+="0"
        cont-=1
    return resultado+str(valor)

operador = input()
numero1 = input()
numero2 = input()

resultado = CalculaResultado(operador,numero1,numero2)
print(MudaString(resultado))
