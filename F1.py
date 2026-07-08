COMANDOS_VALIDOS = ['CX,ON', 'CX,OFF', 'CAL', 'SIM,ENABLE',
 'SIM,ACTIVATE', 'SIM,DISABLE'] 
EQUIPO = '1073' # variable global
def ComandosRecibidos(): 
    comandos_recibidos = [
        'CMD,1073,CX,ON',
        'CMD,1073,CAL',
        'CMD,9999,CX,ON',
        'CMD,1073,SIM,ENABLE',
        'cmd,1073,CAL',
        'CMD,1073,SIM,ACTIVATE',
        'CMD,1073,SIM,DISABLE',
        'DATOS,1073,OK',
    ]
    return comandos_recibidos
comandos_recibidos=ComandosRecibidos()

def ValidarFormato(cmd):
    print("")
    
    paq_telem=cmd.split(',')
    if paq_telem[0].upper()=="CMD" and paq_telem[1]==EQUIPO and len(paq_telem)>=2:
         return True
    else: 
        return False
        
def ExtraerInstruccion(cmd):
    if ValidarFormato(cmd) == False:
        return "INVALIDO"
    paq_telem=cmd.split(',') 
    if len(paq_telem)==3:
        com_valid=paq_telem[2]
        return com_valid
    else:
        com_valid = ','.join(paq_telem[2:4]) 
        return com_valid 

def EsInstruccionConocida(com_valid):
    if com_valid in COMANDOS_VALIDOS:
        return True 
    else: 
        return False
    
def ProcesarTodo(comandos_recibidos):
    for comando in comandos_recibidos:

        valido = ValidarFormato(comando)
        com_valid = ExtraerInstruccion(comando)

        if valido:
            estado = "VÁLIDO"
        else:
            estado = "INVÁLIDO"

        if EsInstruccionConocida(com_valid):
            conocida = "CONOCIDA"
        else:
            conocida = "-"

        print(comando, "->", estado,
              "| Instrucción:", com_valid,
              "|", conocida)
ProcesarTodo(comandos_recibidos)