plik = open('tekst.txt')
dane = plik.read().split()
licznik = 0
litery_main = []
litery_slownik = {}
suma = 0
for i in range(len(dane)):
    litery = []
    licznik_local = 0
    for j in dane[i]:
        suma += 1
        if litery_main.count(j)==0:
            litery_main.append(j)
            litery_slownik[j]=1
        else:
            litery_slownik[j] += 1
        if litery.count(j) == 1 and licznik_local==0:
            licznik +=1
            licznik_local =1
        else:
            litery.append(j)
print(licznik)
#print(suma)
for k in litery_slownik:
        print(k+':', litery_slownik[k], '\t' + str(round((litery_slownik[k]*100/suma), 2)) + '%')

