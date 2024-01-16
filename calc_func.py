def calculadoraMat(fun, num1, num2):
    if (fun == 1):
        res = num1+num2
        return res
    elif(fun == 2):
        res = num1-num2
        return res
    elif(fun == 3):
        res = num1*num2
        return res
    elif(fun == 4):
        res = num1/num2
        return res
    else:
        res = 0
        return res

print ("Funções: 1 - Soma -- 2 - Subtração -- 3 - Multiplicação -- 4 - Divisão")
fun = int(input("Digite o número da função desejada: "))
num1 = float(input("Digite o Primeiro Valor: "))
num2 = float(input("Digite o Segundo Valor: "))
resultado = calculadoraMat(fun,num1,num2)
print (resultado)