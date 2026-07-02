def HistorialDeVuelo():
    historial = [0,0,0,1,1,1,1,2,3,3,3,3,3,4,5,6,6,6]
    return historial
historial=HistorialDeVuelo()

def FasesDeVuelo():
    FASES = {
    0: 'LAUNCH PAD',
    1: 'ASCENT',
    2: 'APOGEE',
    3: 'DESCENT',
    4: 'PAYLOAD RELEASE',
    5: 'PROBE RELEASE',
    6: 'LANDING'
    } 
    return FASES
FASES=FasesDeVuelo()
 
def ConteoPorFase(historial,FASES):
    CONTEO={}
    for claves,valor in FASES.items():
        contador=0
        for j in range (len(historial)):
            if claves==historial[j]:
                contador+=1
        CONTEO[valor] = contador
    return CONTEO


def FaseDeVueloMasLarga(CONTEO):

    cont_fase_mas_larga = 0
    fase_mas_larga = ""

    for clave, valor in CONTEO.items():

        if valor > cont_fase_mas_larga:
            cont_fase_mas_larga = valor
            fase_mas_larga = clave

    return fase_mas_larga, cont_fase_mas_larga


def MostrarResumen(historial, FASES):

    CONTEO = ConteoPorFase(historial, FASES)
    fase_mas_larga, cont_fase_mas_larga = FaseDeVueloMasLarga(CONTEO)

    for i in range(7):
        print(f"{FASES[i]} : {CONTEO[FASES[i]]} paquetes")

    print(f"\nFase más larga: {fase_mas_larga} ({cont_fase_mas_larga} paquetes)")
MostrarResumen(historial, FASES)