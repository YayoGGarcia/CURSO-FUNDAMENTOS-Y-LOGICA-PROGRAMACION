def PaquetesRecibidos():
    # Lista de prueba con tramas
    paquetes_recibidos = [1, 2, 3, 5, 6, 7, 9, 10, 11, 12, 15]

    
    paquetes_limpios = []
    
    # --- ESCUDOS 1 y 2: Filtrar tipos y duplicados a mano 
    for i in range(len(paquetes_recibidos)):
        elemento_actual = paquetes_recibidos[i]
        
        # 1. Primer if: ¿Es un número entero?
        if type(elemento_actual) == int:
            
            # 2. Segundo paso: ¿Ya lo tenemos en paquetes_limpios? 
            # Usamos una variable "bandera" (flag) para buscarlo manualmente
            ya_existe = False
            for j in range(len(paquetes_limpios)):
                if paquetes_limpios[j] == elemento_actual:
                    ya_existe = True
            
            # Si terminamos de buscar y no existe, lo agregamos
            if ya_existe == False:
                paquetes_limpios.append(elemento_actual)
                
    # --- ESCUDO 3: Ordenamiento Burbuja 
    cantidad_elementos = len(paquetes_limpios)
    
    for i in range(cantidad_elementos):
        
        for j in range(0, cantidad_elementos - i - 1):
            
            # Si el elemento izquierdo es mayor que el derecho, los intercambiamos
            if paquetes_limpios[j] > paquetes_limpios[j + 1]:
                
                # Intercambio manual usando una variable temporal
                temporal = paquetes_limpios[j]
                paquetes_limpios[j] = paquetes_limpios[j + 1]
                paquetes_limpios[j + 1] = temporal

    # Retornamos la lista filtrada, sin duplicados y ordenada 
    return paquetes_limpios

paquetes_recibidos = PaquetesRecibidos()




def RecibirPaquetesPerdidos(paquetes_recibidos):
    numeros_perdidos = []
    
    # ESCUDO 4
    if len(paquetes_recibidos) <= 1:
        return numeros_perdidos
        
    for i in range(len(paquetes_recibidos) - 1):
        num_actual = paquetes_recibidos[i]
        num_sig = paquetes_recibidos[i + 1] 
        if num_actual + 1 != num_sig:
            for j in range(num_actual + 1, num_sig):
                numeros_perdidos.append(j)
    return numeros_perdidos


def PorcentajeDePerdida(paquetes_recibidos, numeros_perdidos):
    paq_recibidos = len(paquetes_recibidos)
    num_perdidos = len(numeros_perdidos)
    
    # ESCUDO 5
    if (paq_recibidos + num_perdidos) == 0:
        porcentaje_de_perdida = 0.0
    else:
        porcentaje_de_perdida = (num_perdidos / (paq_recibidos + num_perdidos)) * 100
        
    return porcentaje_de_perdida


def MostrarLista(paquetes_recibidos, numeros_perdidos, porcentaje_de_perdida):
    print(f"Paquetes perdidos : {numeros_perdidos}")
    print(f"Paquetes recibidos: {len(paquetes_recibidos)}")
    print(f"Paquetes perdidos : {len(numeros_perdidos)}")
    print(f"Porcentaje pérdida: {porcentaje_de_perdida:.2f} %")


numeros_perdidos = RecibirPaquetesPerdidos(paquetes_recibidos)
porcentaje_de_perdida = PorcentajeDePerdida(paquetes_recibidos, numeros_perdidos)
MostrarLista(paquetes_recibidos, numeros_perdidos, porcentaje_de_perdida)