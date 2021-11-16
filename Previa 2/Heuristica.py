class nodo:
	def __init__(self,idG,pes,hij):
		self.id_nodo=idG
		#self.nombre=nom
		self.pesos=pes
		self.hijos=hij
		self.visita=1
	def setId(self,id):
		self.id_nodo=id
	'''def setNombre(self,nombre):
		self.nombre=nombre'''
	def setPesos(self,vector):
		self.pesos=vector
	def setHijos(self,vector):
		self.hijos=vector
	def setVisita(self,dato):
		self.visita=datos
	def getId(self):
		return self.id_nodo
	'''def getNombre(self):
		return self.nombre'''
	def getPesos(self):
		return self.pesos
	def getHijos(self):
		return self.hijos
	def getVisita(self):
		return self.visita
def nodosprueba():
	m=nodo("m",None,None)
	l=nodo("l",None,None)
	k=nodo("k",None,None)
	l=nodo("l",None,None)
	j=nodo("j",None,None)
	i=nodo("i",None,None)
	h=nodo("h",None,None)
	g=nodo("g",None,None)
	f=nodo("f",None,None)
	e=nodo("e",[3,2,7],[k,l,m])
	d=nodo("d",[4],[j])
	c=nodo("c",[2,6],[h,i])
	b=nodo("b",[1,2],[f,g])
	a=nodo("a",[1,9,5,6],[b,c,d,e])
	return a
def busquedaCamino(nodoInicial):
	if nodoInicial==None:
		return 0
	else:
		if nodoInicial.getHijos()!=None:
			for x in nodoInicial.getHijos():
				if x.getVisita():
					print(x.getId())

nodoInicial=nodosprueba()
busquedaCamino(nodoInicial)
#print(Estadoinicial.getPesos())
