# -*- coding: utf-8 -*-
import random
centenas = [ '','Ciento ', 'Doscientos ', 'Trescientos ', 'Cuatrocientos ', 'Quinientos ',
            'Seiscientos ', 'Setecientos ', 'Ochocientos ', 'Novecientos ']

decenas1 = [ 'Diez ', 'Once ', 'Doce ', 'Trece ', 'Catorce ', 'Quince ',
            'Dieciseis ', 'Diecisiete ', 'Dieciocho ', 'Diecinueve ']

decenas2 = [ '','','Veinte ', 'Treinta ', 'Cuarenta ','Cincuenta ',
            'Sesenta ','Setenta' ,'Ochenta ', 'Noventa ']

unidades = ['', 'Un ', 'Dos ', 'Tres ', 'Cuatro ', 'Cinco ',
            'Seis ', 'Siete ', 'Ocho ', 'Nueve ']


def unos(n):
    return unidades[int(n % 10)]

def dieces(n):
    if (int(n/10) == 1):
        return (decenas1[int(n % 10)])
    elif not n%10:#decena exact
        return decenas2[int(n/10)]
    elif int(n/10)==2:#de 21 a 29
        return "Veinti"+ unos(n%10).lower()
    elif n in range (0,11):#unidad
        return unos(n%10)
    else:#resto de casos 31 a 99
        letras = decenas2[int(n/10)] + ' y ' + unos(n%10)
        return letras

def cienes(n):
    if n==100:
        return 'Cien '
    if not n/100:
        return dieces(n)
    else:
        return centenas[int(n/100)]+dieces(n%100)

def int2word(n):
    megas = int (n/1000/1000)
    kilos = int((n- megas*1000000)/1000)
    unos = n- megas*1000000 -kilos*1000
    #print (megas, ' ', kilos,' ',unos)
    letras = ''

    if megas:
        if megas == 1:
            letras = 'Un Millon '
        else:
            letras = cienes(megas) + 'Millones '
    if kilos:
        if kilos == 1:
            letras = letras+ 'Mil '
        else:
            letras = letras+ cienes(kilos)+ ' Mil ' 
    if unos:
        if unos == 1:
            letras = letras + ' Un'
        else:
            letras = letras + cienes(unos)
    tmp = ''
    letras_list = letras.split()
    for i in range (0, len(letras_list)):
        tmp = tmp + letras_list[i] + ' '
    return tmp

if __name__ == '__main__':

    n = int(random.random()*100000000)
    print(format(n,',d'),int2word(n))
