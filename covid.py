#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 11:50:48 2021

@author: ivandavid
"""
import pandas as pd

url = "covid_22_noviembre.csv"
data = pd.read_csv(url)


# 1. Numero de casos de contagiados en el pais
n_contagios = data.shape[0]
print(f'\nCasos de Covid-19 en Colombia: {n_contagios}')


# 2. Número de Municipios Afectados
data['Nombre municipio'].replace('puerto COLOMBIA', 'PUERTO COLOMBIA', inplace=True)
data['Nombre municipio'].replace('puerto colombia', 'PUERTO COLOMBIA', inplace=True)
data['Nombre municipio'].replace('barrancabermeja', 'BARRANCABERMEJA', inplace=True)
data['Nombre municipio'].replace('momil', 'MOMIL', inplace=True)
data['Nombre municipio'].replace('MEDELLiN', 'MEDELLIN', inplace=True)
data['Nombre municipio'].replace('Galapa', 'GALAPA', inplace=True)
data['Nombre municipio'].replace('Guepsa', 'GUEPSA', inplace=True)
data['Nombre municipio'].replace('Pensilvania', 'PENSILVANIA', inplace=True)
data['Nombre municipio'].replace('Anserma', 'ANSERMA', inplace=True)

n_municipios = len(data.groupby('Nombre municipio').size())
print(f'\nNumero de municipios afectados: {n_municipios}')


# 3. Liste los municipios afectados (sin repetirlos)
n_muni_afec = data.groupby(
    'Nombre municipio').size().sort_values(ascending=False)
print(f'\nMunicipios afectados: {n_muni_afec}')
