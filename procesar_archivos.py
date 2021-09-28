# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 21:46:32 2021

@author: Jhon Romero
"""

# Este archivo se usa para procesar todos los archivos descargados de supersociedades

import pandas as pd



########
######
####Leer un archivo y unir las hojas
####
######
#######
    ruta = "C:\\Users\\Jhon Romero\\Documents\\Code++\\python\\supersociedades\\bases\\plenas_ind.xlsx"

def compilar_archivo(ruta_archivo):
    excel_file = pd.ExcelFile(ruta_archivo)
    nombre_hojas = excel_file.sheet_names
    
    dict_hojas = {}
    for hoja in nombre_hojas:
        dict_hojas["p_" + hoja] = pd.read_excel(excel_file,sheet_name=hoja)
        
    
    #Eliminar en las hojas los datos de "Periodo" igual a "periodo anteior" cuando aplique y crear un dataframe para cada hoja y la fecha de corte que me queden
    # solo las que son a corte de diciembre
    
    
    
    df_Caratula = dict_hojas["p_Carátula"]
    df_Caratula["mes_corte"] =  pd.DatetimeIndex(df_Caratula["Fecha Corte"]).month
    df_Caratula = df_Caratula.query('mes_corte == 12')
    
    df_EFE = dict_hojas["p_EFE"] 
    df_EFE = df_EFE.query('Periodo == "Periodo Actual"')
    df_EFE["mes_corte"] =  pd.DatetimeIndex(df_EFE["Fecha Corte"]).month
    df_EFE = df_EFE.query('mes_corte == 12')
    
    df_ERI = dict_hojas["p_ERI"] 
    df_ERI = df_ERI.query('Periodo == "Periodo Actual"')
    df_ERI["mes_corte"] =  pd.DatetimeIndex(df_ERI["Fecha Corte"]).month
    df_ERI = df_ERI.query('mes_corte == 12')
    
    df_ESF = dict_hojas["p_ESF"] 
    df_ESF = df_ESF.query('Periodo == "Periodo Actual"')
    df_ESF["mes_corte"] =  pd.DatetimeIndex(df_ESF["Fecha Corte"]).month
    df_ESF = df_ESF.query('mes_corte == 12')
    
    df_ORI = dict_hojas["p_ORI"] 
    df_ORI = df_ORI.query('Periodo == "Periodo Actual"')
    df_ORI["mes_corte"] =  pd.DatetimeIndex(df_ORI["Fecha Corte"]).month
    df_ORI = df_ORI.query('mes_corte == 12')
    
    
    # unir los dataframe en uno sólo
    df_union = pd.merge(df_Caratula,df_EFE, on="Nit")   
    df_union = pd.merge(df_union,df_ERI, on="Nit")
    df_union = pd.merge(df_union,df_ESF, on="Nit")
    df_union = pd.merge(df_union,df_ORI, on="Nit")
    
    return df_union

## Metodo para limpieza de columnas iguales y algo más...

def limpiar_tabla(df):
    df = df.reset_index(drop=True)
    df = df.loc[:,~df.columns.duplicated()]
    
    return df




df_plena_ind = compilar_archivo("C:\\Users\\Jhon Romero\\Documents\\Code++\\python\\supersociedades\\bases\\plenas_ind.xlsx")
df_plena_sep = compilar_archivo("C:\\Users\\Jhon Romero\\Documents\\Code++\\python\\supersociedades\\bases\\plenas_sep.xlsx")
df_pymes_ind = compilar_archivo("C:\\Users\\Jhon Romero\\Documents\\Code++\\python\\supersociedades\\bases\\pymes_ind.xlsx")
df_pymes_sep = compilar_archivo("C:\\Users\\Jhon Romero\\Documents\\Code++\\python\\supersociedades\\bases\\pymes_sep.xlsx")


df_plena_ind = limpiar_tabla(df_plena_ind)
df_plena_sep = limpiar_tabla(df_plena_sep)
df_pymes_ind = limpiar_tabla(df_pymes_ind)
df_pymes_sep = limpiar_tabla(df_pymes_sep)


###Agrupar en un sólo archivo

df_complete_supersolidaria = df_plena_ind.append(df_plena_sep, ignore_index=True)
df_complete_supersolidaria = df_complete_supersolidaria.append(df_pymes_ind, ignore_index=True)
df_complete_supersolidaria = df_complete_supersolidaria.append(df_pymes_sep, ignore_index=True)

#Exportar archivos

df_complete_supersolidaria.to_excel("C:\\Users\\Jhon Romero\\Desktop\\df_complete_supersolidaria.xlsx",sheet_name= "Results")


























