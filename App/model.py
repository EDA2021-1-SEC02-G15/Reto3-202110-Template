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
def newCatalog():

    Catalog = {'id_canciones': None,
                'autores': None,
                'map_id': None,
                'caracteristicas': None
                }

    Catalog['id_canciones'] = lt.newList('SINGLE_LINKED', compareElements)
    Catalog['autores'] = lt.newList('SINGLE_LINKED', compareElements)
    Catalog['map_id'] = mp.newMap(numelements= 10000, prime= 109345121, maptype= 'CHAINING', loadfactor= 0.5, comparefunction= compareIds)
    Catalog['caracterisiticas'] = mp.newMap(numelements= 10000, prime= 109345121, maptype= 'CHAINING', loadfactor= 0.5, comparefunction= compareElements)
    
    return Catalog

# Funciones para agregar informacion al catalogo

def addCanciones(Catalog, cancion, autor):

    if cancion['track_id'] not in Catalog['id_canciones']:

        if cancion['autor'] not in Catalog['autores']:

            lt.addLast(Catalog['id_canciones'], cancion)
            lt.addLast(Catalog['autores'], autor)

            mp.put(Catalog['map_id'], cancion['track_id'], (Catalog['caracteristicas'], cancion['autor']))


def addCaracterisitica(Catalog, caracteristica):

    value = newCaracteristica(caracteristica[' name'], caracteristica['valor'])
    mp.put(Catalog['caracteristicas'], value['name'],value['valor'] )

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
def requerimiento1 (Catalog, caracteristica, valor_min, valor_max):

    table = Catalog['map_id']
    n = mp.size(Catalog['map_id'])
    count_aut = 0
    count_canc = 0
    i=0
    while i < n:

        carac = me.getValue(table,i)[0]
        author = me.getValue(table,i)[1]
        authors = lt.newList()
        value = me.getValue(carac, caracteristica)

        if valor_min <= value <= valor_max:
            count_canc +=1

            if author not in authors:
                count_aut +=1
                lt.addLast(authors, author) 
    
    return count_aut, count_canc

def requerimiento2 (Catalog, min_energy, max_energy, min_danceability, max_danceability):

    table = Catalog['map_id']
    n= mp.size(table)
    track_id = mp.keySet(table)
    tracks = mp.newMap(numelements=n,prime= 109345121, maptype= 'CHAINING', loadfactor= 0.5, comparefunction= compareElements) 
    i=0
    track_count = 0

    while i < n:

        carac = me.getValue(table,i)[0]
        v_energy = me.getValue(carac, 'energy')
        v_dance = me.getValue(carac, 'danceability')

        if min_energy <= v_energy <= max_energy and min_danceability <= v_dance <= max_danceability:
            
            if track_id not in mp.keySet(tracks):
                val = lt.newList()
                lt.addLast(val, v_energy)
                lt.addLast(val, v_dance)
                mp.put(tracks,track_id, val)

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