def hash_Cadena(unaCadena, tamanoTabla):
    suma = 0
    for pos in range(len(unaCadena)):
        suma = suma + ord(unaCadena[pos])*(pos+1)
        

    return suma%tamanoTabla
#Prueba
cadena="casa"
print("Clave Hash para: ",cadena,": ",hash_Cadena(cadena,11))
cadena1="asac"
print("Clave Hash para: ",cadena1,": ",hash_Cadena(cadena1,11))