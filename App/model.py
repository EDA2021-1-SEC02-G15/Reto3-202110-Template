"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newAnalyzer():

    analyzer = {'canciones': None,
                'values': None
                }

    analyzer['canciones'] = lt.newList('SINGLE_LINKED', compareIds)
    analyzer['values'] = om.newMap(omaptype='RBT',
                                      )
    return analyzer
# Funciones para agregar informacion al catalogo

def addSong(analyzer,song):
    lt.addLast(analyzer["canciones"], song)
    updateValues(analyzer["values"],song)
    return analyzer

def updateValues(map,song):
    valor=float(song["instrumentalness"])
    entry=om.get(map,valor)
    if entry is None:
        data=newDataEntry(song)
        om.put(map,valor,data)
    else:
        data=me.getValue(entry)
    addValue(data,song)

def newDataEntry(song):
    entry=lt.newList("ARRAY_LIST")
    return entry

def addValue(data,song):
    lt.addLast(data,song)
    


    

    



# Funciones para creacion de datos

# Funciones de consulta

def songSize(analyzer):
    return lt.size(analyzer["canciones"])

def indexHeight(analyzer):
    return om.height(analyzer["values"])

def indexSize(analyzer):
    return om.size(analyzer["values"])



# Funciones utilizadas para comparar elementos dentro de una lista

def instrumentalTempo(map,minIns,maxIns,minTemp:float,maxTemp:float):
    lista=om.values(map,minIns,maxIns)
    semi=lt.size(lista)
    final_list=lt.newList("ARRAY_LIST")
    for i in range(semi+1):
        songlist=lt.getElement(lista,i)
        for j in range(lt.size(songlist)+1):
            song=lt.getElement(songlist,j)
            if float(song["tempo"])>=minTemp and float(song["tempo"])<=maxTemp:
                lt.addLast(final_list,song)
    final=lt.size(final_list)
    return (final_list,final)


# Funciones de ordenamiento

def compareIds(id1, id2):
    """
    Compara dos crimenes
    """
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1


def compareElements(ele1, ele2):
    """
    Compara dos fechas
    """
    if (ele1 == ele2):
        return 0
    elif (ele1 > ele2):
        return 1
    else:
        return -1