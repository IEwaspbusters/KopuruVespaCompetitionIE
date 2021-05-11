# -*- coding: utf-8 -*-
"""
Created on Mon May  10 11:23:50 2021

Script to create the yearly train and predict datasets (csv files) for the May 12, 2021 submission
to the Kopuru Challange.


@author: bejar
"""

# 

# Base -----------------------------------
import pandas as pd
import numpy as np
#import scipy.stats as ss


# GitHub ---------------------------------
import requests
import io

# Working environment
import os

# 'uncomment' your username below:
username = 'mariobejar'
# username = 'add PedroC's GitHub username here'
# username = 'add Mario's GitHub username here'
# username = 'add PedroG's GitHub username here'

# 'uncomment' your github personal access token below:
token = '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'

# Creates a re-usable GitHub session object with your creds in-built
github_session = requests.Session()
github_session.auth = (username, token)
    
# Downloading the datasets from GitHub
ds01 = "https://raw.githubusercontent.com/IEwaspbusters/KopuruVespaCompetitionIE/main/Input_open_data/ds01_PLANTILLA-RETO-AVISPAS-KOPURU.csv?token=ADAWFG4MASEXGP6OPXOOFRDAOYHIW"
ds02 = "https://raw.githubusercontent.com/IEwaspbusters/KopuruVespaCompetitionIE/main/Input_open_data/ds02_datos-nidos-avispa-asiatica.csv?token=ADAWFGZOUEKVV6QGYWM2TULAOUO4U"
ds03 = "https://raw.githubusercontent.com/IEwaspbusters/KopuruVespaCompetitionIE/main/Input_open_data/ds03_APICULTURA_COLMENAS_KOPURU.csv?token=ADAWFG3KVZCCJHNWNMXYMTLAOUO5Y"
ds04 = "https://raw.githubusercontent.com/IEwaspbusters/KopuruVespaCompetitionIE/main/Input_open_data/ds04_FRUTALES-DECLARADOS-KOPURU.csv?token=ADAWFGZYKXDSQTVUNMI2FGDAOURDU"
WBds01 = 'https://raw.githubusercontent.com/IEwaspbusters/KopuruVespaCompetitionIE/main/Competition_subs/2021-05-12_submit/WBds01_GEO.csv?token=ATVGE4N3F6YDSVY5BS5ADY3ATFNV2'
WBds02 = 'https://raw.githubusercontent.com/IEwaspbusters/KopuruVespaCompetitionIE/main/Competition_subs/2021-05-12_submit/WBds02_METEO_years.csv?token=ATVGE4OBM46JQZIVTYZR7B3ATF6TC'
population ='https://raw.githubusercontent.com/IEwaspbusters/KopuruVespaCompetitionIE/main/Other_open_data/population.csv?token=ATVGE4N4CRGSVCRDG2CGI53ATFQTA'


download01 = github_session.get(ds01).content
download02 = github_session.get(ds02).content
download03 = github_session.get(ds03).content
download04 = github_session.get(ds04).content
downloadWB01 = github_session.get(WBds01).content
downloadWB02 = github_session.get(WBds02).content
downloadpopulation = github_session.get(population).content


# Reading the downloaded content and making it a pandas dataframe
df01 = pd.read_csv(io.StringIO(download01.decode('utf-8')), sep=";")
df02 = pd.read_csv(io.StringIO(download02.decode('utf-8')), sep=",")
df03 = pd.read_csv(io.StringIO(download03.decode('utf-8')), sep=";")
df04 = pd.read_csv(io.StringIO(download04.decode('utf-8')), sep=";")
WBdf01 = pd.read_csv(io.StringIO(downloadWB01.decode('utf-8')), sep=",")
WBdf02 = pd.read_csv(io.StringIO(downloadWB02.decode('utf-8')), sep=",")
df_population = pd.read_csv(io.StringIO(downloadpopulation.decode('utf-8')), sep=",")



# Dropping and Renaming columns in accordance to the DataMap
# DataMap's URL: https://docs.google.com/spreadsheets/d/1Ad7s4IOmj9Tn2WcEOz4ArwedTzDs9Y0_EaUSm6uRHMQ/edit#gid=0

