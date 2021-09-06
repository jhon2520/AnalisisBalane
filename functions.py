# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 21:27:09 2021

@author: Jhon Romero
"""

from mainSpyder import *

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


"""
Función para graficar según un CIIU DADO
"""
def graficarCIIU(codigo):
    
    # maximo = round(transpose_grouped_df[codigo].max(),0)
    # minimo = 0


    fig = plt.figure(figsize=(30,10))
    plt.bar(transpose_grouped_df["variable"], transpose_grouped_df[codigo])
    plt.xticks(rotation=270)
    # plt.yticks(np.arange(minimo, maximo))
    plt.ylabel("Valor en Millones código: ", fontsize=14)
    plt.title( ' Valores promedio para el CIIU: ' + codigo, fontsize=16)
    plt.show()
    

graficarCIIU("A0113")


def crearSubDataFrame(codigo, df):
    sub_df = df[["variable",codigo]].copy()
    sub_df = sub_df.rename(columns={codigo: codigo})

    return sub_df


df_A0113_mean = crearSubDataFrame("A0121",transpose_grouped_df)
df_A0113_max = crearSubDataFrame("A0121",transpose_grouped_max_df)
df_A0113_max = crearSubDataFrame("A0121",transpose_grouped_min_df)



def exportarDataFrame(dataFrame,nombreDataFrame):
    dataFrame.to_excel(nombreDataFrame + ".xlsx",sheet_name= "Results")
    
exportarDataFrame(df_A0113, "A0113")


