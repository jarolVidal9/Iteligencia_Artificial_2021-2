def hechos():
    #hechos en donde se almacena tanto sintomas como enfermedades
    v=[]
    fichero = open('hechos.txt','r')
    for linea in fichero:
        v.append(str.strip(linea))
    fichero.close()
    return v

def reglas():
    #reglas para relacionar los sintomas con las enfermedades
    v=[]
    fichero = open('reglas.txt','r')
    for linea in fichero:
        v.append((str.strip(linea)).split(','))
    for x in range(len(v)):
        for j in range(len(v[x])):
            v[x][j]=float(v[x][j])
    fichero.close()
    return(v)

def diagnostico(agenda,enfermedades):
    #funcion para buscar la enfermedad con mas puntos o resultado inconcluso
    mayor=0
    enfermedad=-1
    contador=0
    for posicion_agenda in agenda:
        if posicion_agenda[1]==mayor:
            contador=contador+1
        elif posicion_agenda[1]>mayor:
            contador=0
            mayor=posicion_agenda[1]
            enfermedad=posicion_agenda[0]  
    if contador>=1:
        return "Resultado inconcluso"
    return enfermedades[int(enfermedad)]
def inferencia(sintomas):
    #agenda donde se almacenaran los resultados de los sintomas
    agenda=[]
    #reglas que relacionan sintomas con enfermedades
    regla=reglas()
    lista_hechos=hechos()
    for sintoma in sintomas:
        for posicion_sintomas in range(len(lista_hechos)):
                    #valida si el sintoma exister
                    if sintoma==lista_hechos[posicion_sintomas]:
                        #busca en las reglas a que enfermedad pertenece el sintoma
                        for z in regla:
                            if posicion_sintomas==z[0]:
                                contador=0
                                #le suma una unidad a la agenda si la enfermedad ya estaba add
                                for posicion_agenda in agenda:
                                    if posicion_agenda[0]==z[1]:
                                        posicion_agenda[1]=posicion_agenda[1]+(1-posicion_agenda[1])*z[2]
                                    else:
                                        contador=contador+1
                                #agrega la enfermedad a la agenda si no existe
                                if contador==len(agenda):
                                    fila=[]
                                    fila.append(z[1])
                                    fila.append(z[2])
                                    agenda.append(fila)
    for x in agenda:
        print(x)
    resultado=diagnostico(agenda,lista_hechos)
    return resultado
        
def inicio():
    print("hola soy tu asistente medico de autodiagnostico para continuar presiona enter")
    input()
    print("Para terminar la ejecucion escriba 'nada' cuando se le pregunta el sintoma")
    #sintomas almacenados en los hechos
    interador=0
    sintomas=[]
    while interador==0:
        pregun_sinto=input("Ingrese por favor un sintoma:").strip()
        if pregun_sinto=="nada":
            interador=1
        else:
            sintomas.append(pregun_sinto)
    print("Su diagnostico es que usted tiene:"+inferencia(sintomas))
                             

inicio()