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