df01.columns = ['municip_code', 'municip_name', 'nests_2020']
df01.drop(columns=['nests_2020'], inplace=True) # just note that this is the final variable to predict in the competition

df02.drop(columns=['JARDUERA_ZENBAKIA/NUM_ACTUACION', 'ERABILTZAILEA_EU/USUARIO_EU', 'ERABILTZAILEA_CAS/USUARIO_CAS', 'HELBIDEA/DIRECCION', 'EGOERA_EU/ESTADO_EU', 'ITXIERAKO AGENTEA_EU/AGENTE CIERRE_EU', 'ITXIERAKO AGENTEA_CAS/AGENTE CIERRE_CAS'], inplace=True)
df02.columns = ['waspbust_id','year','nest_foundDate','municip_name','species','nest_locType','nest_hight','nest_diameter','nest_longitude','nest_latitude','nest_status','nest_judgementDate']

df03.drop(columns=['CP'], inplace=True)
df03.columns = ['municip_name','municip_code','colonies_amount']

df04.columns = ['agriculture_type','municip_code','municip_name']


# We don't have the "months" specified for any of the records in 2017 ('nest_foundDate' is incorrect for this year), so we'll drop those records
df02 = df02.drop(df02[df02['year'] == 2017].index, inplace = False)

# Cleaning municipality names in ds02 with names from ds01
df02_wrong_mun = ['ABADIÑO' ,'ABANTO Y CIERVANA' ,'ABANTO Y CIERVANA-ABANTO ZIERBENA' ,'AJANGIZ' ,'ALONSOTEGI' ,'AMOREBIETA-ETXANO' ,'AMOROTO' ,'ARAKALDO' ,'ARANTZAZU' ,'AREATZA' ,'ARRANKUDIAGA' ,'ARRATZU' ,'ARRIETA' ,'ARRIGORRIAGA' ,'ARTEA' ,'ARTZENTALES' ,'ATXONDO' ,'AULESTI' ,'BAKIO' ,'BALMASEDA' ,'BARAKALDO' ,'BARRIKA' ,'BASAURI' ,'BEDIA' ,'BERANGO' ,'BERMEO' ,'BERRIATUA' ,'BERRIZ' ,'BUSTURIA' ,'DERIO' ,'DIMA' ,'DURANGO' ,'EA' ,'ELANTXOBE' ,'ELORRIO' ,'ERANDIO' ,'EREÑO' ,'ERMUA' ,'ERRIGOITI' ,'ETXEBARRI' ,'ETXEBARRIA' ,'FORUA' ,'FRUIZ' ,'GALDAKAO' ,'GALDAMES' ,'GAMIZ-FIKA' ,'GARAI' ,'GATIKA' ,'GAUTEGIZ ARTEAGA' ,'GERNIKA-LUMO' ,'GETXO' ,'GETXO ' ,'GIZABURUAGA' ,'GORDEXOLA' ,'GORLIZ' ,'GUEÑES' ,'IBARRANGELU' ,'IGORRE' ,'ISPASTER' ,'IURRETA' ,'IZURTZA' ,'KARRANTZA HARANA/VALLE DE CARRANZA' ,'KARRANTZA HARANA-VALLE DE CARRANZA' ,'KORTEZUBI' ,'LANESTOSA' ,'LARRABETZU' ,'LAUKIZ' ,'LEIOA' ,'LEKEITIO' ,'LEMOA' ,'LEMOIZ' ,'LEZAMA' ,'LOIU' ,'MALLABIA' ,'MAÑARIA' ,'MARKINA-XEMEIN' ,'MARURI-JATABE' ,'MEÑAKA' ,'MENDATA' ,'MENDEXA' ,'MORGA' ,'MUNDAKA' ,'MUNGIA' ,'MUNITIBAR-ARBATZEGI' ,'MUNITIBAR-ARBATZEGI GERRIKAITZ' ,'MURUETA' ,'MUSKIZ' ,'MUXIKA' ,'NABARNIZ' ,'ONDARROA' ,'OROZKO' ,'ORTUELLA' ,'OTXANDIO' ,'PLENTZIA' ,'PORTUGALETE' ,'SANTURTZI' ,'SESTAO' ,'SONDIKA' ,'SOPELA' ,'SOPUERTA' ,'SUKARRIETA' ,'TRUCIOS-TURTZIOZ' ,'UBIDE' ,'UGAO-MIRABALLES' ,'URDULIZ' ,'URDUÑA/ORDUÑA' ,'URDUÑA-ORDUÑA' ,'VALLE DE TRAPAGA' ,'VALLE DE TRAPAGA-TRAPAGARAN' ,'ZALDIBAR' ,'ZALLA' ,'ZAMUDIO' ,'ZARATAMO' ,'ZEANURI' ,'ZEBERIO' ,'ZIERBENA' ,'ZIORTZA-BOLIBAR' ]
df02_correct_mun = ['Abadiño' ,'Abanto y Ciérvana-Abanto Zierbena' ,'Abanto y Ciérvana-Abanto Zierbena' ,'Ajangiz' ,'Alonsotegi' ,'Amorebieta-Etxano' ,'Amoroto' ,'Arakaldo' ,'Arantzazu' ,'Areatza' ,'Arrankudiaga' ,'Arratzu' ,'Arrieta' ,'Arrigorriaga' ,'Artea' ,'Artzentales' ,'Atxondo' ,'Aulesti' ,'Bakio' ,'Balmaseda' ,'Barakaldo' ,'Barrika' ,'Basauri' ,'Bedia' ,'Berango' ,'Bermeo' ,'Berriatua' ,'Berriz' ,'Busturia' ,'Derio' ,'Dima' ,'Durango' ,'Ea' ,'Elantxobe' ,'Elorrio' ,'Erandio' ,'Ereño' ,'Ermua' ,'Errigoiti' ,'Etxebarri' ,'Etxebarria' ,'Forua' ,'Fruiz' ,'Galdakao' ,'Galdames' ,'Gamiz-Fika' ,'Garai' ,'Gatika' ,'Gautegiz Arteaga' ,'Gernika-Lumo' ,'Getxo' ,'Getxo' ,'Gizaburuaga' ,'Gordexola' ,'Gorliz' ,'Güeñes' ,'Ibarrangelu' ,'Igorre' ,'Ispaster' ,'Iurreta' ,'Izurtza' ,'Karrantza Harana/Valle de Carranza' ,'Karrantza Harana/Valle de Carranza' ,'Kortezubi' ,'Lanestosa' ,'Larrabetzu' ,'Laukiz' ,'Leioa' ,'Lekeitio' ,'Lemoa' ,'Lemoiz' ,'Lezama' ,'Loiu' ,'Mallabia' ,'Mañaria' ,'Markina-Xemein' ,'Maruri-Jatabe' ,'Meñaka' ,'Mendata' ,'Mendexa' ,'Morga' ,'Mundaka' ,'Mungia' ,'Munitibar-Arbatzegi Gerrikaitz' ,'Munitibar-Arbatzegi Gerrikaitz' ,'Murueta' ,'Muskiz' ,'Muxika' ,'Nabarniz' ,'Ondarroa' ,'Orozko' ,'Ortuella' ,'Otxandio' ,'Plentzia' ,'Portugalete' ,'Santurtzi' ,'Sestao' ,'Sondika' ,'Sopela' ,'Sopuerta' ,'Sukarrieta' ,'Trucios-Turtzioz' ,'Ubide' ,'Ugao-Miraballes' ,'Urduliz' ,'Urduña/Orduña' ,'Urduña/Orduña' ,'Valle de Trápaga-Trapagaran' ,'Valle de Trápaga-Trapagaran' ,'Zaldibar' ,'Zalla' ,'Zamudio' ,'Zaratamo' ,'Zeanuri' ,'Zeberio' ,'Zierbena' ,'Ziortza-Bolibar',]
df02.municip_name.replace(to_replace = df02_wrong_mun, value = df02_correct_mun, inplace = True )
df02.shape


