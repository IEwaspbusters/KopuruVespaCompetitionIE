# -*- coding: utf-8 -*-
"""
Created on Sun May  9 23:21:50 2021

@author: Usuario
"""
import pandas as pd

imp_season= pd.read_csv('D:/Bootcamp/Kopuru/seasons_impute.csv')

imp_season.columns


#2017
imp_season_anual_17= imp_season.loc[imp_season.year==2017,['codigo', 'freez', 'hum','lev_max', 'lev_mid', 'lev_min', 'rain',
                                'rain_1mm', 'rain_cum', 'rain_max_10', 'rain_max_day', 'sun',
                                'temp_avg', 'temp_max_abs', 'temp_max_avg', 'temp_min_abs', 'wind_avg','wind_max', 'wind_max_avg','year']]

imp_season_anual_17=imp_season_anual_17.groupby(['codigo','year'],as_index=True ).agg({'freez':'mean', 
                         'hum':'mean', 
                         'lev_max':'max', 
                         'lev_mid':'mean',
                         'lev_min':'min', 
                         'rain':'mean', 
                         'rain_1mm':'mean',
                         'rain_cum':'mean', 
                         'rain_max_10':'max', 
                         'rain_max_day':'max',                         
                         'sun':'mean',
                         'temp_avg':'mean',
                         'temp_max_abs':'max',
                         'temp_max_avg':'max', 
                         'temp_min_abs':'min', 
                         'rain_max_day':'max',                         
                         'wind_avg':'mean',
                         'wind_max':'max',                                            
                         'wind_max_avg':'max'}).reset_index()



#2018
imp_season_anual_18= imp_season.loc[imp_season.year==2018,['codigo', 'freez', 'hum','lev_max', 'lev_mid', 'lev_min', 'rain',
                                'rain_1mm', 'rain_cum', 'rain_max_10', 'rain_max_day', 'sun',
                                'temp_avg', 'temp_max_abs', 'temp_max_avg', 'temp_min_abs', 'wind_avg','wind_max', 'wind_max_avg','year']]

imp_season_anual_18=imp_season_anual_18.groupby(['codigo','year'],as_index=True ).agg({'freez':'mean', 
                         'hum':'mean', 
                         'lev_max':'max', 
                         'lev_mid':'mean',
                         'lev_min':'min', 
                         'rain':'mean', 
                         'rain_1mm':'mean',
                         'rain_cum':'mean', 
                         'rain_max_10':'max', 
                         'rain_max_day':'max',                         
                         'sun':'mean',
                         'temp_avg':'mean',
                         'temp_max_abs':'max',
                         'temp_max_avg':'max', 
                         'temp_min_abs':'min', 
                         'rain_max_day':'max',                         
                         'wind_avg':'mean',
                         'wind_max':'max',                                            
                         'wind_max_avg':'max'}).reset_index()

#2019
imp_season_anual_19= imp_season.loc[imp_season.year==2019,['codigo', 'freez', 'hum','lev_max', 'lev_mid', 'lev_min', 'rain',
                                'rain_1mm', 'rain_cum', 'rain_max_10', 'rain_max_day', 'sun',
                                'temp_avg', 'temp_max_abs', 'temp_max_avg', 'temp_min_abs', 'wind_avg','wind_max', 'wind_max_avg','year']]

imp_season_anual_19=imp_season_anual_19.groupby(['codigo','year'],as_index=True ).agg({'freez':'mean', 
                         'hum':'mean', 
                         'lev_max':'max', 
                         'lev_mid':'mean',
                         'lev_min':'min', 
                         'rain':'mean', 
                         'rain_1mm':'mean',
                         'rain_cum':'mean', 
                         'rain_max_10':'max', 
                         'rain_max_day':'max',                         
                         'sun':'mean',
                         'temp_avg':'mean',
                         'temp_max_abs':'max',
                         'temp_max_avg':'max', 
                         'temp_min_abs':'min', 
                         'rain_max_day':'max',                         
                         'wind_avg':'mean',
                         'wind_max':'max',                                            
                         'wind_max_avg':'max'}).reset_index()

imp_season_anual= imp_season_anual_17.append(imp_season_anual_18).append(imp_season_anual_19)


imp_season_anual.to_csv('D:/Bootcamp/Kopuru/seasons_anual.csv',index=False )
