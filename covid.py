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


# 4. Número de personas que se encuentran en atención en casa
data['Ubicación del caso'].replace('Casa', 'CASA', inplace=True)
data['Ubicación del caso'].replace('casa', 'CASA', inplace=True)

atencion_casa = len(data[data['Ubicación del caso'] == 'CASA'])
print(f'\nNúmero de personas que se encuentran en atención en casa: {atencion_casa}')


# 5. Número de personas que se encuentran recuperados
n_recuperados = data[data['Recuperado'] == 'Recuperado'].shape[0]
print(f'\nNumero de personas recuperadas {n_recuperados}')


# 6. Número de personas que ha fallecido
n_fallecidos = data[data['Estado'] == 'Fallecido'].shape[0]
print(f'\nNumero de personas fallecidas en Colombia: {n_fallecidos}')


# 7. Ordenar de Mayor a menor por tipo de caso
n_import = data.groupby(
    'Tipo de contagio').size().sort_values(ascending=False)
print(f'\n{n_import}')


# 8. Número de departamentos afectados
data['Nombre departamento'].replace('Caldas', 'CALDAS', inplace=True)
data['Nombre departamento'].replace('Tolima', 'TOLIMA', inplace=True)

n_depar = len(data.groupby('Nombre departamento').size())
print(f'\nNumero de departamentos afectados: {n_depar}')


# 9. Liste los departamentos afectados(sin repetirlos)
data.groupby('Nombre departamento').size()


# 10. Ordene de mayor a menor por tipo de atención
n_tipo_atencion = data.groupby(
    'Ubicación del caso').size().sort_values(ascending=False)
print(f'\n{n_tipo_atencion}')


# 11. Liste de mayor a menor los 10 departamentos con mas casos decontagiados
data['Nombre departamento'].replace('BARRANQUILLA', 'ATLANTICO', inplace=True)
data['Nombre departamento'].replace('CARTAGENA', 'BOLIVAR', inplace=True)

depar = data['Nombre departamento'].value_counts().head(10)
print(f'\n{depar}')


# 12. Liste de mayor a menor los 10 departamentos con mas casos de fallecidos
depar_falle = data[data['Estado'] == 'Fallecido'].groupby(
    'Nombre departamento').size().sort_values(ascending=False).head(10)
print(f'\n{depar_falle}')


# 13. Liste de mayor a menor los 10 departamentos con mas casos de recuperados
depar_recup = data[data['Recuperado'] == 'Recuperado'].groupby(
    'Nombre departamento').size().sort_values(ascending=False).head(10)
print(f'\n{depar_recup}')


# 14. Liste de mayor a menor los 10 municipios con mas casos de contagiados
municipio = data['Nombre municipio'].value_counts().head(10)
print(f'\n{municipio}')


# 15. Liste de mayor a menor los 10 municipios con mas casos de fallecidos
muni_falle = data[data['Estado'] == 'Fallecido'].groupby(
    'Nombre municipio').size().sort_values(ascending=False).head(10)
print(f'\n{muni_falle}')


# 16. Liste de mayor a menor los 10 municipios con mas casos de recuperados
muni_recup = data[data['Recuperado'] == 'Recuperado'].groupby(
    'Nombre municipio').size().sort_values(ascending=False).head(10)
print(f'\n{muni_recup}')


# 17. Liste agrupado por departamento y en orden de Mayor a menor las ciudades con mas casos de contagiados
data.groupby(['Nombre departamento', 'Nombre municipio']
             ).size().sort_values(ascending=False).head(10)


# 18. Número de Mujeres y hombres contagiados por ciudad por departamento
n_m_h = data.groupby(['Nombre departamento', 'Nombre municipio',
                     'Sexo']).size().sort_values(ascending=False)
print(f'\n{n_m_h}')


# 19. Liste el promedio de edad de contagiados por hombre y mujeres por ciudad por departamento
prom_edad = data.groupby(
    ['Nombre departamento', 'Nombre municipio', 'Sexo']).Edad.mean()
print(f'\n{prom_edad}')


# 20. Liste de mayor a menor el número de contagiados por país de procedencia
data['Nombre del país'].replace('VENEUELA', 'VENEZUELA', inplace=True)
data['Nombre del país'].replace('MEXICO', 'MÉXICO', inplace=True)

pais = data['Nombre del país'].value_counts()
print(f'\n{pais}')


# 21. Liste de mayor a menor las fechas donde se presentaron mas contagios
fech_contagio = data.groupby(
    ['Fecha de diagnóstico']).size().sort_values(ascending=False)
print(f'\n{fech_contagio}')


# 22. Diga cual es la tasa de mortalidad y recuperación que tiene Colombia
mortalidad = (len(data[data['Estado'] == 'Fallecido']) / len(data)) * 100
recuperacion = (len(data[data['Recuperado'] == 'Recuperado']) / len(data)) * 100
print('\nTasa de mortalidad: ', "{:.2f}".format(mortalidad))
print('\nTasa de recuperacion: ', "{:.2f}".format(recuperacion))
