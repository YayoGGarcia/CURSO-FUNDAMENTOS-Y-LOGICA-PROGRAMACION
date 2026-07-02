def PaquetesRecibidos():
    paquetes_recibidos = [1, 2, 3, 5, 6, 7, 9, 10, 11, 12, 15]
    return paquetes_recibidos
paquetes_recibidos=PaquetesRecibidos()


def RecibirPaquetesPerdidos(paquetes_recibidos):
    numeros_perdidos=[]
    for i in range(len(paquetes_recibidos)-1):
        print("")
        num_actual=paquetes_recibidos[i]
        num_sig=paquetes_recibidos[i+1] 
        if num_actual+1!=num_sig:
            for j in range(num_actual + 1, num_sig):
                numeros_perdidos.append(j)
    return numeros_perdidos


def PorcentajeDePerdida(paquetes_recibidos,numeros_perdidos):
    paq_recibidos= len(paquetes_recibidos)
    num_perdidos= len(numeros_perdidos)
    porcentaje_de_perdida=(num_perdidos/(paq_recibidos+num_perdidos))*100
    return porcentaje_de_perdida


def MostrarLista(paquetes_recibidos, numeros_perdidos, porcentaje_de_perdida):
    print(f"Paquetes perdidos : {numeros_perdidos}")
    print(f"Paquetes recibidos: {len(paquetes_recibidos)}")
    print(f"Paquetes perdidos : {len(numeros_perdidos)}")
    print(f"Porcentaje pérdida: {porcentaje_de_perdida:.2f} %")
numeros_perdidos=RecibirPaquetesPerdidos(paquetes_recibidos)
porcentaje_de_perdida=PorcentajeDePerdida(paquetes_recibidos,numeros_perdidos)
MostrarLista(paquetes_recibidos, numeros_perdidos, porcentaje_de_perdida)
