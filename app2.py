import random

def main():
    #Wagi przedmiotów:
    wagi = [12, 8, 15, 2, 9, 17, 36, 8, 14, 9]
    #Wartości przedmiotów:
    wartosci = [25, 32, 5, 8, 16, 12, 19, 2, 14, 3]
    #Maksymalna waga plecaka:
    maks_waga = 89
    #Współczynniki krzyżowania i mutacji:
    pk, pm = 0.8, 0.2

    najwieksza_wartosc = 0
    najlepsza_waga = 0
    przedmioty = ""
    bez_zmian_wyniku = 0
    iteracje = 0

    #Pula początkowa chromosomów:
    ch = []
    for i in range(6):
        ch.append(random.randint(0, 1023))
    ch_bin = []
    for x in ch:
        #Zapisanie chromosomów w postaci binarnej za pomocą 10 bitów:
        ch_bin.append(bin(x)[2:].zfill(10))
    print(f"Początkowe chromosomy: \n{ch_bin}")

    #Sprawdzanie wagi plecaka:
    for i in range(6):
        suma_wag = 0
        while True:
            j = 0
            for x in ch_bin[i]:
                if x == "1":
                    suma_wag = suma_wag + wagi[j]
                j = j + 1
            if suma_wag > maks_waga:
                #Wyrzucenie losowego elementu z plecaka:
                while True:
                    pozycja = random.randint(0, 9)
                    if ch_bin[i][pozycja] == "1":
                        ch_bin[i] = ch_bin[i][:pozycja] + "0" + ch_bin[i][pozycja+1:]
                        break
                suma_wag = 0
            else:
                break

    while True:
        #Selekcja chromosomów metodą koła ruletki:
        wartosci_funkcji = []
        for i in range(6):
            wartosc_plecaka = 0
            j = 0
            for x in ch_bin[i]:
                if x == "1":
                    wartosc_plecaka = wartosc_plecaka + wartosci[j]
                j = j + 1
            wartosci_funkcji.append(wartosc_plecaka)
        #Losowanie chromosomów na podstawie funkcji przystosowania (wartości):
        nowe_ch_bin = random.choices(ch_bin, weights=wartosci_funkcji, k=6)
        ch_bin = nowe_ch_bin

        #Krzyżowanie chromosomów:
        for i in range(3):
            ch1 = ch_bin[2*i]
            ch2 = ch_bin[2*i+1]
            if pk >= random.random():
                lokus = random.randint(1, 9)
                # Połączenie części jednego chromosomu z częścią drugiego chromosomu:
                ch_bin[2*i] = (ch1[:lokus] + ch2[lokus:])
                ch_bin[2*i+1] = (ch2[:lokus] + ch1[lokus:])

        #Mutowanie chromosomów:
        for i in range(6):
            if pm >= random.random():
                lokus = random.randint(0, 9)
                lewa = ch_bin[i][:lokus]
                prawa = ch_bin[i][lokus+1:]
                #Zamiana 1 na 0 lub 0 na 1:
                srodek = "0"
                if ch_bin[i][lokus:lokus+1] == "0":
                    srodek = "1"
                #Połączenie części chromosomu wraz ze zmienionym bitem:
                ch_bin[i] = lewa + srodek + prawa

        #Sprawdzanie wagi plecaka:
        for i in range(6):
            suma_wag = 0
            while True:
                j = 0
                for x in ch_bin[i]:
                    if x == "1":
                        suma_wag = suma_wag + wagi[j]
                    j = j + 1
                if suma_wag > maks_waga:
                    #Wyrzucenie losowego elementu z plecaka:
                    while True:
                        pozycja = random.randint(0, 9)
                        if ch_bin[i][pozycja] == "1":
                            ch_bin[i] = ch_bin[i][:pozycja] + "0" + ch_bin[i][pozycja+1:]
                            break
                    suma_wag = 0
                else:
                    break

        #Suma wartości i wag dla aktualnych chromosomów:
        wartości_plecaka = []
        wagi_plecaka = []
        for i in range(6):
            suma_wartosci = 0
            suma_wag = 0
            j = 0
            for x in ch_bin[i]:
                if x == "1":
                    suma_wartosci = suma_wartosci + wartosci[j]
                    suma_wag = suma_wag + wagi[j]
                j = j + 1
            wartości_plecaka.append(suma_wartosci)
            wagi_plecaka.append(suma_wag)

        #Ustalenie najlepszych wyników. Zapisanie wagi, przedmiotów i wartości, jeśli wartość plecaka jest większa od [najwieksza_wartosc].
        for i in range(6):
            if wartości_plecaka[i] > najwieksza_wartosc:
                najwieksza_wartosc = wartości_plecaka[i]
                najlepsza_waga = wagi_plecaka[i]
                przedmioty = ch_bin[i]
                bez_zmian_wyniku = 0

        bez_zmian_wyniku = bez_zmian_wyniku + 1
        iteracje = iteracje + 1

        if bez_zmian_wyniku >= 1000:
            break

    print("Wykonano iteracji:", iteracje)
    print("Waga plecaka wynosi", najlepsza_waga)
    print("Wartość plecaka wynosi", najwieksza_wartosc)
    print("Spakowano przedmioty o numerach:")
    i = 1
    for x in przedmioty:
        if x == "1":
            print(i, end=" ")
        i = i + 1


if __name__ == '__main__':
    main()