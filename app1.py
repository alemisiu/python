import random

def main():
    #Współczynniki funkcji:
    a, b, c, d = -1, 32, 0, 5
    #Współczynniki krzyżowania i mutacji:
    pk, pm = 0.8, 0.2

    bez_zmian_wyniku = 0
    iteracje = 0

    argument = -1000000
    maksimum = -1000000

    #Pula początkowa chromosomów:
    ch = [random.randint(0, 31), random.randint(0, 31), random.randint(0, 31), random.randint(0, 31), random.randint(0, 31), random.randint(0, 31)]
    ch_bin = []
    for x in ch:
        #Zapisanie chromosomów w postaci binarnej za pomocą 5 bitów:
        ch_bin.append(bin(x)[2:].zfill(5))
    print(f"Początkowe chromosomy: \n{ch_bin}")

    while bez_zmian_wyniku < 1000:
        #Selekcja chromosomów metodą koła ruletki:
        wartosci_funkcji = []
        for x in ch_bin:
            x = int(x, 2) #Zamiana liczb binarnych na dziesiętne
            wartosci_funkcji.append(a*x*x*x + b*x*x + c*x + d)
        #Losowanie chromosomów na podstawie funkcji przystosowania
        nowe_ch_bin = random.choices(ch_bin, weights=wartosci_funkcji, k=6)
        ch_bin = nowe_ch_bin

        #Krzyżowanie chromosomów:
        for i in range(3):
            ch1 = ch_bin[2*i]
            ch2 = ch_bin[2*i+1]
            if pk >= random.random():
                lokus = random.randint(1, 4)
                #Połączenie części jednego chromosomu z częścią drugiego chromosomu:
                ch_bin[2*i] = (ch1[:lokus] + ch2[lokus:])
                ch_bin[2*i+1] = (ch2[:lokus] + ch1[lokus:])

        #Mutowanie chromosomów:
        for i in range(6):
            if pm >= random.random():
                lokus = random.randint(0, 4)
                lewa = ch_bin[i][:lokus]
                prawa = ch_bin[i][lokus+1:]
                #Zamiana 1 na 0 lub 0 na 1:
                srodek = "0"
                if ch_bin[i][lokus:lokus+1] == "0":
                    srodek = "1"
                #Połączenie części chromosomu wraz ze zmienionym bitem:
                ch_bin[i] = lewa + srodek + prawa

        argumenty = []
        wyniki = []
        for x in ch_bin:
            x = int(x, 2) #Zamiana liczb binarnych na dziesiętne
            argumenty.append(x)
            wyniki.append(a*x*x*x + b*x*x + c*x + d)

        if max(wyniki) > maksimum:
            maksimum = max(wyniki)
            indeks = wyniki.index(maksimum)
            argument = argumenty[indeks]
            bez_zmian_wyniku = 0

        bez_zmian_wyniku = bez_zmian_wyniku + 1
        iteracje = iteracje + 1

    print("Maksimum funkcji wynosi", maksimum, "dla argumentu x =", argument)
    print("Wykonano iteracji:", iteracje)


if __name__ == '__main__':
    main()