# Merge dataFrames df01 and df02 by 'municip_name', in order to identify every wasp nest with its 'municip_code'
# The intention is that 'all_the_queens-wasps' will be the final dataFrame to use in the ML model eventually
all_the_queens_wasps = pd.merge(df02, df01, how = 'left', on = 'municip_name')


# Group df03 by 'municip_code' because there are multiple rows for each municipality (and we need a 1:1 relationship)
df03 = df03.groupby(by = 'municip_code', as_index= False).colonies_amount.sum()


# Changing 'nest_foundDate' the to "datetime" format
all_the_queens_wasps['nest_foundDate'] = pd.to_datetime(all_the_queens_wasps['nest_foundDate'])


# Create a "year_offset" variable in the main dataframe
# IMPORTANT: THIS REFLECTS OUR ASSUMPTION THAT YEAR-1 DATA CAN BE USE TO PREDICT YEAR DATA
all_the_queens_wasps['year_offset'] = pd.DatetimeIndex(all_the_queens_wasps['nest_foundDate']).year -1

# Selecting and grouping the necessary variables for the larvae model
#It will be an OLS model with a reduced data structure consisting of - location (municipality) - year - month + all weather and food_source variables (fruits and bees)
#waspbust_id will now contain the number of wasps nests pero municip - month - year
 
