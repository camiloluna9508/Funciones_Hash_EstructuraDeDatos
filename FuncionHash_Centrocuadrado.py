from FuncionHash_Modulo import*
def Hash_centrocuadrado(valor,tamañoTabla):
    x=str(valor**2)
    x=list(x)
    t=len(x)
    if t%2==0:
        dato=int(x[((t//2)-1)]+x[(t//2)])
    else:
        dato=int(x[t//2])
    return Hash_modulo(dato,tamañoTabla)
print(Hash_centrocuadrado(74,11))