def hechos(decision):
    sintomas=["fiebre","malestar","tos","dolor garganta"]
    enfermedades=["gripa","faringitis"]
    if decision==1:
        return sintomas
    if decision==0:
        return enfermedades

def reglas():
    regla=[[0,0],[1,0],[2,0],[1,1],[3,1]]
    return regla

def diagnostico(agenda,enfermedades):
    mayor=0
    enfermedad=-1
    for posicion_agenda in agenda:
        if posicion_agenda[1]>mayor:
            mayor=posicion_agenda[1]
            enfermedad=posicion_agenda[0]
    return enfermedades[enfermedad]

        
def inicio():
    print("hola soy tu asistente medico de autodiagnostico para continuar presiona enter")
    input()
    sintomas=hechos(1)
    regla=reglas()
    agenda=[]
    
    for iterador in range(3):
        pregun_sinto=input("Ingrese por favor un sintoma:")
        for posicion_sintomas in range(len(sintomas)):
            if pregun_sinto==sintomas[posicion_sintomas]:
                print(posicion_sintomas)
                print(sintomas[posicion_sintomas])
                for z in regla:
                    if posicion_sintomas==z[0]:
                        print("encontre sintoma")
                        contador=0
                        for posicion_agenda in agenda:
                            print(z[1])
                            if posicion_agenda[0]==z[1]:
                                print("sumo")
                                posicion_agenda[1]=posicion_agenda[1]+1
                            else:
                                contador=contador+1

                        if contador==len(agenda):
                            print("agrego")
                            fila=[]
                            fila.append(z[1])
                            fila.append(1)
                            agenda.append(fila)
    print("Su diagnostico es que usted tiene:"+diagnostico(agenda,hechos(0)))
    for x in agenda:
        print(x)
                            
                    

            

inicio()