# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 06:18:34 2021

@authors:
    mario.bejar@student.ie.edu
    isabel.perezdobarro@student.ie.edu
    pedro.geirinhas@student.ie.edu
    a.berrizbeitia@student.ie.edu
    pcasaverde@student.ie.edu
"""

# Base -----------------------------------
import pandas as pd
import numpy as np
#import scipy.stats as ss

# Viz ------------------------------------
#import seaborn as sns
#import matplotlib.pyplot as plt

# GitHub ---------------------------------
import requests
import io

# Working environment
import os

## 'uncomment' your username below:
username = 'narrativus'
## username = 'add PedroC's GitHub username here'
## username = 'add Mario's GitHub username here'
## username = 'add Isa's GitHub username here'
## username = 'add PedroG's GitHub username here'

## 'uncomment' your github personal access token below:
token = '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'
## token = 'add PedroC's GitHub token here'
## token = 'add Mario's GitHub token here'
## token = 'add Isa's GitHub token here'
## token = 'add PedroG's GitHub token here'

# Creates a re-usable GitHub session object with your creds in-built
github_session = requests.Session()
github_session.auth = (username, token)
    
# Downloading the datasets from GitHub
ds01 = "https://raw.githubusercontent.com/IEwaspbusters/KopuruVespaCompetitionIE/main/Input_open_data/ds01_PLANTILLA-RETO-AVISPAS-KOPURU.csv?token=ADAWFG4CKOYHU2ONTL6WYZTAOODGY"
ds02 = "https://raw.githubusercontent.com/IEwaspbusters/KopuruVespaCompetitionIE/main/Input_open_data/ds02_datos-nidos-avispa-asiatica.csv?token=ADAWFGZOUEKVV6QGYWM2TULAOUO4U"
ds03 = "https://raw.githubusercontent.com/IEwaspbusters/KopuruVespaCompetitionIE/main/Input_open_data/ds03_APICULTURA_COLMENAS_KOPURU.csv?token=ADAWFG3KVZCCJHNWNMXYMTLAOUO5Y"
ds04 = "https://raw.githubusercontent.com/IEwaspbusters/KopuruVespaCompetitionIE/main/Input_open_data/ds04_FRUTALES-DECLARADOS-KOPURU.csv?token=ADAWFGZYKXDSQTVUNMI2FGDAOURDU"
WBds01 = 'https://raw.githubusercontent.com/IEwaspbusters/KopuruVespaCompetitionIE/main/Team_datasets/WBds01_weather2municipality.csv?token=ADAWFG5CMUNPUZZTVPBENZTAOVJCG'
WBds02 = 'https://raw.githubusercontent.com/IEwaspbusters/KopuruVespaCompetitionIE/main/Team_datasets/WBds02_weather_agg_imputed.csv?token=ADAWFG7GVCYAOXMG64DFXQTAOVOJ6'
download01 = github_session.get(ds01).content
download02 = github_session.get(ds02).content
download03 = github_session.get(ds03).content
download04 = github_session.get(ds04).content
downloadWB01 = github_session.get(WBds01).content
downloadWB02 = github_session.get(WBds02).content

# Reading the downloaded content and making it a pandas dataframe
df01 = pd.read_csv(io.StringIO(download01.decode('utf-8')), sep=";")
df02 = pd.read_csv(io.StringIO(download02.decode('utf-8')), sep=",")
df03 = pd.read_csv(io.StringIO(download03.decode('utf-8')), sep=";")
df04 = pd.read_csv(io.StringIO(download04.decode('utf-8')), sep=";")
WBdf01 = pd.read_csv(io.StringIO(downloadWB01.decode('utf-8')), sep=",")
WBdf02 = pd.read_csv(io.StringIO(downloadWB02.decode('utf-8')), sep=",")


# Dropping and Renaming columns in accordance to the DataMap
# DataMap's URL: https://docs.google.com/spreadsheets/d/1Ad7s4IOmj9Tn2WcEOz4ArwedTzDs9Y0_EaUSm6uRHMQ/edit#gid=0

df01.columns = ['municip_code', 'municip_name', 'nests_2020']
df01.drop(columns=['nests_2020'], inplace=True) # just note that this is the final variable to predict in the competition

df02.drop(columns=['URTEA/ANIO', 'JARDUERA_ZENBAKIA/NUM_ACTUACION', 'ERABILTZAILEA_EU/USUARIO_EU', 'ERABILTZAILEA_CAS/USUARIO_CAS', 'HELBIDEA/DIRECCION', 'EGOERA_EU/ESTADO_EU', 'ITXIERAKO AGENTEA_EU/AGENTE CIERRE_EU', 'ITXIERAKO AGENTEA_CAS/AGENTE CIERRE_CAS'], inplace=True)
df02.columns = ['waspbust_id','nest_foundDate','municip_name','species','nest_locType','nest_hight','nest_diameter','nest_longitude','nest_latitude','nest_status','nest_judgementDate']

df03.drop(columns=['CP'], inplace=True)
df03.columns = ['municip_name','municip_code','colonies_amount']

df04.columns = ['agriculture_type','municip_code','municip_name']


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

#txakoli_string = df04.agriculture_type[45]
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

# Changing 'nest_foundDate' the to "datetime" format
all_the_queens_wasps['nest_foundDate'] = pd.to_datetime(all_the_queens_wasps['nest_foundDate'])

# Create a "month" variable in the main dataframe
all_the_queens_wasps['month'] = pd.DatetimeIndex(all_the_queens_wasps['nest_foundDate']).month

# Create a "year_offset" variable in the main dataframe
# IMPORTANT: THIS REFLECTS OUR ASSUMPTION THAT YEAR-1 DATA CAN BE USE TO PREDICT YEAR DATA
all_the_queens_wasps['year_offset'] = pd.DatetimeIndex(all_the_queens_wasps['nest_foundDate']).year-1

# Now, merge the Main 'all_the_queens_wasps' dataFrame with the weather data 'WBdf02' dataFrame
all_the_queens_wasps = pd.merge(all_the_queens_wasps, WBdf02, how = 'left', left_on = ['station_code', 'month', 'year_offset'], right_on = ['station_code', 'month', 'year'])

# But, as we don't have the "months" specified for any of the records in 2017 ('nest_foundDate' is incorrect for this year), we'll drop those records
#all_the_queens_wasps = all_the_queens_wasps.drop(all_the_queens_wasps[all_the_queens_wasps['nest_foundDate'] == 2017].index, inplace = True)

# Save the new dataFrame as a .csv in the current working directory on Windows
cwd = os.getcwd()
path = cwd + "/WBds03_all_the_queens_wasps.csv"
all_the_queens_wasps.to_csv(path, index=False)


