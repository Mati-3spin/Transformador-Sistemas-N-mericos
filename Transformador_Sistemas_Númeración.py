Prefijo_bin = (128,64,32,16,8,4,2,1)
prefijo_bin = (8,4,2,1)
Historial = {}
prefijo_hexa = {'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
prefijo_Hexa = {10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
print("\n______Transformador de Sistemas de Númeración.______")
print(f'-  Menú;  \n 1. Binario -> Decimal \n 2. Decimal -> Binario \n 3. Hexadecimal -> Decimal \n 4. Binario -> Hexadecimal \n 5. Decimal -> Hexadecimal \n 6. Historial \n 7. Borrar Historial \n 8. Salir')  
while True:
    opcion = input('\n Ingrese una de las opciones Enumeradas; ')
 
    if opcion == '1':
        print("\n_____Convertidor de Binario a Decimal._____")
        número_decimal = 0
        byte = input('Ingrese un Número Binario; ')
        while len(byte) != 8 or any(caracter not in '01' for caracter in byte):
            print("Debe tener 8 caracteres binarios (1 o 0)")
            byte = input('Ingrese un Número Binario; ')
        for bit, prefijo in zip(byte, Prefijo_bin):
            if bit == '1':
                número_decimal += prefijo
        print(f"Tú número binario {byte}, pasado a decimal es {número_decimal}.")
        Historial[byte] = número_decimal
    
    elif opcion == '2':
        print('\n_____Convertidor de Decimal a binario._____')         
        try:
            Decimal = int(input('Ingrese un Número Decimal; '))
            while Decimal < 0 or Decimal > 255:
                print("Debe ser un número entero entre 0 y 255.")
                Decimal = int(input('Ingrese un Número Decimal; '))
            Número_decimal = str(Decimal)
            resultado = ""
            for i in Prefijo_bin:
                if Decimal >= i:
                    resultado += "1"
                    Decimal = Decimal - i 
                elif Decimal < i:
                    resultado += "0"
                    Decimal = Decimal
            print(f"Tú número decimal {Número_decimal}, pasado a binario es {resultado}.")
            Historial[Número_decimal] = resultado
        except:
            print('Solo puedes ingresar números. Devuelta al Menú...')
    
    elif opcion == '3':
        print('\n_____Convertidor de Hexadecimal a Decimal._____')
        num_hexa = input('Ingrese un Número Hexadecimal; ')
        while len(num_hexa) != 2 or any(caracter not in '0123456789ABCDEFabcdef' for caracter in num_hexa):
            num_hexa = input('Ingrese un Número Hexadecimal; ')
        Decimal = 0
        for l, HEX in enumerate(num_hexa):
            if HEX.upper() in prefijo_hexa :
                Valor = prefijo_hexa[HEX.upper()]
                if l == 0:
                    Decimal += Valor * 16
                elif l == 1:
                    Decimal += Valor
            else:
                Valor = int(HEX)
                if l == 0:
                    Decimal += Valor * 16
                elif l == 1:
                    Decimal += Valor
        print(f"Tú número hexadecimal {num_hexa}, pasado a decimal es {Decimal}.")
        Historial[num_hexa] = Decimal       
                
    elif opcion == '4':
        print('\n____Convertidor de binario a hexadecimal.____')
        num_binario = input('Ingrese un número binario; ')
        while len(num_binario) != 4 or any(caracter not in '01' for caracter in num_binario):  
            print("Debe tener 4 caracteres binarios (1 o 0)")
            num_binario = input('Ingrese un Número Binario; ')
        Hexadecimal = 0
        for Valor, BIT in zip(prefijo_bin, num_binario):
            if BIT == '1':
                Hexadecimal += Valor
        if Hexadecimal >= 10:
            Hexadecimal = prefijo_Hexa[Hexadecimal]
        else:
            Hexadecimal = str(Hexadecimal)
        print(f'Tú número binario {num_binario}, pasado a hexadecimal es {Hexadecimal}')
        Historial[num_binario] = Hexadecimal
    
    elif opcion == '5':
        print('\n_____Convertidor de Decimal a Hexadecimal._____')
        try:
            decimal = int(input('Ingrese un Número Decimal; '))
            while decimal < 0 or decimal > 255:
                print('Tiene que ser positivo.')
                decimal = int(input('Ingrese un Número Decimal; '))
            resultado_hexadecimal = ''
            decimal_1 = decimal
            decimal_2 = decimal
            divisor =   decimal_1 // 16 
            if 0 <= divisor <= 9:
                resultado_hexadecimal += str(divisor)
            else:
                resultado_hexadecimal += prefijo_Hexa[divisor]
            resto = decimal_2 % 16
            if 0 <= resto <= 9:
                resultado_hexadecimal += str(resto)
            else:
                resultado_hexadecimal += prefijo_Hexa[resto]    
            print(f"Tú número decimal {decimal}, pasado a hexadecimal es {resultado_hexadecimal}.")
            Historial[decimal] = resultado_hexadecimal
        except:
            print('Solo se aceptan números. Devuelta al Menú...')
        
    elif opcion == '6':    
        print('\n____Historial de Uso.____')
        for aporte_X, valor_X in Historial.items():
            print(f'  - {aporte_X} --> {valor_X}')
    
    elif opcion == '7':
        print('\n____Borrar Historial.____')
        Historial.clear()
        print('Historial borrado.')
    
    elif opcion == '8':
        print('\n Cerrando programa...')
        break
    
    else:
        print("\n  Opción no valida, escribe '8' para cerrar el programa.")