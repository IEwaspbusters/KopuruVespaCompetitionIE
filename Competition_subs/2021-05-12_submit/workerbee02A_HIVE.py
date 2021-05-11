# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 16:42:55 2021

@author: Usuario
"""

import pandas as pd
import numpy as np
import glob, os




#-----------

path = r'E:/Kopuru/Estaciones data' # use your path
files = glob.glob(path + "/*.csv")
df = pd.concat([pd.read_csv(fp, header=None, sep=';').assign(new=os.path.basename(fp).split('.')[0]) for fp in files])
df.rename(columns=df.iloc[0], inplace=True)
df.columns
df.rename(columns={'DÍAS DE HELADA 2016': 'new'}, inplace= True)
df=df.loc[~df['COD.'].isin(['KOD.','COD.' ]),:].dropna(subset=['COD.']).drop(columns=["cota (m)", "SUMA"])

# Extract year from the string  
df['year'] = df['new'].str.extract('(\d\d\d\d)', expand=True)

#Función para crear codigo_merge
def str_join(df, sep, *cols):
    from functools import reduce
    return reduce(lambda x, y: x.astype(str).str.cat(y.astype(str), sep=sep), 
                 [df[col] for col in cols])

#Variables------------------------------------------------------------------------------------------------------------------

## Freeze----------------------------
freez= df[df['new'].str.contains("HELADA")].drop(columns=['new'])
freez=pd.melt(freez, id_vars=['COD.', 'ESTACION', 'year'], value_vars=['ENE', 'FEB', 'MAR', 'ABR', 'MAY',
                                                                'JUN', 'JUL', 'AGO', 'SET', 'OCT', 'NOV','DIC'], var_name='month',value_name='freez')

freez['merge_cod'] = str_join(freez,'_' , 'COD.','ESTACION','year', 'month')
freez.drop(columns= ['COD.', 'ESTACION', 'year', 'month'], inplace= True)
cols= ['merge_cod', 'freez']
freez= freez.reindex(columns= cols)

## Rain ------------------------------
rain= df[df['new'].str.contains("DÍAS DE PRECIPITACIÓN 20")].drop(columns=['new'])
rain=pd.melt(rain, id_vars=['COD.', 'ESTACION', 'year'], value_vars=['ENE', 'FEB', 'MAR', 'ABR', 'MAY',
                                                                'JUN', 'JUL', 'AGO', 'SET', 'OCT', 'NOV','DIC'], var_name='month',value_name='rain')

rain['merge_cod'] = str_join(rain,'_' , 'COD.','ESTACION','year', 'month')

rain.drop(columns= ['COD.', 'ESTACION', 'year', 'month'], inplace= True)

## rain_1mm----------------------------

rain_1mm= df[df['new'].str.contains("DÍAS DE PRECIPITACIÓN IGUAL O SUPERIOR")].drop(columns=['new'])
rain_1mm=pd.melt(rain_1mm, id_vars=['COD.', 'ESTACION', 'year'], value_vars=['ENE', 'FEB', 'MAR', 'ABR', 'MAY',
                                                                'JUN', 'JUL', 'AGO', 'SET', 'OCT', 'NOV','DIC'], var_name='month',value_name='rain_1mm')

rain_1mm['merge_cod'] = str_join(rain_1mm,'_' , 'COD.','ESTACION','year', 'month')
rain_1mm.drop(columns= ['COD.', 'ESTACION', 'year', 'month'], inplace= True)

## rain_cum------------------------------
rain_cum= df[df['new'].str.contains("PRECIPITACIÓN ACUMULADA")].drop(columns=['new'])
rain_cum=pd.melt(rain_cum, id_vars=['COD.', 'ESTACION', 'year'], value_vars=['ENE', 'FEB', 'MAR', 'ABR', 'MAY',
                                                                'JUN', 'JUL', 'AGO', 'SET', 'OCT', 'NOV','DIC'], var_name='month',value_name='rain_cum')

rain_cum['merge_cod'] = str_join(rain_cum,'_' , 'COD.','ESTACION','year', 'month')
rain_cum.drop(columns= ['COD.', 'ESTACION', 'year', 'month'], inplace= True)


## rain_max_10------------------------------
rain_max_10= df[df['new'].str.contains("PRECIPITACIÓN MÁXIMA EN 10 MINUTOS ")].drop(columns=['new'])
rain_max_10=pd.melt(rain_max_10, id_vars=['COD.', 'ESTACION', 'year'], value_vars=['ENE', 'FEB', 'MAR', 'ABR', 'MAY',
                                                                'JUN', 'JUL', 'AGO', 'SET', 'OCT', 'NOV','DIC'], var_name='month',value_name='rain_max_10')

rain_max_10['merge_cod'] = str_join(rain_max_10,'_' , 'COD.','ESTACION','year', 'month')
rain_max_10.drop(columns= ['COD.', 'ESTACION', 'year', 'month'], inplace= True)


## rain_max_day------------------------------
rain_max_day= df[df['new'].str.contains("PRECIPITACIÓN MÁXIMA EN UN DÍA ")].drop(columns=['new'])
rain_max_day=pd.melt(rain_max_day, id_vars=['COD.', 'ESTACION', 'year'], value_vars=['ENE', 'FEB', 'MAR', 'ABR', 'MAY',
                                                                'JUN', 'JUL', 'AGO', 'SET', 'OCT', 'NOV','DIC'], var_name='month',value_name='rain_max_day')

rain_max_day['merge_cod'] = str_join(rain_max_day,'_' , 'COD.','ESTACION','year', 'month')
rain_max_day.drop(columns= ['COD.', 'ESTACION', 'year', 'month'], inplace= True)

## hum------------------------------
hum= df[df['new'].str.contains("HUMEDAD MEDIA")].drop(columns=['new'])
hum=pd.melt(hum, id_vars=['COD.', 'ESTACION', 'year'], value_vars=['ENE', 'FEB', 'MAR', 'ABR', 'MAY',
                                                                'JUN', 'JUL', 'AGO', 'SET', 'OCT', 'NOV','DIC'], var_name='month',value_name='hum')

hum['merge_cod'] = str_join(hum,'_' , 'COD.','ESTACION','year', 'month')
hum.drop(columns= ['COD.', 'ESTACION', 'year', 'month'], inplace= True)


## sun------------------------------
sun= df[df['new'].str.contains("IRRADIACIÓN MEDIA")].drop(columns=['new'])
sun=pd.melt(sun, id_vars=['COD.', 'ESTACION', 'year'], value_vars=['ENE', 'FEB', 'MAR', 'ABR', 'MAY',
                                                                'JUN', 'JUL', 'AGO', 'SET', 'OCT', 'NOV','DIC'], var_name='month',value_name='sun')

sun['merge_cod'] = str_join(sun,'_' , 'COD.','ESTACION','year', 'month')
sun.drop(columns= ['COD.', 'ESTACION', 'year', 'month'], inplace= True)




## lev_max------------------------------
lev_max= df[df['new'].str.contains("NIVEL MÁXIMO")].drop(columns=['new'])
lev_max=pd.melt(lev_max, id_vars=['COD.', 'ESTACION', 'year'], value_vars=['ENE', 'FEB', 'MAR', 'ABR', 'MAY',
                                                                'JUN', 'JUL', 'AGO', 'SET', 'OCT', 'NOV','DIC'], var_name='month',value_name='lev_max')

lev_max['merge_cod'] = str_join(lev_max,'_' , 'COD.','ESTACION','year', 'month')
lev_max.drop(columns= ['COD.', 'ESTACION', 'year', 'month'], inplace= True)



## lev_mid------------------------------
lev_mid= df[df['new'].str.contains("NIVEL MEDIO")].drop(columns=['new'])
lev_mid=pd.melt(lev_mid, id_vars=['COD.', 'ESTACION', 'year'], value_vars=['ENE', 'FEB', 'MAR', 'ABR', 'MAY',
                                                                'JUN', 'JUL', 'AGO', 'SET', 'OCT', 'NOV','DIC'], var_name='month',value_name='lev_mid')

lev_mid['merge_cod'] = str_join(lev_mid,'_' , 'COD.','ESTACION','year', 'month')
lev_mid.drop(columns= ['COD.', 'ESTACION', 'year', 'month'], inplace= True)

## lev_min------------------------------only 2019
lev_min= df[df['new'].str.contains("NIVEL MÍNIMO")].drop(columns=['new'])
lev_min=pd.melt(lev_min, id_vars=['COD.', 'ESTACION', 'year'], value_vars=['ENE', 'FEB', 'MAR', 'ABR', 'MAY',
                                                                'JUN', 'JUL', 'AGO', 'SET', 'OCT', 'NOV','DIC'], var_name='month',value_name='lev_min')

lev_min['merge_cod'] = str_join(lev_min,'_' , 'COD.','ESTACION','year', 'month')
lev_min.drop(columns= ['COD.', 'ESTACION', 'year', 'month'], inplace= True)


## temp_max_abs------------------------------
temp_max_abs= df[df['new'].str.contains("TEMPERATURA MÁXIMA ABSOLUTA")].drop(columns=['new'])
temp_max_abs=pd.melt(temp_max_abs, id_vars=['COD.', 'ESTACION', 'year'], value_vars=['ENE', 'FEB', 'MAR', 'ABR', 'MAY',
                                                                'JUN', 'JUL', 'AGO', 'SET', 'OCT', 'NOV','DIC'], var_name='month',value_name='temp_max_abs')

temp_max_abs['merge_cod'] = str_join(temp_max_abs,'_' , 'COD.','ESTACION','year', 'month')
temp_max_abs.drop(columns= ['COD.', 'ESTACION', 'year', 'month'], inplace= True)


## temp_max_avg-----------------------------
temp_max_avg= df[df['new'].str.contains("TEMPERATURA MÁXIMA MEDIA")].drop(columns=['new'])
temp_max_avg=pd.melt(temp_max_avg, id_vars=['COD.', 'ESTACION', 'year'], value_vars=['ENE', 'FEB', 'MAR', 'ABR', 'MAY',
                                                                'JUN', 'JUL', 'AGO', 'SET', 'OCT', 'NOV','DIC'], var_name='month',value_name='temp_max_avg')

temp_max_avg['merge_cod'] = str_join(temp_max_avg,'_' , 'COD.','ESTACION','year', 'month')
temp_max_avg.drop(columns= ['COD.', 'ESTACION', 'year', 'month'], inplace= True)

## temp_avg----------------------------
temp_avg= df[df['new'].str.contains("TEMPERATURA MEDIA")].drop(columns=['new'])
temp_avg=pd.melt(temp_avg, id_vars=['COD.', 'ESTACION', 'year'], value_vars=['ENE', 'FEB', 'MAR', 'ABR', 'MAY',
                                                                'JUN', 'JUL', 'AGO', 'SET', 'OCT', 'NOV','DIC'], var_name='month',value_name='temp_avg')

temp_avg['merge_cod'] = str_join(temp_avg,'_' , 'COD.','ESTACION','year', 'month')
temp_avg.drop(columns= ['COD.', 'ESTACION', 'year', 'month'], inplace= True)


## temp_min_abs----------------------------
temp_min_abs= df[df['new'].str.contains("TEMPERATURA MÍNIMA MEDIA ")].drop(columns=['new'])
temp_min_abs=pd.melt(temp_min_abs, id_vars=['COD.', 'ESTACION', 'year'], value_vars=['ENE', 'FEB', 'MAR', 'ABR', 'MAY',
                                                                'JUN', 'JUL', 'AGO', 'SET', 'OCT', 'NOV','DIC'], var_name='month',value_name='temp_min_abs')

temp_min_abs['merge_cod'] = str_join(temp_min_abs,'_' , 'COD.','ESTACION','year', 'month')
temp_min_abs.drop(columns= ['COD.', 'ESTACION', 'year', 'month'], inplace= True)


## wind_max----------------------------
wind_max= df[df['new'].str.contains("VELOCIDAD DE LA RACHA MÁXIMA ")].drop(columns=['new'])
wind_max=pd.melt(wind_max, id_vars=['COD.', 'ESTACION', 'year'], value_vars=['ENE', 'FEB', 'MAR', 'ABR', 'MAY',
                                                                'JUN', 'JUL', 'AGO', 'SET', 'OCT', 'NOV','DIC'], var_name='month',value_name='wind_max')

wind_max['merge_cod'] = str_join(wind_max,'_' , 'COD.','ESTACION','year', 'month')
wind_max.drop(columns= ['COD.', 'ESTACION', 'year', 'month'], inplace= True)


## wind_avg----------------------------
wind_avg= df[df['new'].str.contains("VELOCIDAD MEDIA ")].drop(columns=['new'])
wind_avg=pd.melt(wind_avg, id_vars=['COD.', 'ESTACION', 'year'], value_vars=['ENE', 'FEB', 'MAR', 'ABR', 'MAY',
                                                                'JUN', 'JUL', 'AGO', 'SET', 'OCT', 'NOV','DIC'], var_name='month',value_name='wind_avg')

wind_avg['merge_cod'] = str_join(wind_avg,'_' , 'COD.','ESTACION','year', 'month')
wind_avg.drop(columns= ['COD.', 'ESTACION', 'year', 'month'], inplace= True)

## wind_max_avg----------------------------
wind_max_avg= df[df['new'].str.contains("MEDIA DE LAS VELOCIDADES MÁXIMAS ")].drop(columns=['new'])
wind_max_avg=pd.melt(wind_max_avg, id_vars=['COD.', 'ESTACION', 'year'], value_vars=['ENE', 'FEB', 'MAR', 'ABR', 'MAY',
                                                                'JUN', 'JUL', 'AGO', 'SET', 'OCT', 'NOV','DIC'], var_name='month',value_name='wind_max_avg')

wind_max_avg['merge_cod'] = str_join(wind_max_avg,'_' , 'COD.','ESTACION','year', 'month')
wind_max_avg.drop(columns= ['COD.', 'ESTACION', 'year', 'month'], inplace= True)


#Merging meteorological data


m_data= freez.merge(hum, on='merge_cod', how= 'outer' ).merge(
    lev_max, on='merge_cod', how= 'outer' ).merge(
    lev_mid, on='merge_cod', how= 'outer' ).merge(
    lev_min, on='merge_cod', how= 'outer' ).merge(
    rain, on='merge_cod', how= 'outer' ).merge(
    rain_1mm, on='merge_cod', how= 'outer' ).merge(
    rain_cum, on='merge_cod', how= 'outer' ).merge(
    rain_max_10, on='merge_cod', how= 'outer' ).merge(
    rain_max_day, on='merge_cod', how= 'outer' ).merge(
    sun, on='merge_cod', how= 'outer' ).merge(
    temp_avg, on='merge_cod', how= 'outer' ).merge(
    temp_max_abs, on='merge_cod', how= 'outer' ).merge(
    temp_max_avg, on='merge_cod', how= 'outer' ).merge(
    temp_min_abs, on='merge_cod', how= 'outer' ).merge(
    wind_avg, on='merge_cod', how= 'outer' ).merge(
    wind_max, on='merge_cod', how= 'outer' ).merge(
    wind_max_avg, on='merge_cod', how= 'outer' )

m_data['code_merge']= m_data['merge_cod']
m_data[['codigo',' estacion','year', 'month']]= m_data.merge_cod.str.split("_",expand=True)
        
m_data.to_csv (r'D:/Bootcamp/Data/estaciones.csv', index = False, header=True)
        

#fruta

fruta= pd.read_csv('E:/Kopuru/data general/FRUTALES-DECLARADOS-KOPURU.csv', sep=';')
fruta.to_csv (r'D:/Bootcamp/Data/fruta.csv', index = False, header=True)
#met
met= pd.read_csv('E:/Kopuru/data general/LOCALIZACION-ESTACIONES-METEOROLOGICAS.csv', sep=';')
met.to_csv (r'D:/Bootcamp/Data/met.csv', index = False, header=True)
#apicu
apicu= pd.read_csv('E:/Kopuru/data general/APICULTURA_COLMENAS_KOPURU.csv', sep=';')
apicu.to_csv (r'D:/Bootcamp/Data/apicu.csv', index = False, header=True)


#nido

nido=pd.read_excel('E:/Kopuru/data general/datos-nidos-avispa-asiatica.xlsx')
nido.to_csv (r'D:/Bootcamp/Data/nido.csv', index = False, header=True)
