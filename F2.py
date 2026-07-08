LIMITE_TEMP = 45.0 # variable global — temperatura máxima permitida
LIMITE_VOLT = 7.60 # variable global — voltaje mínimo permitido

def SensoresRecibidos(): 
    # Creamos y retornamos la lista de diccionarios
    sensores = [
        {'nombre': 'Barometro', 'unidad': 'kPa', 'lectura': 85.3, 'activo': True },
        {'nombre': 'Temperatura', 'unidad': 'C', 'lectura': 46.2, 'activo': True },
        {'nombre': 'GPS', 'unidad': 'coord','lectura': 38.37, 'activo': True },
        {'nombre': 'Voltaje', 'unidad': 'V', 'lectura': 7.55, 'activo': True },
        {'nombre': 'Giroscopio', 'unidad': 'deg/s','lectura': 2.1, 'activo': False},
        {'nombre': 'Acelerometro', 'unidad': 'm/s2', 'lectura': 9.85, 'activo': True },
    ] 
    return sensores 

# Guardamos los sensores en una variable global
sensores = SensoresRecibidos() 

def SensoresActivos(sensores):
    list_sens_act = []
    # Usamos tu variable 'com' para iterar sobre la lista
    for com in sensores:
        # Consultamos directamente la llave del diccionario
        if com['activo'] == True:
            list_sens_act.append(com)
    return list_sens_act

def VerificarAlertas(list_sens_act):
    # Usamos tu variable 'sensor_ver' para iterar
    for sensor_ver in list_sens_act:
        # Verificamos si es temperatura y supera el límite
        if sensor_ver['nombre'] == 'Temperatura' and sensor_ver['lectura'] > LIMITE_TEMP:
            print(f"ALERTA: {sensor_ver['nombre']} en {sensor_ver['lectura']} C - supera el limite de {LIMITE_TEMP} C")
        
        # Verificamos si es voltaje y cae por debajo del límite
        if sensor_ver['nombre'] == 'Voltaje' and sensor_ver['lectura'] < LIMITE_VOLT:
            print(f"ALERTA: {sensor_ver['nombre']} en {sensor_ver['lectura']} V - por debajo del minimo de {LIMITE_VOLT} V")

def CalcularEstadisticas(sensores):
    lista_estadistica = {} # Diccionario vacío donde guardaremos el resumen
    total = 0
    activos = 0
    con_alerta = 0 
    
    # Usamos tu variable 'estadistica' para iterar
    for estadistica in sensores: 
        total += 1 # Cuenta todos los sensores (remplaza a len)
        
        if estadistica['activo'] == True:
            activos += 1
            
        # Condición con 'or' porque puede ser alerta de Temp o de Voltaje
        if (estadistica['nombre'] == 'Temperatura' and estadistica['lectura'] > LIMITE_TEMP) or \
           (estadistica['nombre'] == 'Voltaje' and estadistica['lectura'] < LIMITE_VOLT):
            con_alerta += 1 
            
    # Llenamos el diccionario con los resultados de los contadores
    lista_estadistica['total'] = total
    lista_estadistica['activos'] = activos
    lista_estadistica['con_alerta'] = con_alerta
    
    return lista_estadistica 

def MostrarPanel(sensores):
    print("=== PANEL DE SENSORES ===")
    for com in sensores:
        estado = "ACTIVO  " if com['activo'] else "INACTIVO"
        print(f"{com['nombre']:<13} [{estado}] : {com['lectura']} {com['unidad']}")
    
    print() # Espacio en blanco
    
    # Ejecutamos las alertas pasándole solo los activos
    list_sens_act = SensoresActivos(sensores)
    VerificarAlertas(list_sens_act)
    
    print() # Espacio en blanco
    
    # Ejecutamos estadísticas pasándole todos los sensores
    lista_estadistica = CalcularEstadisticas(sensores)
    print(f"Total sensores : {lista_estadistica['total']}")
    print(f"Activos        : {lista_estadistica['activos']}")
    print(f"Con alerta     : {lista_estadistica['con_alerta']}")

# Llamada principal para arrancar el programa
MostrarPanel(sensores)