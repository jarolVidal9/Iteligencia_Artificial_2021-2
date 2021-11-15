class grafo:
	def __init__(self,idG,pes,hij):
		self.id_grafo=idG
		#self.nombre=nom
		self.pesos=pes
		self.hijos=hij
		self.visita=1
	def setId(self,id):
		self.id_grafo=id
	'''def setNombre(self,nombre):
		self.nombre=nombre'''
	def setPesos(self,vector):
		self.pesos=vector
	def setHijos(self,vector):
		self.hijos=vector
	def setVisita(self,dato):
		self.visita=dato
	def getId(self):
		return self.id_grafo
	'''def getNombre(self):
		return self.nombre'''
	def getPesos(self):
		return self.pesos
	def getHijos(self):
		return self.hijos
	def getVisita(self):
		return self.visita
def grafosprueba():
	m=grafo("m",None,None)
	l=grafo("l",None,None)
	k=grafo("k",None,None)
	l=grafo("l",None,None)
	j=grafo("j",None,None)
	i=grafo("i",None,None)
	h=grafo("h",None,None)
	g=grafo("g",None,None)
	f=grafo("f",None,None)
	e=grafo("e",[3,2,7],[k,l,m])
	d=grafo("d",[4],[j])
	c=grafo("c",[2,6],[h,i])
	b=grafo("b",[1,2],[f,g])
	a=grafo("a",[1,9,5,6],[b,c,d,e])
	return a
def busquedaCamino(grafoInicial):
	if grafoInicial==None:
		return 0
	else:
		if grafoInicial.getHijos()!=None:
			for x in grafoInicial.getHijos():
				if x.getVisita():

grafosprueba()
#print(Estadoinicial.getPesos())
