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
X = np.array(df_cities['X'])
Y = np.array(df_cities['Y'])

print(df_cities.head())

def calcular_distancia(origen, destino):
    distancia = np.sqrt(pow((df_cities.X[destino] - df_cities.X[origen]), 2) +
                        pow((df_cities.Y[destino] - df_cities.Y[origen]), 2))

    return distancia

zeors_array = np.zeros( (197770, 197770) )
print(zeors_array)