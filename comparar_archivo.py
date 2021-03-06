# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 19:35:49 2021

@author: Jhon Romero
"""



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""
MANEJO DE DATOS, CREACIÓN Y ELIMINACIÓN DE COLUMNAS
"""

ruta_df_complete_supersolidaria = r"C:\\Users\\Jhon Romero\\archivosABC\\"

main_dataframe = pd.read_excel(ruta_df_complete_supersolidaria + "df_complete_supersolidaria.xlsx")

lista_columnas_main_df = main_dataframe.columns;

#Eliminar columnas

df_final = main_dataframe.drop(columns=["Codigo Instancia_x","Nit","Fecha Corte_x","Punto Entrada_x","Se reunió el Máximo Órgano Social para considerar los estados financieros",
                            "Razón social de la sociedad","Objeto social principal","Corte de cuentas según estatutos","Fecha de constitución (Aaaa-Mm-Dd)",
                            "Fecha de vencimiento (Aaaa-Mm-Dd)","Estado actual","La sociedad es","Dirección de notificación judicial registrada en Cámara de Comercio",
                            "Departamento de la dirección de notificación judicial","Ciudad de la dirección de notificación judicial","Dirección del domicilio",
                            "Departamento de la dirección del domicilio","Ciudad de la dirección del domicilio","Teléfono del domicilio","Celular corporativo",
                            "E-mail de la sociedad","Matricula mercantil número","Domicilio casa matriz sucursal de sociedad extranjera",
                            "País del domicilio casa matriz sucursal de sociedad extranjera","La compañía está obligada a tener Revisor fiscal?",
                            "El Revisor fiscal pertenece a una firma?","A que firma pertenece el Revisor Fiscal?",
                            "Los estados finacieros estan acompañados del dictamen del revisor fiscal?","Concepto del Revisor fiscal en su informe",
                            "Estos estados financieros presentan información reexpresada?","La información reexpresada corresponde a:",
                            "Reexpresión según normatividad que aplique","La Entidad posee inversiones en subsidiarias, asociadas y/o negocios conjuntos?",
                            "mes_corte_x","Codigo Instancia_y","Fecha Corte_y","Punto Entrada_y","Estado Verificación_x","Periodo_x",
                            "(+/-) Ajustes por gastos por impuestos a las ganancias","( + ) Ajustes por gastos de depreciación y amortización",
                            "(+/-) Ajustes por deterioro de valor (reversiones de pérdidas por deterioro de valor) reconocidas en el resultado del periodo",
                            "(+) Ajustes por provisiones","(+) Ajustes por costos financieros","(+/-) Ajustes por pérdidas (ganancias) de moneda extranjera no realizadas",
                            "(+) Ajustes por pérdidas (ganancias) del valor razonable","(-) Ajustes por ganancias no distribuidas de asociadas",
                            "(+/-) Ajustes por pérdidas (ganancias) por la disposición de activos no corrientes","(+/-) Otros ajustes para conciliar la ganancia (pérdida)",
                            "Total ajustes para conciliar la ganancia (pérdida)","(+/-) Ajustes por disminuciones (incrementos) en los inventarios",
                            "(+/-) Ajustes por la disminución (incremento) de cuentas por cobrar de origen comercial",
                            "(+/-) Ajustes por disminuciones (incrementos) en otras cuentas por cobrar derivadas de las actividades de operación",
                            "(+/-) Ajustes por el incremento (disminución) de cuentas por pagar de origen comercial",
                            "(+/-) Ajustes por incrementos (disminuciones) en otras cuentas por pagar derivadas de las actividades de operación",
                            "(+) Flujos de efectivo procedentes de la pérdida de control de subsidiarias u otros negocios",
                            "(+) Otros cobros por la venta de patrimonio o instrumentos de deuda de otras entidades",
                            "(-) Otros pagos para adquirir patrimonio o instrumentos de deuda de otras entidades",
                            "(+) Otros cobros por la venta de participaciones en negocios conjuntos","(+) Importes procedentes de la venta de propiedades, planta y equipo",
                            "(+) Importes procedentes de ventas de activos intangibles","(+) Recursos por ventas de otros activos a largo plazo",
                            "(+) Importes procedentes de subvenciones del gobierno","(-) Anticipos de efectivo y préstamos concedidos a terceros",
                            "(+) Cobros procedentes del reembolso de anticipos  y préstamos concedidos a terceros",
                            "(-) Pagos derivados de contratos de futuro, a término, de opciones y de permuta financiera",
                            "(+) Cobros procedentes de contratos de futuro, a término, de opciones y de permuta financiera","(+) Dividendos recibidos",
                            "(+) Intereses recibidos","(+) Importes procedentes de aumento de capital y/o recolocación de acciones",
                            "(-) Disminución de capital social y/o readquisición de acciones","(-) Pagos por otras participaciones en el patrimonio",
                            "(+) Importe procedente del aumento prima por emisión","(-) Disminución de prima por emisión","(-) Pagos de pasivos por arrendamientos financieros",
                            "(+) Importes procedentes de subvenciones del gobierno.1","(-) Anticipos de efectivo y préstamos concedidos a terceros.1",
                            "(+) Cobros procedentes del reembolso de anticipos  y préstamos concedidos a terceros.1","(+/-) Otras entradas (salidas) de efectivo.2",
                            "(+/-) Efectos de la variación en la tasa de cambio sobre el efectivo y equivalentes al efectivo","mes_corte_y","Estado Verificación_y",
                            "Periodo_y","Diferencia entre el importe en libros de dividendos pagaderos e importe en libros de activos distribuidos distintos al efectivo",
                            "Ganancias (pérdidas) que surgen de la baja en cuentas de activos financieros medidos al costo amortizado",
                            "Deterioro de valor de ganancias y reversión de pérdidas por deterioro de valor (pérdidas por deterioro de valor) determinado de acuerdo con la NIIF 9",
                            "Ganancias (pérdidas) que surgen de diferencias entre el costo amortizado anterior y el valor razonable de activos financieros reclasificados de la categoría de medición costo amortizado a la categoría de medición de valor razonable con cambios en resultados",
                            "Ganancia (pérdida) acumulada anteriormente reconocida en otro resultado integral que surge de la reclasificación de activos financieros de la categoría de medición de valor razonable con cambios en otro resultado integral a la de valor razonable con cambios en resultados",
                            "Ganancias (pérdidas) de cobertura por cobertura de un grupo de partidas con posiciones de riesgo compensadoras","Ganancia (pérdida) procedente de operaciones discontinuadas",
                            "Ganancia (pérdida)_x","Activos biológicos corrientes",
                            "Activos corrientes distintos al efectivo pignorados como garantía colateral para las que el receptor de transferencias tiene derecho por contrato o costumbre a vender o pignorar de nuevo dicha garantía colateral",
                            "Total activos corrientes distintos de los activos no corrientes o grupo de activos para su disposición clasificados como mantenidos para la venta o como mantenidos para distribuir a los propietarios",
                            "Activos no corrientes o grupos de activos para su disposición clasificados como mantenidos para la venta o como mantenidos para distribuir a los propietarios",
                            "Propiedad de inversión","Plusvalía","Activos intangibles distintos de la plusvalía","Activos biológicos no corrientes","Activos por impuestos diferidos",
                            "Activos por impuestos corrientes, no corriente",
                            "Activos no corrientes distintos al efectivo pignorados como garantía colateral para las que el receptor de transferencias tiene derecho por contrato o costumbre a vender o pignorar de nuevo la garantía colateral",
                            "Otras provisiones corrientes","Total de pasivos corrientes distintos de los pasivos incluidos en grupos de activos para su disposición clasificados como mantenidos para la venta",
                            "Pasivos incluidos en grupos de activos para su disposición clasificados como mantenidos para la venta","Provisiones no corrientes por beneficios a los empleados",
                            "Otras provisiones no corrientes","Total provisiones no corrientes","Pasivo por impuestos diferidos","Pasivos por impuestos corrientes, no corriente",
                            "Otros pasivos financieros no corrientes","Otros pasivos no financieros no corrientes","Acciones propias en cartera","Inversión suplementaria al capital asignado",
                            "Otras participaciones en el patrimonio","Codigo Instancia","Fecha Corte","Punto Entrada","Estado Verificación",
                            "Otro resultado integral, neto de impuestos, ganancias (pérdidas) de inversiones en instrumentos de patrimonio",
                            "Otro resultado integral, neto de impuestos, ganancias (pérdidas) por revaluación",
                            "Otro resultado integral, neto de impuestos, ganancias (pérdidas) por nuevas mediciones de planes de beneficios definidos",
                            "Otro resultado integral, neto de impuestos, cambio en el valor razonable de pasivos financieros atribuible a cambios en el riesgo de crédito del pasivo",
                            "Otro resultado integral, neto de impuestos, ganancias (pérdidas) en instrumentos de cobertura que cubren inversiones en instrumentos de patrimonio",
                            "Total otro resultado integral que no se reclasificará al resultado del periodo, neto de impuestos",
                            "Ganancias (pérdidas) por diferencias de cambio de conversión, netas de impuestos","Ajustes de reclasificación en diferencias de cambio de conversión, neto de impuestos",
                            "Otro resultado integral, neto de impuestos, diferencias de cambio por conversión",
                            "Ganancias (pérdidas) por nuevas mediciones de activos financieros disponibles para la venta, netas de impuestos",
                            "Ajustes de reclasificación, activos financieros disponibles para la venta, neto de impuestos",
                            "Otro resultado integral, neto de impuestos, activos financieros disponibles para la venta","Ganancias (pérdidas) por coberturas de flujos de efectivo, neto de impuestos",
                            "Ajustes de reclasificación en coberturas de flujos de efectivo, neto de impuestos",
                            "Importes eliminados del patrimonio e incluidos en el importe en libros de activos (pasivos) no financieros que se hayan adquirido o incurrido mediante una transacción prevista altamente probable cubierta, neto de impuestos",
                            "Otro resultado integral, neto de impuestos, coberturas del flujo de efectivo",
                            "Ganancias (pérdidas) por coberturas de inversiones netas en negocios en el extranjero, neto de impuestos",
                            "Ajustes de reclasificación por coberturas de inversiones netas en negocios en el extranjero, netos de impuestos",
                            "Otro resultado integral, neto de impuestos, coberturas de inversiones netas en negocios en el extranjero",
                            "Ganancia (pérdida) por cambios en el valor temporal del dinero de opciones, neta de impuestos",
                            "Ajustes de reclasificación por cambios en el valor temporal del dinero de opciones, neto de impuestos",
                            "Otro resultado integral, neto de impuestos, cambios en el valor del valor temporal del dinero de opciones",
                            "Ganancia (pérdida) por cambios en el valor de los elementos a término de contratos a término, neta de impuestos",
                            "Ajustes de reclasificación por cambios en el valor de los elementos a término de contratos a término, netos de impuestos",
                            "Otro resultado integral, neto de impuestos, cambios en el valor de los elementos a término de contratos a término",
                            "Ganancia (pérdida) por cambios en el valor de los diferenciales de la tasa de cambio de la moneda extranjera, neta de impuestos",
                            "Ajustes de reclasificación por cambios en el valor de los diferenciales de la tasa de cambio de la moneda extranjera, netos de impuestos",
                            "Otro resultado integral, neto de impuestos, cambios en el valor de los diferenciales de tasa de cambio de la moneda extranjera",
                            "Ganancia (pérdida) por activos financieros medidos al valor razonable con cambios en otro resultado integral, neto de impuestos",
                            "Ajustes de reclasificación sobre activos financieros medidos al valor razonable con cambios en otro resultado integral, netos de impuestos",
                            "Importes eliminados del patrimonio y ajustados contra el valor razonable de activos financieros en el momento de la reclasificación fuera de la categoría de medición de valor razonable con cambios en otro resultado integral, neto de impuestos",
                            "Otro resultado integral, neto de Impuestos, activos financieros medidos al valor razonable con cambios en otro resultado integral",
                            "Total otro resultado integral que se reclasificará al resultado del periodo, neto de impuestos","Total otro resultado integral","Resultado integral total",
                            "mes_corte","(-) Flujos de efectivo utilizados para obtener el control de subsidiarias u otros negocios","(-) Otros pagos para adquirir participaciones en negocios conjuntos",
                            "(+) Recursos por cambios en las participaciones en la propiedad en subsidiarias que no dan lugar a la pérdida de control",
                            "(-) Pagos por cambios en las participaciones en la propiedad en subsidiarias que no dan lugar a la pérdida de control",
                            "Participación en las ganancias (pérdidas) de Subsidiarias, asociadas y negocios conjuntos que se contabilicen utilizando el método de la participación",
                            "Otros ingresos (gastos) procedentes de subsidiarias, entidades controladas de forma conjunta y asociadas","Inversiones contabilizadas utilizando el método de la participación",
                            "Inversiones en subsidiarias, negocios conjuntos y asociadas",
                            "Participación de otro resultado integral de Subsidiarias, asociadas y negocios conjuntos contabilizados utilizando el método de la participación que no se reclasificará al resultado del periodo, neto de impuestos",
                            "Participación de otro resultado integral de Subsidiarias, asociadas y negocios conjuntos contabilizados utilizando el método de la participación que se reclasificará al resultado del periodo, neto de impuestos",
                            "(+/-) Ajustes por pérdidas (ganancias) del valor razonable","Gastos de ventas","Activos biológicos corrientes, al costo menos depreciación acumulada y deterioro de valor",
                            "Activos biológicos corrientes, al valor razonable","Propiedades de inversión al costo menos depreciación acumulada y deterioro",
                            "Propiedades de inversión a valor razonable con cambios en resultados","Activos biológicos no corrientes, al costo menos depreciación acumulada y deterioro del valor",
                            "Activos biológicos no corrientes, al valor razonable","Activos no corrientes distintos al efectivo pignorados como garantía colateral para las que el receptor de transferencias tiene derecho por contrato o costumbre a vender o pignorar de nuevo dicha garantía colateral",
                            "Préstamos corrientes","Parte corriente de préstamos no corrientes","Total pasivos corrientes distintos de los pasivos incluidos en grupos de activos para su disposición clasificados como mantenidos para la venta",
                            "Parte no corriente de préstamos no corrientes","Otro resultado integral, neto de impuestos, ganancias (pérdidas) actuariales por planes de beneficios definidos",
                            "Participación en las ganancias (pérdidas) de subsidiarias, asociadas y negocios conjuntos que se contabilicen utilizando el método de la participación",
                            "Inversiones en subsidiarias","Inversiones en asociadas","Inversiones en negocios conjuntos",
                            "Participación de otro resultado integral de subsidiarias, asociadas y negocios conjuntos contabilizados utilizando el método de la participación que se reclasificará al resultado del periodo, neto de impuestos",
                            "(+/-) Otras entradas (salidas) de efectivo.1","Unnamed: 0"])

