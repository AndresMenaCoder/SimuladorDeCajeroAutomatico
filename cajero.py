# Saldo inicial
saldo= 1000

# cantidad de operaciones
operaciones = int(input("cuantas operaciones deseas realizar:"))

# Menu
for i in range(operaciones):
  print("1. consultar saldo")
  print("2. retirar dinero")
  print("3. depositar dinero")
    
  opcion=int(input("por favor escoge una opcion:"))
    
  # Saldo actual en el cajero

  if opcion == 1:      
     print(f"tu saldo es de: ${saldo}")
     print("Gracias por usar el cajero automatico")
      
  #retiro de dinero

  elif opcion == 2:
      monto=float(input("Cuanto dinero deseas retirar:"))
      while monto <= 0:
        monto= float(input("valor invalido, ingrese nuevamente su monto a retirar: "))
      if monto > saldo:
        print("fondos insuficientes") 
      else:
        saldo -= monto
        print(f"tu retiro ha sido exitoso. este es tu nuevo saldo {saldo:.2f}")
        print("Gracias por usar el cajero automatico")
        
  # Depositar dinero

  elif opcion == 3:
      monto = float(input("por favor ingresa el monto que deseas depositar:"))
      while monto < 0:
        monto = float(input("valor invalido, por favor ingresa nuevamente el monto que deseas depositar: "))
      
      saldo += monto
      print(f"Tu deposito ha sido exitoso,este es tu nuevo saldo {saldo:.2f}")
      print("Gracias por usar el cajero automatico")
  else:     
      print("opcion invalida")




      
        









    
   

