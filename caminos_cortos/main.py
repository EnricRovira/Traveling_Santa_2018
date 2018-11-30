import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#import seaborn as sns
import random
from sympy import isprime, primerange
import time
import math
import sys


df_cities = pd.read_csv('data/cities.csv')
print (df_cities.head())

df_cities['prime'] = df_cities.CityId.apply(isprime)
print (df_cities.head())


# Funcion que calucla la distancia euclidea a partir de un origen y un destino

def calcular_distancia (origen, destino):
    distancia = 0
    distancia = math.sqrt( (df_cities['X'][df_cities.CityId[destino]] - df_cities['X'][df_cities.CityId[origen]])**2 +
                           (df_cities['Y'][df_cities.CityId[destino]] - df_cities['Y'][df_cities.CityId[origen]])**2)
    return distancia

#############################################
############### Cosas sueltas ###############
#############################################


# Function that calculates the minimum distance to the next city
# and append that city to 'visited'. That city will be the nex to be visited

def get_destiny(origin):
    mindistance = sys.maxsize
    for city in no_visited:
        distance = calcular_distancia(origin, city)
        if (distance < mindistance ):
            mindistance = distance
            nextCity = city
    return nextCity, mindistance

################################
######### --- MAIN --- #########
################################

# GLOBAL VARIABLES

numVertices = len(df_cities.CityId)
cities = df_cities['CityId']
no_visited = df_cities['CityId']
total_distance = 0

#//

start_time = time.time()

path = [0,]
nextCity = 0
i=0

while (len(visited_city) < numVertices):
    i+=1
    visited_city.append(nextCity)
    no_visited.drop(nextCity)
    nextCity, distance = get_destiny(nextCity)
    path.append(nextCity)
    total_distance += distance
    if (i%100==0 or i==1):
        print ("Ya llevo: " + str(i))

elapsed_time = time.time() - start_time
print ("Total distance: " + str(total_distance))
print ("Elapsed time: " + str(elapsed_time))

#path.append(0)





