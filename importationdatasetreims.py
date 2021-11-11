# -*- coding: utf-8 -*-
"""ImportationDatasetReims.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1T4pGsQUpAFfokGOZP6zSh2vIBAz9nq3K
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset_1 = pd.concat([pd.read_csv('https://static.data.gouv.fr/resources/demandes-de-valeurs-foncieres/20211020-111113/valeursfoncieres-2020.txt', sep = '|'),pd.read_csv('https://static.data.gouv.fr/resources/demandes-de-valeurs-foncieres/20211020-110806/valeursfoncieres-2019.txt', sep = '|')
  ,pd.read_csv('https://static.data.gouv.fr/resources/demandes-de-valeurs-foncieres/20211020-110525/valeursfoncieres-2018.txt', sep = '|')])

dataReims_1 = dataset_1[dataset_1["Commune"]=="REIMS"]

del dataset_1

dataset_2 = pd.read_csv('https://static.data.gouv.fr/resources/demandes-de-valeurs-foncieres/20211020-110129/valeursfoncieres-2017.txt', sep = '|')
dataReims_2 = dataset_2[dataset_2["Commune"]=="REIMS"]
del dataset_2
dataReims = pd.concat([dataReims_1,dataReims_2])

dataReims.shape

datasetReims = dataReims.drop(["Identifiant local","Prefixe de section","Code service CH", "Reference document","1 Articles CGI", "2 Articles CGI",
   "3 Articles CGI", "4 Articles CGI", "5 Articles CGI", "No disposition", "B/T/Q", "No Volume", "1er lot", "Surface Carrez du 1er lot", "2eme lot", "Surface Carrez du 2eme lot", "3eme lot", "Surface Carrez du 3eme lot", "4eme lot", "Surface Carrez du 4eme lot", "5eme lot", "Surface Carrez du 5eme lot", "Nature culture","Nature culture speciale", "Surface terrain"], axis=1)

del dataReims

datasetReims.isnull().sum()

datasetReims_appartement = datasetReims[datasetReims["Type local"]=="Appartement"]

del datasetReims_appartement["Type local"]

#Telechargement du dataset des appartements de Reims 2017, 2018, 2019, 2020
from google.colab import files

datasetReims_appartement.to_csv('datasetReimsAppartements.csv')
files.download('datasetReimsAppartements.csv')