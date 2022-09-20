import csv
import matplotlib.pyplot as mpt
f = open('/home/particule/Documents/progra/metro/trafic2021RATP.csv','r',newline='')
reader = csv.DictReader(f)
liste = [ligne for ligne in reader]
liste.sort(key=lambda a: a.get("station"))


def recherche_aux(lst, val, d, f):
    if d==f and lst[d].get("station")==val:
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

def findStationData(lst, val):
    if len(lst)!=0:
        print(val)
        return liste[recherche_aux(lst, val, 0, len(lst)-1)]




def findStationByRank(lst, val):
    lstTemp = lst.copy()
    lstTemp.sort(key = lambda a : a.get("rang"))
    if len(lst)!=0:
        return lstTemp[val]

def compareStation(lst):
    lstDt = [findStationData(liste,elt) for elt in lst]
    lstNb = [int(elt.get('trafic')) for elt in lstDt]
    mpt.bar_label(mpt.bar([i*2 for i in range(len(lstNb))],lstNb),lst)
    mpt.show()
stations = ['GARE DE LYON','GARE DE LYON-RER','GARE DE L\'EST','CHATELET','CHATELET-LES HALLES-RER','LES HALLES','SAINT-LAZARE','LA DEFENSE','LA DEFENSE-RER','GARE DU NORD','GARE DU NORD-RER','GARE D\'AUSTERLITZ']
compareStation(stations)
