EQUIPO = '1073' # variable global
def HistorialComandos(): 
    historial = [
    {'comando': 'CX,ON', 'resultado': 'OK', 'tiempo': '00:00:05'},
    {'comando': 'CAL', 'resultado': 'OK', 'tiempo': '00:00:12'},
    {'comando': 'SIM,ENABLE', 'resultado': 'OK', 'tiempo': '00:01:00'},
    {'comando': 'SIM,ACTIVATE', 'resultado': 'OK', 'tiempo': '00:01:05'},
    {'comando': 'SIM,DISABLE', 'resultado': 'ERROR','tiempo': '00:03:00'},
    {'comando': 'CX,OFF', 'resultado': 'OK', 'tiempo': '00:05:00'},
    {'comando': 'CAL', 'resultado': 'ERROR','tiempo': '00:05:30'},
    {'comando': 'CX,ON', 'resultado': 'OK', 'tiempo': '00:06:00'},
    ]
    return historial
historial=HistorialComandos()  

def ContarResultados(historial):
    contador_ok=0
    contador_error=0
    for registro in historial:
        if registro['resultado']=='OK':
            contador_ok+=1
        elif registro['resultado']=='ERROR':
            contador_error+=1
    return {'OK': contador_ok, 'ERROR': contador_error}   

def BuscarComando(historial, nombre):
    lista_encontrados=[]
    for registro in historial:
        if registro['comando']==nombre:
            lista_encontrados.append(registro)
    return lista_encontrados

def ComandoMasUsado(historial):
    frecuencias={}
    for registro in historial:
        if registro['comando'] in frecuencias:
            frecuencias[registro['comando']] += 1
        else:
            frecuencias[registro['comando']] = 1             
    comando_max = ""
    max_apariciones = 0    
    for comando in frecuencias:       
        if frecuencias[comando] > max_apariciones:
            max_apariciones = frecuencias[comando]
            comando_max = comando            
    return comando_max 

def MostrarHistorial(historial):
    print(f"=== HISTORIAL DE COMANDOS – EQUIPO {EQUIPO} ===")
    for registro in historial:
        print(f"{registro['tiempo']} | {registro['comando']:<14} | {registro['resultado']}")
    # Llamamos a ContarResultados() para obtener el diccionario de conteos
    res = ContarResultados(historial)
    print(f"Resultados  → OK: {res['OK']}  |  ERROR: {res['ERROR']}")    
    # Obtenemos el comando más usado llamando a ComandoMasUsado()
    mas_usado = ComandoMasUsado(historial)
    veces = len(BuscarComando(historial, mas_usado))
    
    print(f"Comando más usado: {mas_usado} (aparece {veces} veces)")
MostrarHistorial(historial)
    

