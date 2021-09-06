# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 22:21:47 2021

@author: Jhon Romero
"""

from mainSpyder import *
from functions import * 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def leerArchivo(nombreArchivo):
    dataFrame = pd.read_excel(nombreArchivo + ".xlsx")
    return dataFrame;

df_user = leerArchivo("file_A0113")


"""

Función de crear dataframe según el cIIU y luego crear df unificado

"""
def mergeDataFrames(dfMean,dfMax,dfMin, key):
    df = pd.merge(dfMean, dfMax, on=key)
    df = pd.merge(df,dfMin, on=key)
    df = df.rename(columns={})
    return df
    

historic_df = mergeDataFrames(df_A0113_mean,df_A0113_max,df_A0113_max, "variable")
    



def createCompleteDataFrame(codigo,df_user):
    
    df_historic = crearSubDataFrame(codigo)
    df_final = pd.merge(df_user,df_historic, on="variable")
    df_final = df_final.rename(columns={codigo +"_x": "data user",codigo +"_y": "historic data"})
    
    return df_final
    
prueba = createCompleteDataFrame("A0113",df_user)
prueba["diferencia"] = prueba["historic data"] - prueba["data user"]
prueba["diferencia porcentual"] = ( prueba["data user"]/ prueba["historic data"] )*100


transpose_grouped_df = transpose_grouped_df.rename(columns={"index":"variable"})