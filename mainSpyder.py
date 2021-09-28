# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 19:35:49 2021

@author: Jhon Romero
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ruta = r"C:\\Users\\Jhon Romero\\Documents\\Code++\\python\\supersociedades\\AnalisisSupersociedades\\"

main_dataframe = pd.read_excel(ruta + "Plenas Individuales Base.xlsx")

reduced_dataframe = main_dataframe.drop(columns=["Fecha Corte","Codigo Instancia","Nit", "Punto Entrada", "Se reunió el Máximo Órgano Social para considerar los estados financieros",
                            "Objeto social principal","Corte de cuentas según estatutos", "Fecha de constitución (Aaaa-Mm-Dd)","Fecha de vencimiento (Aaaa-Mm-Dd)",
                            "Estado actual", "La sociedad es", "Dirección de notificación judicial registrada en Cámara de Comercio","Departamento de la dirección de notificación judicial",
                            "Ciudad de la dirección de notificación judicial", "Dirección del domicilio","Departamento de la dirección del domicilio","Ciudad de la dirección del domicilio",
                            "Teléfono del domicilio","Celular corporativo","E-mail de la sociedad","Matricula mercantil número","Domicilio casa matriz sucursal de sociedad extranjera",
                            "País del domicilio casa matriz sucursal de sociedad extranjera","La compañía está obligada a tener Revisor fiscal?","El Revisor fiscal pertenece a una firma?",
                            "A que firma pertenece el Revisor Fiscal?","Los estados finacieros estan acompañados del dictamen del revisor fiscal?","Concepto del Revisor fiscal en su informe",
                            "Estos estados financieros presentan información reexpresada?","La información reexpresada corresponde a:","Reexpresión según normatividad que aplique",
                            "La Entidad posee inversiones en subsidiarias, asociadas y/o negocios conjuntos?","Codigo Instancia.1","Validación","Nit.1","Fecha Corte.1","Punto Entrada.1",
                            "Periodo","Plusvalía","Codigo Instancia.2","Validación.1","Nit.2","Fecha Corte.2","Punto Entrada.2","Estado Verificación","Periodo.1","Codigo Instancia.3",
                            "Validación.2","Nit.3","Fecha Corte.3","Punto Entrada.3","Estado Verificación.1","Periodo.2","Ganancia (pérdida).1"])

#Crea una lista con las columnas seguidas a eliminar

lista_Columnas_sobrantes = []
list_aux = list(reduced_dataframe.columns)

for i in range(80,181):
    lista_Columnas_sobrantes.append(i)
    

    

#Elimina todas las columnas y crea un dataframe final
    
final_dataFrame = reduced_dataframe.drop(reduced_dataframe.columns[lista_Columnas_sobrantes], axis="columns")



#Cambiar NAN por cero

final_dataFrame = final_dataFrame.fillna(0)

#Crear columna con los CIIU, primero se agrega al final, luego se elimina y se coloca al inicio

final_dataFrame["CIIU"] = final_dataFrame["Clasificación Industrial Internacional Uniforme Versión 4 A.C"].astype(str).str[0:5]
colum_CIIU = final_dataFrame.pop("CIIU")
final_dataFrame.insert(2, "CIIU", colum_CIIU)


"""
Agrupar el df por CIIU
"""

grouped_mean_df = final_dataFrame.groupby(final_dataFrame["CIIU"]).mean().round(3)
grouped_max_df = final_dataFrame.groupby(final_dataFrame["CIIU"]).max(1)
grouped_min_df = final_dataFrame.groupby(final_dataFrame["CIIU"]).min(1)
grouped_std_df = final_dataFrame.groupby(final_dataFrame["CIIU"]).std()


#Crear dataframe transpuesto

transpose_grouped_mean_df = grouped_mean_df.transpose()
transpose_grouped_mean_df = transpose_grouped_mean_df.reset_index()
transpose_grouped_mean_df = transpose_grouped_mean_df.rename(columns={"index":"variable"})


transpose_grouped_max_df = grouped_max_df.transpose()
transpose_grouped_max_df = transpose_grouped_max_df.reset_index()
transpose_grouped_max_df = transpose_grouped_max_df.rename(columns={"index":"variable"})

transpose_grouped_min_df = grouped_min_df.transpose()
transpose_grouped_min_df = transpose_grouped_min_df.reset_index()
transpose_grouped_min_df = transpose_grouped_min_df.rename(columns={"index":"variable"})

transpose_grouped_std_df = grouped_std_df.transpose()
transpose_grouped_std_df = transpose_grouped_std_df.reset_index()
transpose_grouped_std_df = transpose_grouped_std_df.rename(columns={"index":"variable"})

"""
Crear grafica para un CIIU
"""

fig = plt.figure(figsize=(30,10))
plt.bar(transpose_grouped_df["variable"], transpose_grouped_df["B0620"])
plt.xticks(rotation=270)
plt.ylabel("Valor en Millones", fontsize=14)
plt.show()


"""
Crear sub dataframe según el CIIU
"""

