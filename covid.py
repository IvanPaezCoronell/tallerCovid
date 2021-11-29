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
