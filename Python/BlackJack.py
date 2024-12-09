import random
import time

cartas = ["As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
mano_crupier = []
mano_crupier_palos = []
mano_jugador = []
mano_jugador_palos = []

puntos = {"As" : 1, "2" : 2, "3" : 3,
          "4" : 4, "5" : 5, "6" : 6,
          "7" : 7, "8" : 8, "9" : 9,
          "10" : 10, "J" : 10, "Q" : 10, "K" : 10}
palos = {1 : "♠", 2: "♦",
         3: "♣", 4: "♥"}

# FUNCIONES DEL CRUPIER
    
def asignacionCrupier(mano_crupier):
    palo_carta = palos[random.randint(1,4)] # ASIGNA PALO A CADA CARTA QUE SALE
    mano_crupier_palos.append(f"{mano_crupier[len(mano_crupier)-1]} {palo_carta}") # AÑADE CARTA CON PALO A MANO DE CRUPIER
    return mano_crupier_palos
    
def crupier():
    eleccion = cartas[random.randint(0,len(cartas)-1)] # ELIGE UNA CARTA EN CARTAS
    mano_crupier.append(eleccion) # AÑADE LA CARTA A LA MANO DEL CRUPIER
    return mano_crupier # DEVUELVE LA MANO

def puntosCrupier (mano_crupier):
    global suma_crupier
    suma_crupier = 0 # CADA VEZ QUE SE CORRA LA FUNCIÓN RESETEA LA SUMA
    # SUMA PUNTOS DE CARTAS QUE LE HAN TOCADO
    for i in range (len(mano_crupier)):
        suma_crupier = suma_crupier + puntos[mano_crupier[i]]
    asignacionCrupier(mano_crupier) # LLAMADA DE FUNCION
    '''# COMPRUEBA SI PALO ASIGNADO COINCIDE CON ALGUNA CARTA YA ASIGNADA ANTERIORMENTE
    for i in range (len(mano_crupier)-1):
        if mano_crupier[len(mano_crupier)-1] in mano_crupier or mano_crupier[len(mano_crupier)-1] in mano_jugador:
            mano_crupier_palos.remove(f"{mano_crupier[len(mano_crupier)-1]}") # EXPULSA CARTA REPETIDA Y REEMPLAZA POR OTRA
            palo_carta = palos[random.randint(1,4)]
            mano_crupier_palos.append(f"{mano_crupier[i]} {palo_carta}")
            suma_crupier = 0 # REASIGNA EL VALOR CORRECTO DE LA SUMA CON LA NUEVA CARTA
            for i in range (len(mano_crupier)):
                suma_crupier = suma_crupier + puntos[mano_crupier[i]]'''
    # IMPRIME LA INFO Y ESPERA 2 SEGS
    print(f"Mano crupier: {mano_crupier_palos}")
    print(f"Crupier ha obtenido: {mano_crupier_palos[len(mano_crupier_palos)-1]}")
    time.sleep(2)
    # SI LA MANO DEL CRUPIER NO LLEGA A 18 O MAS, EJECUTA MÁS VECES EL CÓDIGO
    if suma_crupier < 18:
        crupier()
        puntosCrupier(mano_crupier)
    return suma_crupier # DEVUELVE LA SUMA DE LA MANO DEL CRUPIER

def turnocrupier():
    crupier()
    puntosCrupier(mano_crupier)
    print(f"Puntuación final: {suma_crupier}")
    
# FUNCIONES DEL JUGADOR
    
def jugador():
    eleccion = cartas[random.randint(0,len(cartas)-1)] # ELIGE UNA CARTA EN CARTAS
    return mano_jugador.append(eleccion) # AÑADE LA CARTA A LA MANO DEL JUGADOR

def puntosjugador(mano_jugador):
    global suma_jugador
    global mano_jugador_palos
    suma_jugador = 0 # CADA VEZ QUE SE CORRA LA FUNCIÓN RESETEA LA SUMA
    # SUMAR LAS CARTAS DE LA MANO
    for i in range (len(mano_jugador)):
        suma_jugador = suma_jugador + puntos[mano_jugador[i]]
    palo_carta = palos[random.randint(1,4)] # ELIGE UN PALO
    mano_jugador_palos.append(f"{mano_jugador[i]} {palo_carta}") # ASIGNA EL PALO A LA CARTA Y LA AÑADE A LA MANO
    return suma_jugador


# COMIENZO DEL JUEGO
carta_nueva = str(input("¿Quieres carta? (si/no)")) # PREGUNTA POR OTRA CARTA
carta_nueva = carta_nueva.upper() # PASA RESPUESTA A MAYUSCULAS
suma_jugador = 0
while carta_nueva == "SI": # EJECUTA SI AFIRMATIVO
    if suma_jugador < 21: # EJECUTA SI SUMA 21 O MENOS
        jugador() # SACA UNA CARTA
        puntosjugador(mano_jugador)
        print(mano_jugador_palos) # IMPRIME LA MANO CON LA NUEVA CARTA
    print(f"Has obtenido {suma_jugador} puntos") # IMPRIME LA SUMA DE LA MANO
    carta_nueva = "x" # RESETEA LA RESPUESTA DE CARTANUEVA
    if suma_jugador < 21: # SI NO SUMA 21 O MAS, PREGUNTA POR OTRA CARTA
        carta_nueva = str(input("¿Quieres otra carta? (si/no): "))
        carta_nueva = carta_nueva.upper() # PASA LA RESPUESTA A MAYUSCULAS

turnocrupier() # EJECUTA TURNO DEL CRUPIER

# DEFINE QUIEN HA GANADO
if suma_crupier == 21:
    print("Ha ganado el crupier")
elif suma_jugador == 21 and suma_crupier < 21:
    print("Has ganado al crupier")
elif suma_crupier > 21 and suma_jugador <= 21:
    print("Has ganado al crupier")
elif suma_jugador > 21:
    print("Has perdido")
elif suma_crupier < 21 and suma_jugador < 21:
    if suma_jugador < suma_crupier:
        print("Ha ganado el crupier")
    elif suma_jugador == suma_crupier:
        print("Ha ganado el crupier")
    elif suma_jugador > suma_crupier:
        print("Has ganado al crupier")
