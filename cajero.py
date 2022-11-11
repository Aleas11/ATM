billetes = [2000, 5000, 10000]
monto = int(input("Ingrese el monto que desea retirar: "))

def monto_a_dar(monto):
    resultado = []
    for b in billetes:
        if b == monto:
            print('Un billete de '+ str(b) + ' colones')
            exit()
        cant_billetes = monto // b
        if cant_billetes < 0:
            break
        if cant_billetes > 0:
            resultado.append([cant_billetes, b])
        ordenar = sorted(resultado)
    for c in ordenar:
        cant = c[0]
        billete = c[1]
        print(str(cant) + ' de billetes de ' + str(billete) + ' colones')
        falta = monto - cant * billete
        if falta > 0:
            for i in range(3):
                if falta - billetes[i] >= 0:
                    monto_a_dar(falta)
        else:
            exit(0)


monto_a_dar(monto)

