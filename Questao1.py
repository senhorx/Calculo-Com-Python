def RemoveNumeros(lista):
    result = []
    for i in lista:
        if i not in result:
            result.append(i)
    result.sort()
    return result

numeros = []
qtd = int(input())

i=0
while i < qtd:
    n = input()
    if n!="":
        try:
            n=int(n)
            numeros.append(n)
            i += 1
            print(i)
        except:
            pass

for valor in RemoveNumeros(numeros):
    print(valor)