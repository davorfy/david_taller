# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 22:49:40 2021

@author: Lenovo
"""

# Desarrollo 1
def valory():
    y = ( ( 5 + 2 - 5)**2 * 5 + 8 / 2 - 30) / 2 * 5 - 3
    return y

def valor2y():
    z = 5
    n = 3
    m = z - n
    y = (((z + 2 - n)**2 * m + 8 / 2 - 30) / 2 * 5 - 3 )**5 + 15 * 3 - 9 / 3
    return y

def valor3y():
    z = 5
    n = ((8+2-4)**2 * 5 + 8 + 7 / 2 - 30* 5 ) / 2 * 5 - 3;
    m = z**2 * 3 + n;
    y = ((((z+2-n)**2 * m+8/2 - 30) / 2 * 5 - 3)**5 + 15 * 3 - 9 / 3)**2 - 5 / 4
    return y

# Desarrollo 2

def actividad1(p, v, t):
    return (p * v) / (0.37 * (t + 460))

def actividad2(edad):
    return (200 - edad) / 10

def actividad3(pers1, pers2, pers3):
    total = pers1 + pers2 + pers3
    porc1 = pers1 * 100 / total
    porc2 = pers2 * 100 / total
    porc3 = pers3 * 100 / total
    return porc1, porc2, porc3

def actividad4(saldoini):
    return saldoini + (saldo * 0.015)

def actividad5(sueldobase):
    ley = sueldobase * 0.01
    seguro_social = sueldobase * 0.04
    seguro_forzoso = sueldobase * 0.005
    cajaahor = sueldobase * 0.05
    sueldo_final = sueldobase - ley - seguro_social - seguro_forzoso - cajaahor

    return ley, seguro_social, seguro_forzoso, cajaahor, sueldo_final

def actividad6(npalabras, tam, col):
    return (npalabras * 20000) + (tam * 15000) + (col * 25000)

def actividad7(t):
    return 100000 + (120000 * (t - 1))

def actividad8(t_h):
    desc = (t_h * 20000) * 0.05
    pago = t_h * 20000 - desc
    return pago, desc

def actividad9(inic, fin):
    return (inic - fin) - ((inic - fin) * 0.2)

def actividad10(nfot):
    return (nfot * 1500) + ((nfot * 1500) * 0.16)

def actividad11(monto):
    ginecologia =  monto * 0.4
    traumatologia = monto * 0.3
    pediatria = monto * 0.3

    return ginecologia, traumatologia, pediatria


