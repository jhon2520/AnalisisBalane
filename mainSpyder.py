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

for i in range(115,181):
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



