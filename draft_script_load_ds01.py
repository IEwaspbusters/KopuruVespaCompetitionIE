# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 01:21:10 2021

@author: a.berrizbeitia@student.ie.edu
"""

import pandas as pd
import requests
import io

## 'uncomment' your username below:
username = 'narrativus'

## 'uncomment' your github personal access token below:
token = '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'

# Creates a re-usable session object with your creds in-built
github_session = requests.Session()
github_session.auth = (username, token)
    
# Downloading the csv file from your GitHub
ds01 = "https://raw.githubusercontent.com/IEwaspbusters/KopuruVespaCompetitionIE/main/Input_open_data/ds01_PLANTILLA-RETO-AVISPAS-KOPURU.csv?token=ADAWFG4CKOYHU2ONTL6WYZTAOODGY"
download01 = github_session.get(ds01).content

# Reading the downloaded content and making it a pandas dataframe
df01 = pd.read_csv(io.StringIO(download01.decode('utf-8')), sep=";")
df01.head()
