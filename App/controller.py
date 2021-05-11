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
 """

import config as cf
import model
import csv

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
def initCatalog():
    return model.newCatalog

# Funciones para la carga de datos
def loadData(Catalog):
    loadTracks(Catalog)
    loadCaracterisiticas(Catalog)

def loadTracks(Catalog):
    tracks_file = cf.data_dir + "context_content_features-small.csv"
    input_file = csv.DictReader(open(tracks_file, encoding='utf-8'),delimiter='\t')
    for categoria in input_file:
        model.addCanciones(Catalog,categoria)

def loadCaracterisiticas(Catalog):
    caracteristics_file = cf.data_dir + "context_content_features-small.csv"
    input_file = csv.DictReader(open( caracteristics_file, encoding='utf-8'),delimiter='\t')
    for categoria in input_file:
        model.addCaracterisitica(Catalog,categoria)
def init():
    analyzer = model.newAnalyzer()
    return analyzer

# Funciones para la carga de datos
def loadData(analyzer):
    songfile="context_content_features-small.csv"
    songfile = cf.data_dir + songfile
    input_file = csv.DictReader(open(songfile, encoding="utf-8"),
                                delimiter=",")
    for song in input_file:
        model.addSong(analyzer, song)
    return analyzer

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo

def requerimiento1(Catalog, caracteristica, valor_min, valor_max):

    return model.requerimiento1(Catalog, caracteristica, valor_min, valor_max)

def requerimiento2(Catalog, min_energy, max_energy, min_danceability, max_danceability):

    return model.requerimiento2(Catalog, min_energy, max_energy, min_danceability, max_danceability)
def songSize(analyzer):
    return model.songSize(analyzer)

def indexHeight(analyzer):
    return model.indexHeight(analyzer)

def indexSize(analyzer):
    return model.indexSize(analyzer)

def instrumentalTempo(map,minIns,maxIns,minTemp,maxTemp):
    return model.instrumentalTempo(map,minIns,maxIns,minTemp,maxTemp)