#Tratar NA

df_final = df_final.fillna(0)


#Crear columna con los CIIU, primero se agrega al final, luego se elimina y se coloca al inicio

df_final["CIIU"] = df_final["Clasificación Industrial Internacional Uniforme Versión 4 A.C"].astype(str).str[0:5]
colum_CIIU = df_final.pop("CIIU")
df_final.insert(0, "CIIU", colum_CIIU)





"""
AGRUPACIÓN DE DATOS SEGÚN EL CIIU PARA CREAR LAS 4 TABLAS (MAX,MIN,PROMEDIO,DESVIACIÓN ESTANDAR) y CREACIÓN DE DF TRANSPUESTOS
"""

df_grouped_mean = df_final.groupby(df_final["CIIU"]).mean().round(3)
df_grouped_max = df_final.groupby(df_final["CIIU"]).max(1)
df_grouped_min = df_final.groupby(df_final["CIIU"]).min(1)
df_grouped_std = df_final.groupby(df_final["CIIU"]).std()


#Tener el nombre del ciiu según el valor de la columna

#Crear dataframe transpuesto

df_transpose_grouped_mean = df_grouped_mean.transpose()
df_transpose_grouped_mean = df_transpose_grouped_mean.reset_index()
df_transpose_grouped_mean = df_transpose_grouped_mean.rename(columns={"index":"cuenta"})

