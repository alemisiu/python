import os #Potrzebne do ustalenia ścieżki pliku

def main():

    points = []

    #Wczytanie pliku z punktami
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(dir_path+'/data.txt', 'r') as file:
        lines = file.read().splitlines()
        #Zapisanie linijek jako lista i dodanie do listy punktów
        for x in lines:
            points.append([float(point) for point in x.split()])      
    file.close()
    
    #Wyświetlenie listy punktów
    for i in range(len(points)):
        print(i, "-", points[i])
    #Wybieranie punktu startowego
    start = int(input("Wybierz punkt startowy: "))
    start_point = points[start]
    
    print("\nWyznaczono trasę:")
    
    #Zapisanie ostatniego odwiedzonego punktu i wyrzucenie go z listy punktów, które można odwiedzić
    last_point = points.pop(start)
    print(last_point)
    
    path_lenght = 0
    for i in range(len(points)):   
        lenghts = []
        #Obliczanie odległości od ostatniego odwiedzonego punktu do wszystkich pozostałych punktów
        for x in points:
            lenghts.append(((last_point[0] - x[0])**2 + (last_point[1] - x[1])**2)**0.5)
        #Wybranie najkrótszej drogi
        min_lenght = min(lenghts)
        #Zapisanie ostatniego odwiedzonego punktu i wyrzucenie go z listy punktów, które można odwiedzić
        last_point = points.pop(lenghts.index(min_lenght))
        print(last_point)
        #Dodanie długości do łącznej długości trasy
        path_lenght += min_lenght

    #Powrót do punktu początkowego
    print(start_point)
    path_lenght += ((last_point[0] - start_point[0])**2 + (last_point[1] - start_point[1])**2)**0.5
    print("Długość trasy wynosi:", path_lenght)

if __name__ == "__main__":
    main()