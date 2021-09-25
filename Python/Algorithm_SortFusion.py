def division_liste(liste_flottants):
    
#Si la liste comporte un élément, la function return cet élément
    if len(liste_flottants) <= 1: 
        return liste_flottants

#Diviser la liste en deux moitiés
    median = len(liste_flottants)//2
    liste_d = liste_flottants[:median]
    liste_g = liste_flottants[median:]

#Appliquer la fonction aux moitiés
    gauche = division_liste(liste_d)
    droite = division_liste(liste_g)
#Reconstituer la liste avec des éléments séparés
    fusionne = fusion(gauche,droite)
    return fusionne

#Tri des éléments
def fusion(tableau1,tableau2):
    indice_tableau1 = 0
    indice_tableau2 = 0    
    taille_tableau1 = len(tableau1)
    taille_tableau2 = len(tableau2)
    tableau_fusionne = []

#First, it checks the place of each element and compare it with the lenght of the "table". While the place (indice) is bigger than the number
#of the elements, the code keeps going. It checks which number is bigger and place it at right or left. 
    while indice_tableau1<taille_tableau1 and indice_tableau2<taille_tableau2:
        if tableau1[indice_tableau1] < tableau2[indice_tableau2]:
            tableau_fusionne.append(tableau1[indice_tableau1])
            indice_tableau1 += 1
        else:
            tableau_fusionne.append(tableau2[indice_tableau2])
            indice_tableau2 += 1
#Fusion de deux 'parties' (droite et gauche) pour sortir un tableau consolidé
    while indice_tableau1<taille_tableau1:
        tableau_fusionne.append(tableau1[indice_tableau1])
        indice_tableau1+=1
    while indice_tableau2<taille_tableau2:
        tableau_fusionne.append(tableau2[indice_tableau2])
        indice_tableau2+=1
    return tableau_fusionne

def merge_sort(u_input):
    try:
        # Convert list into float
        lst_float= [float(x) for x in u_input]
        print(lst_float)
        lst_trie = division_liste(lst_float)
        return lst_trie
    except:
        print ("The values entered are not valid")
        return None