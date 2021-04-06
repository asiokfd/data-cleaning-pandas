

def reduciendo (x): 
    ### Esta función comprobará si la columna contiene los strings "surf" o "Surf" y los cambiará por "Surfing", en cualquier otro caso, retornará "Fishing"### 
    for item in x:
        if "surf" in x:
            return "Surfing"
        if "Surf" in x:
            return "Surfing"
        else:
            return "Fishing"

def abrir (imag):#esto lo dejo, pero no lo uso, abre la imagen en el visualizador de imagenes de windows
    ### Esta función abre una imagen en el visor de imagenes dándole el nombre como argumento###
    ruta = ("..\images\" + imag)
    imag = Image.open (ruta)
    return imag.show ()