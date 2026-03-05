saldo_inicial= 1000
operaciones = int(input("cuantas operaciones deseas realizar:"))

for i in range(operaciones):
    print("1. consultar saldo")
    print("2. retirar dinero")
    print("3. depositar dinero")
    opcion=int(input("por favor escoge una opcion:"))
    if opcion == 1:
     print(f"tu saldo es de: ${saldo_inicial}")
    if opcion == 2:
     retiro=float(input("Cuanto dinero deseas retirar:"))
    
    elif retiro > saldo_inicial:
     print("fondos insuficientes")
    elif retiro < 0:
      print("el valor no puede ser negativo, ingrese el valor a retirar nuevamente")

