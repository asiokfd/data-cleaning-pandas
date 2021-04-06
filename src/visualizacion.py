from PIL import Image

print ("En este documento explicaremos el proceso de investigación realizado, e incluiremos algunas imagenes")
print ("Lo primero que hemos hecho es la realización de hipótesis, en este caso:\n 1ª hipotesis :Los hombres provocan mas ataques las mujeres")
print (" 2ª Los surfistas provocan más ataques que los pescadores")
print (" 3ª Hay más ataques en Florida que en Reunión ( posteriormente cambiada a Seychelles y finalmente a Hawaii por falta de datos)")

print ("\nPara ello primero hemos limpiado todas las filas que contenian todos los valores nulos y posteriormente hemos filtrado para cada hipótesis: ")
print("\nPara la primera hipótesis, como vemos en la imagen:")

Image.open ("../images/imagengenerosucia.jpg") #con las barras así me funciona en windows, pero no tengo claro que funcione en mac o linux

print("\n Parece que nos sobran datos, asi que los pulimos un poco para que nos quede:")

Image.open ("../images/imagengenero.jpg")

print ("\n Algo parecido nos ocurre con la segunda hipótesis, comparar quien provoca más ataques, si los surfistas o los pescadores \n pero en este caso el proceso de depurado fue más complejo al contener strings")
print ("En cualquier caso, inicialmente teníamos estos datos")

Image.open ("../images/imagenactividadsucia.jpg")

print ("Intratable... \n Y finalmente")

Image.open ("../images/imagenactividad.jpg")

print ("\ algo mas visible, y falsamos la hipótesis, parece que son los pescadores los mas provocadores")


print ("\n En el 3º caso, comprobar que en Florida atacan más que en Hawai, me he encontrado con la columna mas limpia, hasta las mayúsculas bien puestas, \n asi que solo hubo que depurar un poco")

print ("\inicialmente:")

Image.open ("../images/imagenzonassucia.jpg")

print("\n y finalmente...")

Image.open ("../images/imagenzonas.jpg")

print("\n efectivamente, en Florida atacan más, o al menos, hay más registros")

print (color.BOLD + "CONCLUSIONES PERSONALES" + color.END)

print ("Por un lado satisfecho de haber realizado el primero proyecto pasando por todos los checkpoints, pero un poco decepcionado con las hipótesis que he hecho\ y los gráficos que me han quedado, a mi parecer simples porque se reducen a 'quien más', no lo pensé cuando las plantee \n también es verdad que en el sample me dío miedo meterme con las fechas, pero limpiarlas hubiera sido clave para poder ver\n mejores plots ")
