![portada](https://github.com/Ironhack-Data-Madrid-Enero-2021/w2-pandas-project/blob/master/images/portada.jpg)

# PROYECTO DE LIMPIEZA DE UN PANDAS DATAFRAME

En este proyecto lo que vamos a encontrar es una **puesta en práctica de algunas de las técnicas de limpieza de un Pandas Data Frame** más comunes, para ello elaboraremos unas sencillas hipótesis que mediante la limpieza del dataset intentaremos validar para después añadir una breve visualización de ellas. La técnica utilizada será la de reducir al máximo el set para cada caso, dejando unicamente lo necesario para las hipótesis

## Archivos incluidos:

1- Un Jupyter Notebook llamado "limpieza.ypnb" en el que se encuentra todo el proceso en sucio
2- Este README 
3- Una carpeta llamada "src" con:
    3a- Un archivo de Python llamado "src.py" donde estarán las funciones utilizadas
    3b-Un archivo de Python llamado "limpieza_texto.py" donde sólo encontraremos la aplicacion de los métodos de limpieza 
    3d- Un archivo de python llamado "visualizacion.py" donde incluiremos la visualizacion y un análisis de las hipótesis
4- Una carpeta llamada "images" con las imagenes necesarias para la visualización



## Métodos utilizados:

1. Veremos el uso de **dropna** y **fillna** para gestionar los valores nulos
2. Reduciremos las columnas con el método **drop** o sencillamente nos quedaremos con las que nos interesen
3. Y dentro de ellas, nos quedaremos solo con los valores que nos interesen
4. Aplicaremos el **replace** también para sustituir algún valor mal escrito
5. Mediante el uso de **str.contains** filtraremos strings
6. Y también utilizaremos el método **apply** con funcion propia para modificar columnas

## Bibliotecas:

Para todo esto, hemos utilizado las bibliotecas:
**pandas, numpy, PIL y seaborn**

## Links utilizados
https://pandas.pydata.org/docs/
https://seaborn.pydata.org/
https://numpy.org/doc/
todas las clases de esta última semana
https://www.analyticslane.com/2020/01/13/filtrado-de-cadenas-de-texto-en-dataframe-con-pandas/
https://es.stackoverflow.com/
https://www.delftstack.com/es/
