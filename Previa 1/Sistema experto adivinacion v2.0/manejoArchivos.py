#busca un atributo y me regresa la posicion donde se encuetra
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
#busco la entidad si esta devuelvo su posicion de lo contrario devuelvo la ultima posicion negativa para saber en que posicion se agregara
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
#escribo en el archivo la entidad sus correspondiente atributos y los relaciono escribiendo la correspondiente relacion en el archivo "reglas"
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
#retorno una lista con los atributos 
def leerAtributos():
	v=[]
	leer = open('Atributo.txt','r')
	for linea in leer:
		v.append(str.strip(linea))
	leer.close()
	return v
#retorno una lista con todos las entidades
def leerEntidades():
	v=[]
	leer = open('Entidad.txt','r')
	for linea in leer:
		v.append(str.strip(linea))
	leer.close()
	return v
#retorno una lista con todos las reglas
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
#verifico si es sistema ya se ha entrenado antes
def tamreglas():
	fichero = open('reglas.txt','r')
	i=0
	for linea in fichero:
		i=i+1
	fichero.close()
	return i