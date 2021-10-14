import manejoArchivos
#agrega los elementos a los archivos para entrenar el sistemas
def agregarElemento():
	nuevoElememto=[]
	print("Si desea agregar nuevos atributos a una entidad solo ingrese de nuevo el nombre de la entidad acontinuacion")
	entidad=input("Dime en que piensas:")
	nuevoElememto.append(entidad)
	print("Si desea dejar de ingresar caracteristicas escriba 'parar'")
	iterador=0
	while iterador==0:
		atributo=input("Que lo caracteriza?:")
		if(atributo=="parar"):
			iterador=1
		else:
			nuevoElememto.append(atributo)
	manejoArchivos.escribirArchivo(nuevoElememto)
#Eliminar la rama por contestar no
def eliminar(reglas,x,atributos):
	Coincidencias=[]
	for y in reglas[:]:
		if y[1]==x[1]:
			Coincidencias.append(y)
			reglas.remove(y)
	for i in Coincidencias:
		for z in reglas[:]:
			if (i[0]==z[0]):
				reglas.remove(z)
#elimina las demas ramas al contestar si
def eliminar2(reglas,x,atributos):
	Coincidencias=[]
	for y in reglas[:]:
		if y[1]==x[1]:
			Coincidencias.append(y)
	reglas2=[]
	for i in Coincidencias:
		for z in reglas:
			if i[0]==z[0]:
				reglas2.append(z)
	for x in reglas[:]:
		reglas.remove(x)
	for z in reglas2:
		reglas.append(z)
#valido que solo quede una entidad
def validacion(reglas):
	i=0
	posicion=reglas[0][0]
	for x in reglas:
		if x[0]==posicion:
			i=i+1
	if len(reglas)==i:
		return 1
	else:
		return 0
#se eliminan los atributos que ya no se deben preguntar 
def validacionAtributos(atributos,reglas):
	for i in range(len(atributos)):
		contador=0
		if atributos[i]!="0":
			for j in reglas:
				if j[1]==i:
					contador=1
					break
			if contador==0:
				atributos[i]="0"
#entidad principal donde se realizan las preguntas
def jugar():
	atributos=manejoArchivos.leerAtributos()
	reglas=manejoArchivos.leerReglas()
	entidad=manejoArchivos.leerEntidades()
	print("Por favor conteste 'SI' o 'NO' unicamente")
	print("Si desea detener las preguntas escriba 'parar'")
	for j in reglas[:]:
		if atributos[j[1]]=="0":
			continue
		else:
			respuesta=input("Estas pensando en "+atributos[j[1]]+" ?")
			if respuesta.strip().lower()=="si":
				aux=j
				atributos[j[1]]="0"
				eliminar2(reglas,aux,atributos)
			elif respuesta.strip().lower()=="no":
				aux2=j
				atributos[j[1]]="0"
				eliminar(reglas,aux2,atributos)
			elif respuesta.strip().lower()=="parar":
				break
			if validacion(reglas)==1:
					print("En lo que usted esta pensando es:"+entidad[reglas[0][0]])
					break
			if len(reglas)==0:
				print("No se cuenta con el suficiente conocimiento para adivinar.")
				break
		validacionAtributos(atributos,reglas)
#menu donde se elige si agregar mas entidades o jugar
def menu():
	print("Este es un sistema experto que se dedica al aprendizaje y 'adivinacion'")
	print("\n")
	i=0
	while i==0:
		print("\tMenu:")
		print("Ingrese '1' para educar a el sistema experto")
		if manejoArchivos.tamreglas()>0:
			print("Ingrese '2' para jugar a el sistema experto")
		print("Ingrese '3' para salir")
		opcion=input()
		if opcion=="1":
			agregarElemento()
		elif opcion=="2":
			jugar()
		elif opcion=="3":
			print("Gracias por utilizar nuestro programa")
			break
menu()
