# -*- coding: utf-8 -*-
"""
Created on Thu May 27 23:12:47 2021

@author: pgeir
"""

# UTM to WSG84 Decidata Converter

## Using Geopandas

import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

pd.read_csv("../Input_open_data/ds02_datos-nidos-avispa-asiatica.csv")