sub_df = transpose_grouped_df[["variable","B0620"]].copy()
sub_df = sub_df.rename(columns={"B0620": "B0620 valor promedio"})


##################################################
#################################
##########################
#################
###########
##########

"""

ARCHIVO FUNCIONES

"""


"""
Función para graficar según un CIIU DADO
"""
def graficarCIIU(codigo,df):
    

    fig = plt.figure(figsize=(30,10))
    plt.bar(df["variable"], df[codigo])
    plt.xticks(rotation=270)
    # plt.yticks(np.arange(minimo, maximo))
    plt.ylabel("Valor en Millones", fontsize=14)
    plt.title( ' Valores promedio para el CIIU' + codigo, fontsize=16)
    plt.show()
    

graficarCIIU("A0113",transpose_grouped_mean_df)


def crearSubDataFrame(codigo, df):
    sub_df = df[["variable",codigo]].copy()
    sub_df = sub_df.rename(columns={codigo: codigo})

    return sub_df


df_A0113_mean = crearSubDataFrame("A0121",transpose_grouped_mean_df)
df_A0113_max = crearSubDataFrame("A0121",transpose_grouped_max_df)
df_A0113_min = crearSubDataFrame("A0121",transpose_grouped_min_df)
df_A0113_std = crearSubDataFrame("A0121",transpose_grouped_std_df)

#df_union = pd.merge(df_A0113_mean,df_A0113_max, on="variable")
#df_union = pd.merge(df_union,df_A0113_min, on="variable")

def mergeDataFrames(dfMean,dfMax,dfMin, dfStd):
    df = pd.merge(dfMean,dfMax, on="variable")
    df = pd.merge(df,dfMin, on="variable")
    df = pd.merge(df,dfStd, on="variable")
    return df

df_union = mergeDataFrames(df_A0113_mean,df_A0113_max,df_A0113_min, df_A0113_std)

"""
UNIR mean, max, min
"""




def exportarDataFrame(dataFrame,nombreDataFrame):
    dataFrame.to_excel(nombreDataFrame + ".xlsx",sheet_name= "Results")
    
exportarDataFrame(df_union, "A0121")



####################################################
#############################
#####################
##################


"""
LEER EXCEL
"""

ruta_lectura_user = r"C:/Users/Jhon Romero/Documents/Code++/python/supersociedades/AnalisisSupersociedades/"

def leerArchivo(nombreArchivo):
    dataFrame = pd.read_excel(ruta_lectura_user + nombreArchivo + ".xlsx")
    return dataFrame;

df_user = leerArchivo("file_A0121")


"""

Función de crear dataframe según el cIIU y luego crear df unificado

"""

    
#para eliminar
#historic_df = mergeDataFrames(df_A0113_mean,df_A0113_max,df_A0113_max, "variable")
    



def createCompleteDataFrame(df_user, df_historic,codigo):

    df = pd.merge(df_historic,df_user,on="variable" )
    df.columns.values[1] = codigo + " mean"
    df.columns.values[2] = codigo + " max"
    df.columns.values[3] = codigo + " min"
    df.columns.values[4] = codigo + " std"
    df.columns.values[5] = codigo + " user"
    # df_final = df_final.rename(columns={codigo +"_x": "data user",codigo +"_y": "historic data"})
    
    return df



    
complete_df = createCompleteDataFrame(df_user,df_union,"A0121")

def crearIndicadores(df):
    
    df["diferencia"] = df.iloc[:,1] - df.iloc[:,5]
    df["diferencia porcentual"] = ( df.iloc[:,5]/ df.iloc[:,1] )*100
    df["limite superior"] = df.iloc[:,1] + df.iloc[:,4]
    df["limite inferior"] = df.iloc[:,1] - df.iloc[:,4]
    
    #crear condiciones
    # 1 = alerta 0= normal
    df["Alertas"] = np.where(df.iloc[:,5] > df["limite superior"],1, np.where(df.iloc[:,5] < df["limite inferior"], 1,0))
    
    
    return df

complete_df = crearIndicadores(complete_df)


"""
Grafico de barras agrupado
"""

x = np.arange(len(complete_df["variable"]))
errorbar = np.array(complete_df["A0121 std"])
labels = np.array(complete_df["variable"])

width = 0.40
fig = plt.figure(figsize=(30,10), dpi=600)
plt.bar(x - width/2, complete_df["A0121 mean"], width, color="#38A3A5", label="Promedio sector", yerr=errorbar, error_kw={'elinewidth':0.5, 'capsize':1.0, 'capthick':0.5})
plt.bar(x + width/2, complete_df["A0121 user"], width, color="#22577A", label="Valor usuario")
plt.xticks(x, labels,rotation=270)
plt.ylabel("Valor en Millones código ", fontsize=14)
plt.title( ' Valores promedio para el CIIU ', fontsize=16)
plt.legend()
#plt.savefig(r'C:\Users\Jhon Romero\Desktop\comparacion.png', dpi=600)
plt.show()











