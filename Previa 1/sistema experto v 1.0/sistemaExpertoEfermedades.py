def hechos(decision):
    #hechos en donde se almacena tanto sintomas como enfermedades
    sintomas=["fiebre","malestar","tos","dolor garganta","diarrea"]
    enfermedades=["gripa","faringitis","parasitos"]
    if decision==1:
        return sintomas
    if decision==0:
        return enfermedades

def reglas():
    #reglas para relacionar los sintomas con las enfermedades
    regla=[[0,0],[1,0],[2,0],[1,1],[3,1],[4,2],[1,2]]
    return regla

def diagnostico(agenda,enfermedades):
    #funcion para buscar la enfermedad con mas puntos o resultado inconcluso
    mayor=0
    enfermedad=-1
    for posicion_agenda in agenda:
        if posicion_agenda[1]==mayor:
            return "inconcluso"
        if posicion_agenda[1]>mayor:
            mayor=posicion_agenda[1]
            enfermedad=posicion_agenda[0]
    return enfermedades[enfermedad]

        
def inicio():
    print("hola soy tu asistente medico de autodiagnostico para continuar presiona enter")
    input()
    print("Para terminar la ejecucion escriba 'nada' cuando se le pregunta el sintoma")
    #sintomas almacenados en los hechos
    sintomas=hechos(1)
    #reglas que relacionan sintomas con enfermedades
    regla=reglas()
    #agenda donde se almacenaran los resultados de los sintomas
    agenda=[]
    interador=0
    while interador==0:
        pregun_sinto=input("Ingrese por favor un sintoma:")
        if pregun_sinto=="nada":
            interador=1
        else:
            #ciclo para buscar el sintoma en los hechos
            for posicion_sintomas in range(len(sintomas)):
                #valida si el sintoma exister
                if pregun_sinto==sintomas[posicion_sintomas]:
                    #busca en las reglas a que enfermedad pertenece el sintoma
                    for z in regla:
                        if posicion_sintomas==z[0]:
                            contador=0
                            #le suma una unidad a la agenda si la enfermedad ya estaba add
                            for posicion_agenda in agenda:
                                if posicion_agenda[0]==z[1]:
                                    posicion_agenda[1]=posicion_agenda[1]+1
                                else:
                                    contador=contador+1
                            #agrega la enfermedad a la agenda si no existe
                            if contador==len(agenda):
                                fila=[]
                                fila.append(z[1])
                                fila.append(1)
                                agenda.append(fila)
    print("Su diagnostico es que usted tiene:"+diagnostico(agenda,hechos(0)))
    for x in agenda:
        print(x)
                            
                    

inicio()