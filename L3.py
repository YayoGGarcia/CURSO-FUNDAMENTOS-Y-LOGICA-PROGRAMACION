def ListaDeTemperaturas():
    temperaturas = [42.1, 41.8, 41.3, 40.5, 39.8, 38.9, 38.2, 38.5, 39.1, 40.2, 41.0,41.5]
    return temperaturas
temperaturas=ListaDeTemperaturas() 

tamano_ventana=3 

def PromedioVentana(temperaturas,inicio,tamano_ventana):
    sum_total=0
    prom=0
    for i in range (inicio,inicio+tamano_ventana):
        sum_total+=temperaturas[i]
    prom=sum_total/tamano_ventana 
    return round(prom, 2)

def CalcularPromediosMoviles(temperaturas):
    lista_promedios=[]
    for i in range (0, (len(temperaturas))):
        if i < tamano_ventana-1:
            lista_promedios.append("N/A")
        elif i >= tamano_ventana -1: 
            inicio_ventana = i - tamano_ventana + 1
            prom=PromedioVentana(temperaturas,inicio_ventana,tamano_ventana)
            lista_promedios.append(prom)
    return lista_promedios
lista_promedios=CalcularPromediosMoviles(temperaturas) 
print(f"PROMEDIOS MOVILES: {lista_promedios}")

def DetectarTendencia(lista_promedios):
    primer_valor_valido=None
    ultimo_valor_valido=None
    for i in range (0, len(lista_promedios)):
        elemento_actual = lista_promedios[i]
        if (elemento_actual!="N/A"):
            if(primer_valor_valido==None):
                primer_valor_valido=elemento_actual
            ultimo_valor_valido=elemento_actual
    if ultimo_valor_valido>primer_valor_valido:
        print(" CALENTO ")
    if ultimo_valor_valido<primer_valor_valido:
        print(" ENFRIO ")    
    else:
        print(" ESTABLE ")
DetectarTendencia(lista_promedios)