df_transpose_grouped_max = df_grouped_max.transpose()
df_transpose_grouped_max = df_transpose_grouped_max.reset_index()
df_transpose_grouped_max = df_transpose_grouped_max.rename(columns={"index":"cuenta"})

df_transpose_grouped_min = df_grouped_min.transpose()
df_transpose_grouped_min = df_transpose_grouped_min.reset_index()
df_transpose_grouped_min = df_transpose_grouped_min.rename(columns={"index":"cuenta"})

df_transpose_grouped_std = df_grouped_std.transpose()
df_transpose_grouped_std = df_transpose_grouped_std.reset_index()
df_transpose_grouped_std = df_transpose_grouped_std.rename(columns={"index":"cuenta"})


#TODO AQUI VOOOOOOOOOOOOOOOOOOOOOOOOOOOYYYYYYYYYYYYYY








# reduced_dataframe = main_dataframe.drop(columns=["Fecha Corte","Codigo Instancia","Nit", "Punto Entrada", "Se reunió el Máximo Órgano Social para considerar los estados financieros",
#                             "Objeto social principal","Corte de cuentas según estatutos", "Fecha de constitución (Aaaa-Mm-Dd)","Fecha de vencimiento (Aaaa-Mm-Dd)",
#                             "Estado actual", "La sociedad es", "Dirección de notificación judicial registrada en Cámara de Comercio","Departamento de la dirección de notificación judicial",
#                             "Ciudad de la dirección de notificación judicial", "Dirección del domicilio","Departamento de la dirección del domicilio","Ciudad de la dirección del domicilio",
#                             "Teléfono del domicilio","Celular corporativo","E-mail de la sociedad","Matricula mercantil número","Domicilio casa matriz sucursal de sociedad extranjera",
#                             "País del domicilio casa matriz sucursal de sociedad extranjera","La compañía está obligada a tener Revisor fiscal?","El Revisor fiscal pertenece a una firma?",
#                             "A que firma pertenece el Revisor Fiscal?","Los estados finacieros estan acompañados del dictamen del revisor fiscal?","Concepto del Revisor fiscal en su informe",
#                             "Estos estados financieros presentan información reexpresada?","La información reexpresada corresponde a:","Reexpresión según normatividad que aplique",
#                             "La Entidad posee inversiones en subsidiarias, asociadas y/o negocios conjuntos?","Codigo Instancia.1","Validación","Nit.1","Fecha Corte.1","Punto Entrada.1",
#                             "Periodo","Plusvalía","Codigo Instancia.2","Validación.1","Nit.2","Fecha Corte.2","Punto Entrada.2","Estado Verificación","Periodo.1","Codigo Instancia.3",
#                             "Validación.2","Nit.3","Fecha Corte.3","Punto Entrada.3","Estado Verificación.1","Periodo.2","Ganancia (pérdida).1"])

#Crea una lista con las columnas seguidas a eliminar

# lista_Columnas_sobrantes = []
# list_aux = list(reduced_dataframe.columns)

# for i in range(80,181):
#     lista_Columnas_sobrantes.append(i)
    

    

#Elimina todas las columnas sobrantes y crea un dataframe final
    
# final_dataFrame = main_dataframe.drop(main_dataframe.columns[lista_columnas_sobrantes], axis="columns")



#Cambiar NAN por cero





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











