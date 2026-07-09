EQUIPO = 'Cuauhtémoc' # variable global

paquetes = [
 {'id':1, 'altitud':120.3, 'temp':42.1, 'voltaje':7.80, 'estado':0},
 {'id':2, 'altitud':890.5, 'temp':41.3, 'voltaje':7.78, 'estado':1},
 {'id':3, 'altitud':2100.1, 'temp':39.8, 'voltaje':7.75, 'estado':1},
 {'id':4, 'altitud':3089.3, 'temp':38.2, 'voltaje':7.72, 'estado':2},
 {'id':5, 'altitud':1500.0, 'temp':39.1, 'voltaje':7.70, 'estado':3},
 {'id':6, 'altitud':500.2, 'temp':40.5, 'voltaje':7.65, 'estado':3},
 {'id':7, 'altitud':48.6, 'temp':41.8, 'voltaje':7.60, 'estado':6},
]
MAPA_ESTADOS = {0:'LAUNCH PAD', 1:'ASCENT', 2:'APOGEE',
 3:'DESCENT', 6:'LANDING'}

VOLTAJE_MINIMO = 7.65 # variable global 

def ObtenerNombreEstados(estado):
    if estado in MAPA_ESTADOS:
        return MAPA_ESTADOS[estado]
    else:
        return 'DESCONOCIDO'

def ClasificarVoltaje(voltaje):
    if voltaje>= 7.75:
        return 'NORMAL'
    elif voltaje>=VOLTAJE_MINIMO and voltaje< 7.75:
        return 'BAJO'
    else:
        return 'CRITICO'
    
def CalcularTasaDeDesenso(altitud_actual,altitud_anterior):
    resultado = altitud_anterior - altitud_actual
    return resultado

def MostrarReportes(paquetes):
    for paquete in paquetes:
        nombre_estado = ObtenerNombreEstados(paquete['estado']) 
        nivel_voltaje = ClasificarVoltaje(paquete['voltaje']) 
        if paquete['id']==1:
            tasa_de_desenso='N/A'
        else:
            tasa_de_desenso = CalcularTasaDeDesenso(paquete['altitud'], altitud_anterior)
        print(f"PAQUETE {paquete['id']} | {nombre_estado} | voltaje: {nivel_voltaje} | Desenso: {tasa_de_desenso}")
        altitud_anterior = paquete['altitud']

def EncontrarApogeo(paquetes):
    paquete_mas_alto = paquetes[0]
    for paquete in paquetes:
        if paquete['altitud']> paquete_mas_alto['altitud']:
            paquete_mas_alto = paquete 
    return paquete_mas_alto

def ContarAlertas(paquetes):
    alertas=0
    for paquete in paquetes:
        nivel_voltaje = ClasificarVoltaje(paquete['voltaje'])
        if (nivel_voltaje == 'BAJO' or nivel_voltaje == 'CRITICO')and (paquete['altitud'] > 500):
            alertas+=1
    return alertas

print(f'=== REPORTE DE VUELO - {EQUIPO} ===\n')
MostrarReportes(paquetes)

apogeo = EncontrarApogeo(paquetes)
print(f'\nApogeo registrado en paquete {apogeo["id"]}: {apogeo["altitud"]} m')

alertas = ContarAlertas(paquetes)
print(f'Paquetes con alerta de voltaje en vuelo: {alertas}')