all_the_queens_wasps = all_the_queens_wasps.loc[all_the_queens_wasps.species == 'AVISPA ASIÁTICA',['waspbust_id','year', 'municip_name', 'species', 'municip_code','year_offset']].groupby( by =['year', 'municip_name', 'species', 'municip_code', 'year_offset'], as_index = False).count()


# Now merge df03 to add number of bee hives in each municipality
# Note that we're also replacing NaNs (unknown amount of hives) with zeroes for the 'colonies_amount' variable
all_the_queens_wasps = pd.merge(all_the_queens_wasps, df03, how = 'left', on= 'municip_code')
all_the_queens_wasps.colonies_amount.fillna(value=0, inplace=True)


# Group df04 by municipality code, while appending variables with the amount of each type of agricultural product
aux = df04.copy(deep=True)
aux.drop(columns=['municip_name'], inplace=True)

aux['food_fruit'] = np.where(aux['agriculture_type'] == 'FRUTALES', '1', '0')
aux['food_fruit'] = aux['food_fruit'].astype('int')

aux['food_apple'] = np.where(aux['agriculture_type'] == 'MANZANO', '1', '0')
aux['food_apple'] = aux['food_apple'].astype('int')

txakoli_string = df04.agriculture_type[45]
aux['food_txakoli'] = np.where(aux['agriculture_type'] == txakoli_string, '1', '0')
aux['food_txakoli'] = aux['food_txakoli'].astype('int')

aux['food_kiwi'] = np.where(aux['agriculture_type'] == 'AKTINIDIA (KIWI)', '1', '0')
aux['food_kiwi'] = aux['food_kiwi'].astype('int')

aux['food_pear'] = np.where(aux['agriculture_type'] == 'PERAL', '1', '0')
aux['food_pear'] = aux['food_pear'].astype('int')

aux['food_blueberry'] = np.where(aux['agriculture_type'] == 'ARANDANOS', '1', '0')
aux['food_blueberry'] = aux['food_blueberry'].astype('int')

aux['food_raspberry'] = np.where(aux['agriculture_type'] == 'FRAMBUESAS', '1', '0')
aux['food_raspberry'] = aux['food_raspberry'].astype('int')

aux = aux.groupby(by='municip_code', as_index=False).sum()
df04 = aux.copy(deep=True)


# Now merge df04 to add number of each type of food source ('agriculture_type') present in each municipality
# Any municipality not present in df04 will get a 'zero' as substitute for NaN
all_the_queens_wasps = pd.merge(all_the_queens_wasps, df04, how = 'left', on= 'municip_code')
all_the_queens_wasps.food_fruit.fillna(value=0, inplace=True)
all_the_queens_wasps.food_apple.fillna(value=0, inplace=True)
all_the_queens_wasps.food_txakoli.fillna(value=0, inplace=True)
all_the_queens_wasps.food_kiwi.fillna(value=0, inplace=True)
all_the_queens_wasps.food_pear.fillna(value=0, inplace=True)
all_the_queens_wasps.food_blueberry.fillna(value=0, inplace=True)
all_the_queens_wasps.food_raspberry.fillna(value=0, inplace=True)


# Adding weather station code to main dataset "no municipality left behind!"
all_the_queens_wasps = pd.merge(all_the_queens_wasps, WBdf01, how = 'left', on= 'municip_code')


