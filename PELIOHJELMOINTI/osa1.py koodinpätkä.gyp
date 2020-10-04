import random
import string

# Satunnaisuus 
print(random.randint(1,10))

# Nopan heittäminen 
print("Silmäluku: ", random.randint(1,6))

# Kolikon heittäminen 
a = ["Kruuna","klaava"]
print("Tulos: " + random.choice(a)) 

# Salasanan arpoja 
merkkienmaara = 0
salasana=""
while(merkkienmaara<8):
    salasana += random.choice(string.ascii_lowercase)
    merkkienmaara += 1
print(salasana) 

salasana=""
for x in range(8):
    salasana += random.choice(string.ascii_lowercase) 
print(salasana) 

# Sekoittaja 

def sekoitaLista(luvut):
    random.shuffle(luvut)

def tulostaLista(luvut):
     print(luvut) 

luvut = [1, 2, 3, 4, 5, 6, 7, 8]
sekoitaLista(luvut)
tulostaLista(luvut) 

# Vihollisen sijainnit 
sijaintiLista=[]
for i in range(0,1000):
    n = str(random.randint(1,100)) + "," + str(random.randint(1,100))
    sijaintiLista.append(n)

print(sijaintiLista)
