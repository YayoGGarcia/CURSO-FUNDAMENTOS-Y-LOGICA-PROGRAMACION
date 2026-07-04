#ORDENAMIENTO BURBUJA 
def ListaAltitudes(): 
    altitudes = [500.2, 3089.3, 120.3, 1900.4, 890.1,
    2100.5, 48.6, 345.7, 2800.1, 1450.2]
    return altitudes
altitudes=ListaAltitudes() 

def OrdenamientoBurbuja(altitudes):
    num_elementos_lista=len(altitudes) 
    for i in range (num_elementos_lista-1):
        intercambio=False
        for j in range (num_elementos_lista-1-i):
            if (altitudes[j]<altitudes[j+1]):
                aux=altitudes[j] 
                altitudes[j]=altitudes[j+1]
                altitudes[j+1]=aux 
                intercambio=True
        if not intercambio:
            break
    return altitudes


def MostrarListaOrdenada(altitudes):
    num_elementos_lista=len(altitudes)
    for i in range(num_elementos_lista):
        print(f"POSICION ",i+1, ": ",altitudes[i]," m" )

altitudes=OrdenamientoBurbuja(altitudes)
MostrarListaOrdenada(altitudes)

