def busquedaAtributo(elemtoBuscar):
	leer = open('Atributo.txt','r')
	i=0
	flag=0
	for linea in leer:
		if str.strip(linea)==elemtoBuscar:
			flag=1
			break
		i=i+1
	leer.close()
	if flag==1:
		return i
	else:
		return -i
def busquedaEntidad(elemtoBuscar):
	leer = open('Entidad.txt','r')
	i=0
	flag=0
	for linea in leer:
		if str.strip(linea)==elemtoBuscar:
			flag=1
			break
		i=i+1
	leer.close()
	if flag==1:
		return i
	else:
		return -i
def escribirArchivo(vectorElemento):
	#realizo la escritura en las entidades
	posicionEntidad=busquedaEntidad(vectorElemento[0])
	if posicionEntidad<0:
		f = open ('Entidad.txt','a')
		f.write(vectorElemento[0]+"\n")
		f.close()
		posicionEntidad=posicionEntidad*-1
	#busco los atributos en la lista si ya esta guardo su posicion para las reglas si no esta lo agrego y tambien guardo su posicion
	posicionesAtributos=[]
	iteradorAtributos=1
	while iteradorAtributos<len(vectorElemento):
		posicionAtributo=busquedaAtributo(vectorElemento[iteradorAtributos])
		if posicionAtributo<0:
			f = open ('Atributo.txt','a')
			f.write(vectorElemento[iteradorAtributos]+"\n")
			f.close()
			posicionesAtributos.append(posicionAtributo*-1)
		else:
			posicionesAtributos.append(posicionAtributo)
		iteradorAtributos=iteradorAtributos+1
	#realizo la escritura en las reglas
	f = open ('reglas.txt','a')
	for x in range(len(posicionesAtributos)):
		f.write(str(posicionEntidad)+","+str(posicionesAtributos[x])+"\n")
	f.close()
	posicionEntidad=posicionEntidad*-1
def leerAtributos():
	v=[]
	leer = open('Atributo.txt','r')
	for linea in leer:
		v.append(str.strip(linea))
	leer.close()
	return v
def leerEntidades():
	v=[]
	leer = open('Entidad.txt','r')
	for linea in leer:
		v.append(str.strip(linea))
	leer.close()
	return v
def leerReglas():
    fichero = open('reglas.txt','r')
    v=[]
    for linea in fichero:
        v.append((str.strip(linea)).split(','))
    for x in range(len(v)):
        for j in range(len(v[x])):
            v[x][j]=int(v[x][j])
    fichero.close()
    return(v)
def tamreglas():
	fichero = open('reglas.txt','r')
	i=0
	for linea in fichero:
		i=i+1
	fichero.close()
	return i