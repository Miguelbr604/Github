while True:
    numero_1 = input("digite um numero ")
    numero_2 = input("digite outro numero ")
    operadores = input ("digite o operador que voce deseja, +, -, /, *: ")

    numeros_validos = None
   


    try:
        num1 = float(numero_1)
        num2 = float(numero_2)
        numeros_validos = True

    except:
        numeros_validos = None
    
    if numeros_validos is None:
        print("voce nao digitou um numero")
        continue
    operadores_permitidos = "+,-,/,*"

    if operadores not in operadores_permitidos:
        print("digitou operadores errado")
        continue
    if operadores == "+":
        print(f"{num1} + {num2}=", num1 + num2)
        continue

    elif operadores == "-":
        print(f"{num1}-{num2}=", num1 - num2)
        continue
    elif operadores == "/":
        print(f"{num1}/ {num2}=", num1 / num2)
        continue
    elif operadores == "*":
        print(f"{num1}*{num2}=", num1 * num2  )
        continue

    else:
        print("voce nao inseriu nenhum operador")

    saida = input("voce quer [s]air? ").lower().startswith()

    if saida is True:
        break


    

    

    

 