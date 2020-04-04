import csv
import random

def datos():
    with open('/home/mr/Documents/corona/basesdedatos/nombres_300.csv') as f:
        lista = list(csv.reader(f))
        num_elms = random.randrange(1,4)
        gen = random.randrange(1,3)
        if gen==1:
            if num_elms==1:
                ind_elm = random.randrange(0,149)
                ind_elm2 = random.randrange(0,149)
                nombres = lista[ind_elm] + [" "] + lista[ind_elm2]
            else:
                ind_elm = random.randrange(0,149)
                nombres = lista[ind_elm]
        else:
            if num_elms==1:
                ind_elm = random.randrange(151,299)
                ind_elm2 = random.randrange(151,299)
                nombres = lista[ind_elm] + [" "] + lista[ind_elm2]
            else:
                ind_elm = random.randrange(151,299)
                nombres = lista[ind_elm]


    with open('/home/mr/Documents/corona/basesdedatos/apellidos_248.csv') as f:
        lista = list(csv.reader(f))
        num_elms = random.randrange(1,4)
        ind_elm = random.randrange(0,248)
        if num_elms == 1:
            apellidos = lista[ind_elm]
        else:
            ind_elm2 = random.randrange(0,248)
            apellidos = lista[ind_elm] + [" "] + lista[ind_elm2]

    with open('/home/mr/Documents/corona/basesdedatos/emails_50000_2.txt') as f:
        lista = f.readlines()
        ind_elm = random.randrange(0,len(lista))
        correo = lista[ind_elm][:-1]    
        del lista[ind_elm]
    with open('/home/mr/Documents/corona/basesdedatos/emails_50000_2.txt', 'w+') as f:
        f.seek(0)
        f.truncate()
        for i in range(len(lista)):
            f.write(lista[i])
    
    if len(apellidos)==1:
        print('Datos tomados: ', nombres[0], apellidos[0], correo)
    else:
        print('Datos tomados: ', nombres[0], apellidos[0], apellidos[2], correo)
    print("Datos restantes: ",len(lista))
    return nombres, apellidos, correo