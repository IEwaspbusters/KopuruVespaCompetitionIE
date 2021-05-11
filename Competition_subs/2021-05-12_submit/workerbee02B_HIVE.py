# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 19:47:50 2021

@author: Usuario
"""


import pandas as pd
import numpy as np
from datawig import SimpleImputer
from datawig.utils import random_split
from sklearn.metrics import f1_score, classification_report, precision_score, recall_score, r2_score, mean_squared_error
from sklearn.ensemble import RandomForestRegressor as rfr
from sklearn.datasets import make_regression

seasons= pd.read_csv('D:/Bootcamp/Data/estaciones.csv')

seasons.columns



#Hum----------------------------------------------------------------------------------------


df_train, df_test = random_split(seasons, split_ratios=[0.8, 0.2])

#Initialize a SimpleImputer model
imputer_hum = SimpleImputer(
input_columns=['month','freez', 'temp_avg', 'rain','wind_avg','rain_1mm','rain_cum','rain_max_10','rain_max_day'],
output_column='hum',
output_path = 'imputer_model'
)

#Fit an imputer model on the train data
imputer_hum.fit(train_df=df_train)
predictions_hum = imputer_hum.predict(df_test)

pre_hum= predictions_hum.loc[~predictions_hum['hum'].isnull(),['hum','hum_imputed'] ]

#Calculate f1 score
r2_hum = r2_score(pre_hum['hum'], pre_hum['hum_imputed'])
msq_hum = mean_squared_error(pre_hum['hum'], pre_hum['hum_imputed'])


#completing hum data

seasons_1= imputer_hum.predict(seasons.loc[seasons['hum'].isnull(),:])
del seasons_1["hum"]
seasons_1=seasons_1.rename(columns={'hum_imputed':'hum'}).append(seasons.loc[~seasons['hum'].isnull(),:])


#Freez----------------------------------------------------------------------------------------

df_train, df_test= random_split(seasons_1, split_ratios=[0.8, 0.2])

#Initialize a SimpleImputer model
imputer_freez = SimpleImputer(
input_columns=['month','hum', 'temp_avg', 'rain','wind_avg'],
output_column='freez',
output_path = 'imputer_model'
)

#Fit an imputer model on the train data
imputer_freez.fit(train_df=df_train)
predictions_freez = imputer_freez.predict(df_test)

pre_freez= predictions_freez.loc[~predictions_freez['freez'].isnull(),['freez','freez_imputed'] ]

#Calculate R2 & MSE
r2_freez = r2_score(pre_freez['freez'], pre_freez['freez_imputed'])
msq_freez = mean_squared_error(pre_freez['freez'], pre_freez['freez_imputed'])

seasons_2= imputer_freez.predict(seasons_1.loc[seasons_1['freez'].isnull(),:])
del seasons_2["freez"]
seasons_2=seasons_2.rename(columns={'freez_imputed':'freez'}).append(seasons_1.loc[~seasons['freez'].isnull(),:])



#Rain----------------------------------------------------------------------------------------

df_train, df_test = random_split(seasons_2, split_ratios=[0.8, 0.2])

#Initialize a SimpleImputer model
imputer_rain = SimpleImputer(
input_columns=['month','hum', 'temp_avg','wind_avg', 'freez','rain_1mm','rain_cum','rain_max_10','rain_max_day'],
output_column='rain',
output_path = 'imputer_model'
)

#Fit an imputer model on the train data
imputer_rain.fit(train_df=df_train)
predictions_rain = imputer_rain.predict(df_test)

pre_rain= predictions_rain.loc[~predictions_rain['rain'].isnull(),['rain','rain_imputed'] ]

#Calculate R2 & MSE
r2_rain = r2_score(pre_rain['rain'], pre_rain['rain_imputed'])
msq_rain = mean_squared_error(pre_rain['rain'], pre_rain['rain_imputed'])

seasons_3= imputer_rain.predict(seasons_2.loc[seasons_2['rain'].isnull(),:])
del seasons_3["rain"]
seasons_3=seasons_3.rename(columns={'rain_imputed':'rain'}).append(seasons_2.loc[~seasons['rain'].isnull(),:])


#lev_max----------------------------------------------------------------------------------------

df_train, df_test = random_split(seasons_3, split_ratios=[0.8, 0.2])

#Initialize a SimpleImputer model
imputer_lev_max = SimpleImputer(
input_columns=['hum', 'temp_avg','wind_avg', 'rain', 'freez','sun','lev_mid','lev_min'],
output_column='lev_max',
output_path = 'imputer_model'
)

#Fit an imputer model on the train data
imputer_lev_max.fit(train_df=df_train)
predictions_lev_max = imputer_lev_max.predict(df_test)

pre_lev_max= predictions_lev_max.loc[~predictions_lev_max['lev_max'].isnull(),['lev_max','lev_max_imputed'] ]

#Calculate R2 & MSE
r2_lev_max = r2_score(pre_lev_max['lev_max'], pre_lev_max['lev_max_imputed'])
msq_lev_max = mean_squared_error(pre_lev_max['lev_max'], pre_lev_max['lev_max_imputed'])

seasons_4= imputer_lev_max.predict(seasons_3.loc[seasons_3['lev_max'].isnull(),:])
del seasons_4["lev_max"]
seasons_4=seasons_4.rename(columns={'lev_max_imputed':'lev_max'}).append(seasons_3.loc[~seasons['lev_max'].isnull(),:])


#lev_mid----------------------------------------------------------------------------------------

df_train, df_test = random_split(seasons_4, split_ratios=[0.8, 0.2])

#Initialize a SimpleImputer model
imputer_lev_mid = SimpleImputer(
input_columns=['hum', 'temp_avg','wind_avg', 'rain', 'freez','sun','lev_min','lev_max'],
output_column='lev_mid',
output_path = 'imputer_model'
)

#Fit an imputer model on the train data
imputer_lev_mid.fit(train_df=df_train)
predictions_lev_mid = imputer_lev_mid.predict(df_test)

pre_lev_mid= predictions_lev_mid.loc[~predictions_lev_mid['lev_mid'].isnull(),['lev_mid','lev_mid_imputed'] ]

#Calculate R2 & MSE
r2_lev_mid = r2_score(pre_lev_mid['lev_mid'], pre_lev_mid['lev_mid_imputed'])
msq_lev_mid = mean_squared_error(pre_lev_mid['lev_mid'], pre_lev_mid['lev_mid_imputed'])

seasons_5= imputer_lev_mid.predict(seasons_4.loc[seasons_4['lev_mid'].isnull(),:])
del seasons_5["lev_mid"]
seasons_5=seasons_5.rename(columns={'lev_mid_imputed':'lev_mid'}).append(seasons_4.loc[~seasons['lev_mid'].isnull(),:])



#lev_min----------------------------------------------------------------------------------------

df_train, df_test = random_split(seasons_5, split_ratios=[0.8, 0.2])

#Initialize a SimpleImputer model
imputer_lev_min = SimpleImputer(
input_columns=['hum', 'temp_avg','wind_avg', 'rain', 'freez','sun','lev_mid','lev_max'],
output_column='lev_min',
output_path = 'imputer_model'
)

#Fit an imputer model on the train data
imputer_lev_min.fit(train_df=df_train)
predictions_lev_min = imputer_lev_min.predict(df_test)

pre_lev_min= predictions_lev_min.loc[~predictions_lev_min['lev_min'].isnull(),['lev_min','lev_min_imputed'] ]

#Calculate R2 & MSE
r2_lev_min = r2_score(pre_lev_min['lev_min'], pre_lev_min['lev_min_imputed'])
msq_lev_min = mean_squared_error(pre_lev_min['lev_min'], pre_lev_min['lev_min_imputed'])

seasons_6= imputer_lev_min.predict(seasons_5.loc[seasons_5['lev_min'].isnull(),:])
del seasons_6["lev_min"]
seasons_6=seasons_6.rename(columns={'lev_min_imputed':'lev_min'}).append(seasons_5.loc[~seasons['lev_min'].isnull(),:])


#rain_1mm----------------------------------------------------------------------------------------

df_train, df_test = random_split(seasons_6, split_ratios=[0.8, 0.2])

#Initialize a SimpleImputer model
imputer_rain_1mmn = SimpleImputer(
input_columns=['hum', 'temp_avg','wind_avg', 'rain', 'freez','sun','rain_cum','rain_max_10','rain_max_day'],
output_column='rain_1mm',
output_path = 'imputer_model'
)

#Fit an imputer model on the train data
imputer_rain_1mmn.fit(train_df=df_train)
predictions_rain_1mm = imputer_rain_1mmn.predict(df_test)

pre_rain_1mm= predictions_rain_1mm.loc[~predictions_rain_1mm['rain_1mm'].isnull(),['rain_1mm','rain_1mm_imputed'] ]

#Calculate R2 & MSE
r2_rain_1mm = r2_score(pre_rain_1mm['rain_1mm'], pre_rain_1mm['rain_1mm_imputed'])
msq_rain_1mm = mean_squared_error(pre_rain_1mm['rain_1mm'], pre_rain_1mm['rain_1mm_imputed'])

seasons_7= imputer_rain_1mmn.predict(seasons_6.loc[seasons_6['rain_1mm'].isnull(),:])
del seasons_7["rain_1mm"]
seasons_7=seasons_7.rename(columns={'rain_1mm_imputed':'rain_1mm'}).append(seasons_6.loc[~seasons['rain_1mm'].isnull(),:])


#rain_cum ----------------------------------------------------------------------------------------

df_train, df_test = random_split(seasons_7, split_ratios=[0.8, 0.2])

#Initialize a SimpleImputer model
imputer_rain_cum  = SimpleImputer(
input_columns=['hum', 'temp_avg','wind_avg', 'freez','sun','rain_1mm','rain_max_10','rain_max_day','lev_max','lev_mid','lev_min'],
output_column='rain_cum',
output_path = 'imputer_model'
)

#Fit an imputer model on the train data
imputer_rain_cum.fit(train_df=df_train)
predictions_rain_cum  = imputer_rain_cum.predict(df_test)

pre_rain_cum = predictions_rain_cum.loc[~predictions_rain_cum ['rain_cum'].isnull(),['rain_cum','rain_cum_imputed'] ]

#Calculate R2 & MSE
r2_rain_cum = r2_score(pre_rain_cum['rain_cum'], pre_rain_cum['rain_cum_imputed'])
msq_rain_cum = mean_squared_error(pre_rain_cum['rain_cum'], pre_rain_cum['rain_cum_imputed'])

seasons_8= imputer_rain_cum.predict(seasons_7.loc[seasons_7['rain_cum'].isnull(),:])
del seasons_8["rain_cum"]
seasons_8=seasons_8.rename(columns={'rain_cum_imputed':'rain_cum'}).append(seasons_7.loc[~seasons['rain_cum'].isnull(),:])

#rain_max_10----------------------------------------------------------------------------------------

df_train, df_test = random_split(seasons_8, split_ratios=[0.8, 0.2])

#Initialize a SimpleImputer model
imputer_rain_max_10 = SimpleImputer(
input_columns=['hum', 'temp_avg','wind_avg', 'rain', 'freez','sun','rain_cum','rain_1mm','rain_max_day'],
output_column='rain_max_10',
output_path = 'imputer_model'
)

#Fit an imputer model on the train data
imputer_rain_max_10.fit(train_df=df_train)
predictions_rain_max_10 = imputer_rain_max_10.predict(df_test)

pre_rain_max_10= predictions_rain_max_10.loc[~predictions_rain_max_10['rain_max_10'].isnull(),['rain_max_10','rain_max_10_imputed'] ]

#Calculate R2 & MSE
r2_rain_max_10 = r2_score(pre_rain_max_10['rain_max_10'], pre_rain_max_10['rain_max_10_imputed'])
msq_rain_max_10= mean_squared_error(pre_rain_max_10['rain_max_10'], pre_rain_max_10['rain_max_10_imputed'])

seasons_9= imputer_rain_max_10.predict(seasons_8.loc[seasons_8['rain_max_10'].isnull(),:])
del seasons_9["rain_max_10"]
seasons_9=seasons_9.rename(columns={'rain_max_10_imputed':'rain_max_10'}).append(seasons_8.loc[~seasons['rain_max_10'].isnull(),:])


#rain_max_day----------------------------------------------------------------------------------------

df_train, df_test = random_split(seasons_9, split_ratios=[0.8, 0.2])

#Initialize a SimpleImputer model
imputer_rain_max_day = SimpleImputer(
input_columns=['month','hum', 'temp_avg','wind_avg', 'rain', 'freez','sun','rain_cum','rain_1mm','rain_max_10'],
output_column='rain_max_day',
output_path = 'imputer_model'
)

#Fit an imputer model on the train data
imputer_rain_max_day.fit(train_df=df_train)
predictions_rain_max_day = imputer_rain_max_day.predict(df_test)

pre_rain_max_day =predictions_rain_max_day.loc[~predictions_rain_max_day['rain_max_day'].isnull(),['rain_max_day','rain_max_day_imputed'] ]

#Calculate R2 & MSE
r2_rain_max_day = r2_score(pre_rain_max_day['rain_max_day'], pre_rain_max_day['rain_max_day_imputed'])
msq_rain_max_day= mean_squared_error(pre_rain_max_day['rain_max_day'], pre_rain_max_day['rain_max_day_imputed'])

seasons_10= imputer_rain_max_day.predict(seasons_9.loc[seasons_9['rain_max_day'].isnull(),:])
del seasons_10["rain_max_day"]
seasons_10=seasons_10.rename(columns={'rain_max_day_imputed':'rain_max_day'}).append(seasons_9.loc[~seasons['rain_max_10'].isnull(),:])



#temp_avg----------------------------------------------------------------------------------------

df_train, df_test = random_split(seasons_10, split_ratios=[0.8, 0.2])

#Initialize a SimpleImputer model
imputer_temp_avg = SimpleImputer(
input_columns=['hum','wind_avg', 'rain', 'freez','sun','temp_max_abs','temp_max_avg','temp_min_abs'],
output_column='temp_avg',
output_path = 'imputer_model'
)

#Fit an imputer model on the train data
imputer_temp_avg.fit(train_df=df_train)
predictions_temp_avg = imputer_temp_avg.predict(df_test)

pre_temp_avg =predictions_temp_avg.loc[~predictions_temp_avg['temp_avg'].isnull(),['temp_avg','temp_avg_imputed'] ]

#Calculate R2 & MSE
r2_temp_avg = r2_score(pre_temp_avg['temp_avg'], pre_temp_avg['temp_avg_imputed'])
msq_temp_avg= mean_squared_error(pre_temp_avg['temp_avg'], pre_temp_avg['temp_avg_imputed'])

seasons_11= imputer_temp_avg.predict(seasons_10.loc[seasons_10['temp_avg'].isnull(),:])
del seasons_11["temp_avg"]
seasons_11=seasons_11.rename(columns={'temp_avg_imputed':'temp_avg'}).append(seasons_10.loc[~seasons['temp_avg'].isnull(),:])




#temp_max_abs----------------------------------------------------------------------------------------

df_train, df_test = random_split(seasons_11, split_ratios=[0.8, 0.2])

#Initialize a SimpleImputer model
imputer_temp_max_abs = SimpleImputer(
input_columns=['hum','wind_avg', 'rain', 'freez','sun','temp_max_avg','temp_avg','temp_min_abs'],
output_column='temp_max_abs',
output_path = 'imputer_model'
)

#Fit an imputer model on the train data
imputer_temp_max_abs.fit(train_df=df_train)
predictions_temp_max_abs = imputer_temp_max_abs.predict(df_test)

pre_temp_max_abs=predictions_temp_max_abs.loc[~predictions_temp_max_abs['temp_max_abs'].isnull(),['temp_max_abs','temp_max_abs_imputed'] ]

#Calculate R2 & MSE
r2_temp_max_abs= r2_score(pre_temp_max_abs['temp_max_abs'], pre_temp_max_abs['temp_max_abs_imputed'])
msq_temp_max_abs= mean_squared_error(pre_temp_max_abs['temp_max_abs'], pre_temp_max_abs['temp_max_abs_imputed'])

seasons_12= imputer_temp_max_abs.predict(seasons_11.loc[seasons_11['temp_max_abs'].isnull(),:])
del seasons_12["temp_max_abs"]
seasons_12=seasons_12.rename(columns={'temp_max_abs_imputed':'temp_max_abs'}).append(seasons_11.loc[~seasons['temp_max_abs'].isnull(),:])


#temp_max_avg----------------------------------------------------------------------------------------

df_train, df_test = random_split(seasons_12, split_ratios=[0.8, 0.2])

#Initialize a SimpleImputer model
imputer_temp_max_avg = SimpleImputer(
input_columns=['hum','wind_avg', 'rain', 'freez','sun','temp_max_abs','temp_avg','temp_min_abs'],
output_column='temp_max_avg',
output_path = 'imputer_model'
)

#Fit an imputer model on the train data
imputer_temp_max_avg.fit(train_df=df_train)
predictions_temp_max_avg= imputer_temp_max_avg.predict(df_test)

pre_temp_max_avg=predictions_temp_max_avg.loc[~predictions_temp_max_avg['temp_max_avg'].isnull(),['temp_max_avg','temp_max_avg_imputed'] ]

#Calculate R2 & MSE
r2_temp_max_avg= r2_score(pre_temp_max_avg['temp_max_avg'], pre_temp_max_avg['temp_max_avg_imputed'])
msq_temp_max_avg= mean_squared_error(pre_temp_max_avg['temp_max_avg'], pre_temp_max_avg['temp_max_avg_imputed'])

seasons_13= imputer_temp_max_avg.predict(seasons_12.loc[seasons_12['temp_max_avg'].isnull(),:])
del seasons_13["temp_max_avg"]
seasons_13=seasons_13.rename(columns={'temp_max_avg_imputed':'temp_max_avg'}).append(seasons_12.loc[~seasons['temp_max_avg'].isnull(),:])


#temp_min_abs----------------------------------------------------------------------------------------

df_train, df_test = random_split(seasons_13, split_ratios=[0.8, 0.2])

#Initialize a SimpleImputer model
imputer_temp_min_abs = SimpleImputer(
input_columns=['hum','wind_avg', 'rain', 'freez','sun','temp_max_abs','temp_avg','temp_max_avg'],
output_column='temp_min_abs',
output_path = 'imputer_model'
)

#Fit an imputer model on the train data
imputer_temp_min_abs.fit(train_df=df_train)
predictions_temp_min_abs= imputer_temp_min_abs.predict(df_test)

pre_temp_min_abs=predictions_temp_min_abs.loc[~predictions_temp_min_abs['temp_min_abs'].isnull(),['temp_min_abs','temp_min_abs_imputed'] ]

#Calculate R2 & MSE
r2_temp_min_abs= r2_score(pre_temp_min_abs['temp_min_abs'], pre_temp_min_abs['temp_min_abs_imputed'])
msq_temp_min_abs= mean_squared_error(pre_temp_min_abs['temp_min_abs'], pre_temp_min_abs['temp_min_abs_imputed'])

seasons_14= imputer_temp_min_abs.predict(seasons_13.loc[seasons_13['temp_min_abs'].isnull(),:])
del seasons_14["temp_min_abs"]
seasons_14=seasons_14.rename(columns={'temp_min_abs_imputed':'temp_min_abs'}).append(seasons_13.loc[~seasons['temp_min_abs'].isnull(),:])


#wind_avg----------------------------------------------------------------------------------------

df_train, df_test = random_split(seasons_14, split_ratios=[0.8, 0.2])

#Initialize a SimpleImputer model
imputer_wind_avg = SimpleImputer(
input_columns=['hum','wind_max', 'rain', 'freez','sun','temp_avg', 'wind_max_avg'],
output_column='wind_avg',
output_path = 'imputer_model'
)

#Fit an imputer model on the train data
imputer_wind_avg.fit(train_df=df_train)
predictions_wind_avg= imputer_wind_avg.predict(df_test)

pre_wind_avg=predictions_wind_avg.loc[~predictions_wind_avg['wind_avg'].isnull(),['wind_avg','wind_avg_imputed'] ]

#Calculate R2 & MSE
r2_wind_avg= r2_score(pre_wind_avg['wind_avg'], pre_wind_avg['wind_avg_imputed'])
msq_wind_avg= mean_squared_error(pre_wind_avg['wind_avg'], pre_wind_avg['wind_avg_imputed'])

seasons_15= imputer_wind_avg.predict(seasons_14.loc[seasons_14['wind_avg'].isnull(),:])
del seasons_15["wind_avg"]
seasons_15=seasons_15.rename(columns={'wind_avg_imputed':'wind_avg'}).append(seasons_14.loc[~seasons['wind_avg'].isnull(),:])


#wind_max----------------------------------------------------------------------------------------

df_train, df_test = random_split(seasons_15, split_ratios=[0.8, 0.2])

#Initialize a SimpleImputer model
imputer_wind_max = SimpleImputer(
input_columns=['hum','wind_avg', 'rain', 'freez','sun','temp_avg', 'wind_max_avg'],
output_column='wind_max',
output_path = 'imputer_model'
)

#Fit an imputer model on the train data
imputer_wind_max.fit(train_df=df_train)
predictions_wind_max= imputer_wind_max.predict(df_test)

pre_wind_max=predictions_wind_max.loc[~predictions_wind_max['wind_max'].isnull(),['wind_max','wind_max_imputed'] ]

#Calculate R2 & MSE
r2_wind_max= r2_score(pre_wind_max['wind_max'], pre_wind_max['wind_max_imputed'])
msq_wind_max= mean_squared_error(pre_wind_max['wind_max'], pre_wind_max['wind_max_imputed'])

seasons_16= imputer_wind_max.predict(seasons_15.loc[seasons_15['wind_max'].isnull(),:])
del seasons_16["wind_max"]
seasons_16=seasons_16.rename(columns={'wind_max_imputed':'wind_max'}).append(seasons_15.loc[~seasons['wind_max'].isnull(),:])



#wind_max_avg----------------------------------------------------------------------------------------

df_train, df_test = random_split(seasons_16, split_ratios=[0.8, 0.2])

#Initialize a SimpleImputer model
imputer_wind_max_avg = SimpleImputer(
input_columns=['hum','wind_max', 'rain', 'freez','sun','temp_avg', 'wind_max_avg'],
output_column='wind_max_avg',
output_path = 'imputer_model'
)

#Fit an imputer model on the train data
imputer_wind_max_avg.fit(train_df=df_train)
predictions_wind_max_avg= imputer_wind_max_avg.predict(df_test)

pre_wind_max_avg=predictions_wind_max_avg.loc[~predictions_wind_max_avg['wind_max_avg'].isnull(),['wind_max_avg','wind_max_avg_imputed'] ]

#Calculate R2 & MSE
r2_wind_max_avg= r2_score(pre_wind_max_avg['wind_max_avg'], pre_wind_max_avg['wind_max_avg_imputed'])
msq_wind_max_avg= mean_squared_error(pre_wind_max_avg['wind_max_avg'], pre_wind_max_avg['wind_max_avg_imputed'])

seasons_17= imputer_wind_max_avg.predict(seasons_16.loc[seasons_16['wind_max_avg'].isnull(),:])
del seasons_17["wind_max_avg"]
seasons_17=seasons_17.rename(columns={'wind_max_avg_imputed':'wind_max_avg'}).append(seasons_16.loc[~seasons['wind_max_avg'].isnull(),:])


#sun----------------------------------------------------------------------------------------

df_train, df_test = random_split(seasons_17, split_ratios=[0.8, 0.2])

#Initialize a SimpleImputer model
imputer_sun= SimpleImputer(
input_columns=['hum','wind_avg', 'rain', 'freez','sun','temp_avg'],
output_column='sun',
output_path = 'imputer_model'
)

#Fit an imputer model on the train data
imputer_sun.fit(train_df=df_train)
predictions_sun= imputer_sun.predict(df_test)

pre_sun=predictions_sun.loc[~predictions_sun['sun'].isnull(),['sun','sun_imputed'] ]

#Calculate R2 & MSE
r2_sun= r2_score(pre_sun['sun'], pre_sun['sun_imputed'])
msq_sun= mean_squared_error(pre_sun['sun'], pre_sun['sun_imputed'])

seasons_18= imputer_sun.predict(seasons_17.loc[seasons_17['sun'].isnull(),:])
del seasons_18["sun"]
seasons_18=seasons_18.rename(columns={'sun_imputed':'sun'}).append(seasons_17.loc[~seasons['sun'].isnull(),:])



#Save  Dataframe


seasons_18.to_csv('D:/Bootcamp/Data/seasons_inpute.csv')


