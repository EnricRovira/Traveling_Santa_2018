import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import random
import sys
import time
import math

df_cities = pd.read_csv('data/cities.csv')

cities = np.array(df_cities['CityId'])
numVertices = len(df_cities.CityId)

visited_city = [0,]
no_visited = df_cities['CityId']
no_visited = no_visited.drop(0)

X = np.array(df_cities['X'])
Y = np.array(df_cities['Y'])

print(df_cities.head())

def calcular_distancia(origen, destino):
    distancia = np.sqrt(pow((X[destino] - X[origen]), 2) +
                        pow((Y[destino] - Y[origen]), 2))

    return distancia

def get_destiny(origin, mindistance):
    for city in no_visited:
        distance = calcular_distancia(origin, city)
        if (distance < mindistance ):
            mindistance = distance
            nextCity = city
    return nextCity, mindistance

start = time.time()
total_distance = 0
i=0
path=[0,]
nextCity = 0
mindistance = sys.maxsize

while (len(visited_city) < numVertices):
    i+=1
    nextCity, distance = get_destiny(nextCity, mindistance)
    path.append(nextCity)
    visited_city.append(nextCity)
    no_visited = no_visited.drop(nextCity)
    total_distance += distance

    if (i%100==0 or i==1):
        print ("Ya llevo: " + str(i) + ' en ' + str(time.time() - start) + " ,distancia_tot=" + str(total_distance) + " " + str(path[-6:-1]))

elapsed_time = time.time() - start
print ("Total distance: " + str(total_distance))
print("time: " + str(elapsed_time))