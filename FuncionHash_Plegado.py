from FuncionHash_Modulo import*
def Hash_plegado (x,tamañoTabla):
    sumDigit, extNum = 0, 0
    while x != 0:
        extNum = x % 10
        x //= 10
        sumDigit += extNum
    return Hash_modulo(sumDigit,tamañoTabla)

print(Hash_plegado(4587963335,11))