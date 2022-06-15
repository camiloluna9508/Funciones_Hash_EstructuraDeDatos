def hash(unaCadena, tamanoTabla):
    suma = 0
    for pos in range(len(unaCadena)):
        suma = suma + ord(unaCadena[pos])
        

    return suma%tamanoTabla
#Prueba
cadena="casa"
print("Clave Hash para: ",cadena,": ",hash(cadena,11))
cadena1="asac"
print("Clave Hash para: ",cadena1,": ",hash(cadena1,11))