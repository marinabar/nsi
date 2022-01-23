from math import sqrt

# distance euclidienne
def distance(a, b): # a et b deux tuples de coordonnées
    d =0
    for i in range (len(a)):
        d+=(a[i]-b[i])**2
    return sqrt(d)


# renvoie la liste des distances de points à un autre point o
def listd(L,o):
    listd = []
    for i in range (len(L)):
        listd.append((distance(L[i], o), i))
    return listd


# calcule les k plus proches voisins d'un point o
def knn(L,k,o):
    d = listd(L,o) 
    d.sort(key=lambda x:x[0]) # trier liste en fonction du 1er arg dans chaque tuple de la liste
    return d[:k]
