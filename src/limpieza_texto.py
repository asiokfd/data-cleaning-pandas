import seaborn as sb
import pandas as pd
import numpy as np
import src

data = pd.read_csv("src/attacks.csv",encoding = "ISO-8859-1")

# primero limpio las filas con todos los valores nulos
data.dropna (how= "all", inplace=True)

#para la primera hipótesis filtro por provocados y sexo inicialmente, luego incluyo el nombre para saber el que tenia valor N
# y poder depurarlo
dfhipo1 = data [[ "Type", "Sex ", "Name" ]]
dfhipo1a = dfhipo1 [dfhipo1.Type == "Provoked" ]
dfhipo1a [dfhipo1a [ "Sex "].isin ([ "N" ])]
dfhipo1a [ "Sex "].replace ({"N" : "M"}, inplace=True )

#para la segunda hipótesis filtro por provocados y actividad, después depuro las actividades a las que incluyan "surf" o "fish" y luego
# las reduzco con una función para normalizarlas a solo 2 valores: Surfing y Fishing, soy consciente que de que me he comido al menos un valor
# que estaba pescando mientras surfeaba.
dfhipo2 = data [["Type", "Activity" ]]
dfhipo2a = dfhipo2 [ dfhipo2.Type == "Provoked" ]
dfhipo2a.fillna ( "nada" )
dfhipo2b = dfhipo2a [ dfhipo2a.Activity.str.contains ('surf|fish', case=False, na=False )]
dfhipo2b ["Activity"] = dfhipo2b ["Activity"].apply (reduciendo)

#para la tercera hipótesis filtro por area, country y location porque en un principio no sé donde estarán los valores, después de verlo, 
# voy reduciendo
data2 = data [[ "Country" , "Area" , "Location" ]]
data2.dropna ( how = "all" , inplace = True )
data2a = data2.drop ([ "Location"] , axis=1 )
data2a = data2a.loc [(data2a ["Area"] == "Florida") | (data2a["Country"] == "Seychelles" )]#aquí cambio la hipótesis a Hawaii
data2h = data2.loc [(data2 ["Area"] == "Florida") | (data2["Area"] == "Hawaii" )]
