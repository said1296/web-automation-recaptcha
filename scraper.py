from tabula import read_pdf, convert_into
from tabulate import tabulate
import csv
import random

correos = []

num_datos = 50000

with open('./basesdedatos/ashley.txt') as oldfile, open('./basesdedatos/ashley_legit.txt', 'w') as newfile:
    for line in oldfile:
        if ('yahoo' in line or 'hotmail' in line or 'gmail' in line) and 'com.' not in line:
            newfile.write(line)

f = open('./basesdedatos/ashley_legit.txt', 'rt')

for i in f:
    if len(i)>10 and len(i)<30:
        correos.append(i)

f.close()

correos = random.sample(correos, num_datos)

f = open('./basesdedatos/emails_50000_2.txt', "w+")
for i in range(len(correos)):
    f.write(correos[i])
f.close()

print(len(correos))