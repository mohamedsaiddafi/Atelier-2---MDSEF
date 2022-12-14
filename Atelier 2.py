
#Créer une liste en choisissant des éléments d'index impair dans la première liste et des éléments d'index pair dans la seconde. Étant donné deux listes, l1 et l2, écrivez un programme pour créer une troisième liste l3 en choisissant un élément d'indice impair dans la liste l1 et des éléments d'indice pair dans la liste l2.

l1 = [1,2,3,4,5,6,8]
l2 = [11,12,13,14,15,16,17]
l3 = []
for i in range (len(l1)):
    if i% 2 != 0:
        l3.append (l1[i])
for i in range (len(l2)):
    if i% 2 != 0:
        l3.append (l2[i])      
print (l3)





#Deviser la liste en 3 morceaux égaux et inverser chaque morceau.

l= [24,35,6,65,5,61,51,60,56]
longueur = len (l)
morceau1 = l [:longueur // 3]
morceau2 = l [longueur // 3:(2*longueur)//3]
morceau3 = l [(2*longueur) // 3:]
morceau1 = morceau1 [:: -1]
morceau2 = morceau2 [:: -1]
morceau3 = morceau3 [:: -1]
print (morceau1)
print (morceau2)
print (morceau3)





#Écrire un programme pour itérer une liste donnée et compter l'occurrence de chaque élément et créer un dictionnaire pour montrer le nombre de chaque élément. 

l =[2,4,5,3,4,7,3,4,5,0]
occurences = {}
for element in l:
   if element not in occurences: occurences [element] = 1
   else : occurences [element] += 1
print (occurences)





#Trouver l'intersection (commune) de deux Sets et supprimez ces éléments du premier Set.

set1 = {2,5,4,2,5,3}
set2 = {3,6,5,4,1,2}
intersection = set1.intersection(set2)
print (intersection)





#Itérer une liste donnée et vérifier si un élément donné existe en tant que valeur de clé dans un dictionnaire. Sinon, supprimez-le de la liste.

l= [1,16,17,19,20]
d= {'mohamed':16, 'said': 19 }
removelist = []
for i in l : 
    if i not in d. values():l.remove (i) 
print (l) 



