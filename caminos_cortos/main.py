import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#import seaborn as sns
import random
from sympy import isprime, primerange
import time
import math


df_cities = pd.read_csv('data/cities.csv')
print (df_cities.head())

df_cities['prime'] = df_cities.CityId.apply(isprime)
print (df_cities.head())

numVertices = len(df_cities.CityId)


# Funcion que calucla la distancia euclidea a partir de un origen y un destino

def calcular_distancia (origen, destino):
    distancia = 0
    distancia = math.sqrt( (df_cities['X'][df_cities.CityId[destino]] - df_cities['X'][df_cities.CityId[origen]])**2 +
                           (df_cities['Y'][df_cities.CityId[destino]] - df_cities['Y'][df_cities.CityId[origen]])**2)
    return distancia

#############################################
############### Cosas sueltas ###############
#############################################

"""
    def minDistance(dist, sptSet):



    # Funtion that implements Dijkstra's single source
    # shortest path algorithm for a graph represented
    # using adjacency matrix representation
    def dijkstra(self, src):

        dist = [sys.maxint] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for cout in range(self.V):

            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # u is always equal to src in first iteration
            u = self.minDistance(dist, sptSet)

            # Put the minimum distance vertex in the
            # shotest path tree
            sptSet[u] = True

            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shotest path tree
            for v in range(self.V):
                if self.graph[u][v] > 0 and sptSet[v] == False and
                   dist[v] > dist[u] + self.graph[u][v]:
                        dist[v] = dist[u] + self.graph[u][v]
"""
