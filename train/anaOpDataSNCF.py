import matplotlib.pyplot as mpt
import csv
f = open('/home/particule/Documents/progra/train/frequentation-gares.csv','r',newline='')
reader = csv.DictReader(f)
liste = [ligne for ligne in reader]

liste.sort(key=lambda a: a.get("Nom de la gare"))



def recherche_aux(lst, val, d, f):
    if d==f and lst[d].get("Nom de la gare")==val:
        return d
    elif d==f : 
        return None
    
    indDebMid = recherche_aux(lst, val, d, (d+f)//2)
    indMidFin = recherche_aux(lst, val, (d+f)//2+1, f)
    if indDebMid != None :
        return indDebMid
    elif  indMidFin != None:
        return indMidFin
    else:
        return None

def findGareData(lst, val):
    if len(lst)!=0:
        return lst[recherche_aux(lst, val, 0, len(lst)-1)]

def isoFre(data):
    """isole les nombres de voyageurs d'une gare

    Args:
        data (dict)

    Returns:
        dict
    """
    dico = {}
    nb = 2015
    for i in range(6):
        dico['Total Voyageurs ' + str(nb+i)] = data.get('Total Voyageurs ' + str(nb+i))
    return dico


def affichEvo(data,color='red', marker='+'):
    """plot les données d'une gare

    Args:
        data (dict) : dict de int
        color (str, optional): couleur de la marque
        marker (str, optional): style de la marque
    """
    nb=2015
    for i in range(6):
        mpt.plot(nb+i,int(data.get('Total Voyageurs ' + str(nb+i))), color=color, marker=marker)

    
def compareEvo(noms):
    """max 7 names

    Args:
        noms (lst): liste de chaine de caractères (nom de gare)
    """
    assert len(noms)<=7
    colorList = ['b','g','r','c','m','y','k']
    for elt in noms:
        affichEvo(isoFre(findGareData(liste,elt)),color=colorList.pop(0))
    mpt.show()
lstN = ['Toul']
compareEvo(lstN)

