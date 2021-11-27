from collections import defaultdict
# basado en el codigo https://ichi.pro/es/algoritmo-de-busqueda-busqueda-primero-en-amplitud-con-python-88335038789726
def generarGrafo(aristas):
    ListaAdyacencia = defaultdict(list)
    for u, v in aristas:
        ListaAdyacencia[u].append(v)
        ListaAdyacencia[v].append(u)
    return ListaAdyacencia

aristas = [['A', 'B'], ['A', 'C'], ['B', 'D'], ['B', 'E'], ['C', 'F'], ['C', 'G'], ['D', 'H'], ['D', 'I'], ['E', 'J'], ['E', 'K'], ['F', 'L'], ['F', 'M']]
ListaAdyacencia = generarGrafo(aristas)

def busquedaAmplitud(ListaAdyacencia, nodo):
    Visitado = set()
    cola = []
    Visitado.add(nodo)
    cola.append(nodo)
    result = []
    while cola:
        v = cola[0]
        result.append(v)
        cola = cola[1:]
        for neighbor in ListaAdyacencia[v]:
            if neighbor not in Visitado:
                Visitado.add(neighbor)
                cola.append(neighbor)
    return result
print(busquedaAmplitud(ListaAdyacencia,'H'))