# Now, merge the Main 'all_the_queens_wasps' dataFrame with the weather data 'WBdf02' dataFrame
all_the_queens_wasps = pd.merge(all_the_queens_wasps, WBdf02, how = 'left', left_on = ['station_code', 'year_offset'], right_on = ['codigo', 'year'])

# Translate the Euskara/Spanish contents to English
all_the_queens_wasps.species.replace(to_replace=['AVISPA ASIÁTICA', 'AVISPA COMÚN', 'ABEJA'], value=['Vespa Velutina', 'Common Wasp', 'Wild Bee'], inplace=True)
#all_the_queens_wasps.nest_locType.replace(to_replace=['CONSTRUCCIÓN', 'ARBOLADO'], value=['Urban Environment', 'Natural Environment'], inplace=True)
#all_the_queens_wasps.nest_status.replace(to_replace=['CERRADA - ELIMINADO', 'CERRADA - NO ELIMINABLE', 'PENDIENTE DE GRUPO'], value=['Nest Terminated', 'Cannot Terminate', 'Pending classification'], inplace=True)


# Adding population by municipality
all_the_queens_wasps = pd.merge(all_the_queens_wasps, df_population, how = 'left', left_on= ['municip_code', 'year_x'], right_on = ['municip_code', 'year'])


#dropping unnecessary/duplicate columns
all_the_queens_wasps.drop(columns=['year_y','codigo', 'year'], inplace=True)


# Save the new dataFrame as a .csv in the current working directory on Windows
cwd = os.getcwd()
path = cwd + "/WBds03_QUEENtrain_years.csv"
all_the_queens_wasps.to_csv(path, index=False)


#From here on: script to create the WBds03_QUEENpredict.csv

# Downloading the datasets from GitHub

pred_temp = 'https://raw.githubusercontent.com/IEwaspbusters/KopuruVespaCompetitionIE/main/Other_open_data/predict_template_years.csv?token=ATVGE4LJTPM3GRZWHHYULF3ATF74O'
downloadpred_temp = github_session.get(pred_temp).content

# Reading the downloaded content and making it a pandas dataframe
df_temp = pd.read_csv(io.StringIO(downloadpred_temp.decode('utf-8')), sep=",")


# Now merge df03 to add number of bee hives in each municipality
# Note that we're also replacing NaNs (unknown amount of hives) with zeroes for the 'colonies_amount' variable
df_temp = pd.merge(df_temp, df03, how = 'left', on= 'municip_code')
df_temp.colonies_amount.fillna(value=0, inplace=True)

# Now merge df04 to add number of each type of food source ('agriculture_type') present in each municipality
# Any municipality not present in df04 will get a 'zero' as substitute for NaN
df_temp = pd.merge(df_temp, df04, how = 'left', on= 'municip_code')
df_temp.food_fruit.fillna(value=0, inplace=True)
df_temp.food_apple.fillna(value=0, inplace=True)
df_temp.food_txakoli.fillna(value=0, inplace=True)
df_temp.food_kiwi.fillna(value=0, inplace=True)
df_temp.food_pear.fillna(value=0, inplace=True)
df_temp.food_blueberry.fillna(value=0, inplace=True)
df_temp.food_raspberry.fillna(value=0, inplace=True)


# Adding weather station code to main dataset "no municipality left behind!"
df_temp = pd.merge(df_temp, WBdf01, how = 'left', on= 'municip_code')

# Now, merge de_temp with dataFrame with the weather data 'WBdf02' dataFrame
df_temp = pd.merge(df_temp, WBdf02, how = 'left', left_on = ['station_code', 'year_offset'], right_on = ['codigo', 'year'])

# Adding population by municipality
df_temp = pd.merge(df_temp, df_population, how = 'left', left_on= ['municip_code', 'year_x'], right_on = ['municip_code', 'year'])


#dropping unnecessary/duplicate columns
df_temp.drop(columns=['year_y','codigo', 'year'], inplace=True)



# Save the new dataFrame as a .csv in the current working directory on Windows
cwd = os.getcwd()
path = cwd + "/WBds03_QUEENpredict_years.csv"
df_temp.to_csv(path, index=False)


