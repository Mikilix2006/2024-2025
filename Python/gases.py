gases = ["P", "V", "T"]

while True:
    correcto = False
    while not correcto:
        correcto = False
        while not correcto:
            incognita = input("¿Qué te piden? (P/V/T): ")
            if incognita.upper() not in gases:
                print("Dato incorrecto.\nVolver a introducir")
            else:
                correcto = True
                    
        correcto = False
        while not correcto:
            cte = input("¿Cuál es la constante? (P/V/T): ")
            if cte.upper() not in gases:
                print("Dato incorrecto.\nVolver a introducir")
            else:
                correcto = True
                
        if incognita == cte:
            print("La incógnita y la constante no pueden ser la misma.\nVolver a introducir")
            correcto = False
            
    # === FUNCIONES === #

    # FUNCIONES PARA INCÓGNITAS
                
    # FUNCION QUE INTRODUCE LA UNIDAD DE LA INCOGNITA Y CAMBIA EL VALOR CONOCIDO A LA UNIDAD DE LA INCÓGNITA
    def cambiar_incognita_presion(x):
        global valor_p1
        global ud_p1
        global ud_inc_p
        if x == 1:
            ud_inc_p = "atm"
            if ud_p1 == 2: # PASAR P1 DE mmHg A atm
                valor_p1 = valor_p1/760
            elif ud_p1 == 3: # PASAR P1 DE Pa A atm
                valor_p1 = ud_p1/101300
        elif x == 2:
            ud_inc_p = "mmHg"
            if ud_p1 == 1: # PASAR P1 DE atm A mmHg
                valor_p1 = valor_p1*760
            elif ud_p1 == 3: # PASAR P1 DE Pa a mmHg
                valor_p1 = valor_p1*760/101300
        elif x == 3:
            ud_inc_p = "Pa"
            if ud_p1 == 1: # PASAR P1 DE atm A Pa
                valor_p1 = valor_p1*101300
            elif ud_p1 == 2: # PASAR P1 DE mmHg A Pa
                valor_p1 = valor_p1*101300/760
        return valor_p1, ud_inc_p

    def cambiar_incognita_temperatura():
        global ud_inc_t
        global valor_t1
        global ud_t1
        if ud_t1 == 2:
            valor_t1 = valor_t1+273
        if ud_inc_t == 1:
            ud_inc_t = "K"
        if ud_inc_t == 2:
            ud_inc_t = "ºC"
        return valor_t1, ud_inc_t

    def cambiar_incognita_volumen(x):
        global ud_inc_v
        if x == 1:
            ud_inc_v = "L"
        if x== 2:
            ud_inc_v = "m^3"
        return ud_inc_v

    # FUNCIONES PARA NO INCÓGNITAS

    def cambiar_ud_temperatura(x,y):
        global valor_t1
        global valor_t2
        # PASAR TODOS DE ºC A KELVIN
        if x == 2:
            valor_t1 = valor_t1+273
        if y == 2:
            valor_t2 = valor_t2+273
        return valor_t1, valor_t2

    def cambiar_ud_presion(x,y):
        global valor_p1
        global valor_p2
        if x == 2: # PASAR DE mmHg A atm
            valor_p1 = valor_p1/760
        if x == 3: # PASAR DE pA A atm
            valor_p1 = ud_p1/101300
        if y == 2: # PASAR DE mmHg A atm
            valor_p2 = valor_p2/760
        if y == 3: # PASAR DE Pa A atm
            valor_p2 = valor_p2/101300
        return valor_p1,valor_p2


    # === CASO DE LA PRESIÓN COMO INCÓGNITA === #

    if incognita.upper() == "P": # DATO QUE PIDEN
        correcto = False
        while not correcto:
            ud_inc_p = int(input("¿En qué unidades te piden la incógnita?\n1: atm\n2: mmHg\n3: Pa\n> "))      
            if ud_inc_p not in range(1,4):
                print("Dato incorrecto.\nVolver a introducir.")
            else: # YA SE HAN METIDO LAS UNIDADES DE P2
                while not correcto:
                    ud_p1 = int(input("¿En qué unidades está la presión que te dan?\n1: atm\n2: mmHg\n3: Pa\n> "))
                    if ud_p1 not in range(1,4):
                        print("Dato incorrecto.\nVolver a introducir.")
                    else: # YA SE HAN METIDO LAS UNIDADES DE P1
                        
    # === CASO DE LA PRESIÓN COMO INCÓGNITA Y EL VOLUMEN CONSTANTE === #

                        if cte.upper() == "V": # VOLUMEN CONSTANTE
                            while not correcto:
                                ud_t1 = int(input("Introduce las unidades de la primera temperatura.\n1: Kelvin\n2: ºC\n> "))
                                if ud_t1 not in range (1,3):
                                    print("Dato incorrecto.\nVolver a introducir.")
                                else: # YA SE HAN METIDO LAS UNIDADES DE T1
                                    while not correcto:
                                        ud_t2 = int(input("Introduce las unidades de la segunda temperatura.\n1: Kelvin\n2: ºC\n> "))
                                        if ud_t2 not in range (1,3):
                                            print("Dato incorrecto.\nVolver a introducir.")
                                        else: # YA SE HAN METIDO LAS UNIDADES DE T2
                                            # EN ESTE PUNTO SE TIENEN LAS UNIDADES DE T1, T2, P1 Y P2
                                            valor_p1 = float(input("Introduce valor de la presión que te dan: "))
                                            valor_t1 = float(input("Introduce valor de la primera temperatura: "))
                                            valor_t2 = float(input("Introduce valor de la segunda temperatura: "))
                                            # EN ESTE PUNTO SE TIENEN TODOS LOS DATOS NECESARIOS
                                            # AHORA SE CONVIERTEN LAS UNIDADES DE LOS DATOS
                                            # CAMBIAR UNIDADES DE P1
                                            cambiar_incognita_presion(ud_inc_p)
                                            # EN ESTE PUNTO LAS UNNIDADES DE LAS PRESIONES SON CORRECTAS
                                            # AHORA SE CONVIERTEN LAS UNIDADES DE LAS TEMPERATURAS
                                            cambiar_ud_temperatura(ud_t1,ud_t2)
                                            # EN ESTE PUNTO LAS UNIDADES DE TODOS LOS DATOS SON CORRECTAS
                                            correcto = True
                                            # p2 = p1*t2/t1
                                            res = round(valor_p1*valor_t2/valor_t1,2)
                                            print(f"El resultado de la presión es {res} {ud_inc_p}")
                                            
    # === CASO DE LA PRESIÓN COMO INCÓGNITA Y LA TEMPERATURA CONSTANTE === #
                        
                        if cte.upper() == "T": # TEMPERATURA CONSTANTE
                            correcto = False
                            while not correcto:
                                ud_v1 = int(input("Introduce las unidades del primer volumen.\n1: Litros\n2: Decímetros cúbicos\n> "))
                                if ud_v1 not in range (1,3):
                                    print("Dato incorrecto.\nVolver a introducir.")
                                else: # YA SE HAN METIDO LAS UNIDADES DE V1
                                    while not correcto:
                                        ud_v2 = int(input("Introduce las unidades del segundo volumen.\n1: Litros\n2: Decímetros cúbicos\n> "))
                                        if ud_v2 not in range(1,3):
                                            print("Dato incorrecto.\nVolver a introducir.")
                                        else: # YA SE HAN METIDO LAS UNIDADES DE V2
                                            # EN ESTE PUNTO SE TIENEN LAS UNIDADES DE P1, P2, V1 Y V2
                                            valor_p1 = float(input("Introduce la presión que te dan: "))
                                            valor_v1 = float(input("Introduce valor del primer volumen: "))
                                            valor_v2 = float(input("Introduce valor del segundo volumen: "))
                                            # EN ESTE PUNTO SE TIENEN TODOS LOS DATOS NECESARIOS
                                            # AHORA SE CONVIERTEN LAS UNIDADES DE LOS DATOS
                                            # CAMBIAR UNIDADES DE P1
                                            cambiar_incognita_presion(ud_inc_p)
                                            # EN ESTE PUNTO LAS UNNIDADES DE LAS PRESIONES SON CORRECTAS
                                            correcto = True
                                            # p2 = p1*v1/v2
                                            res = round(valor_p1*valor_v1/valor_v2, 2)
                                            print(f"El resultado de la presión es {res} {ud_inc_p}")


    # === CASO DE LA TEMPERATURA COMO INCÓGNITA === #

    if incognita.upper() == "T": # DATO QUE PIDEN
        correcto = False
        while not correcto:
            ud_inc_t = int(input("¿En qué unidades te piden la incógnita?\n1: Kelvin\n2: ºC\n> "))      
            if ud_inc_t not in range(1,3):
                print("Dato incorrecto.\nVolver a introducir.")
            else: # YA SE HAN METIDO LAS UNIDADES DE T2
                while not correcto:
                    ud_t1 = int(input("¿En qué unidades está la temperatura que te dan?\n1: Kelvin\n2: ºC\n> "))
                    if ud_t1 not in range(1,3):
                        print("Dato incorrecto.\nVolver a introducir.")
                    else: # YA SE HAN METIDO LAS UNIDADES DE T1
                        
    # === CASO DE LA TEMPERATURA COMO INCÓGNITA Y EL VOLUMEN CONSTANTE === #

                        if cte.upper() == "V": # VOLUMEN CONSTANTE
                            while not correcto:
                                ud_p1 = int(input("Introduce las unidades de la primera presión.\n1: atm\n2: mmHg\n3: Pa\n> "))
                                if ud_p1 not in range (1,4):
                                    print("Dato incorrecto.\nVolver a introducir.")
                                else: # YA SE HAN METIDO LAS UNIDADES DE P1
                                    while not correcto:
                                        ud_p2 = int(input("Introduce las unidades de la segunda presión.\n1: atm\n2: mmHg\n3: Pa\n> "))
                                        if ud_p2 not in range (1,4):
                                            print("Dato incorrecto.\nVolver a introducir.")
                                        else: # YA SE HAN METIDO LAS UNIDADES DE P2
                                            # EN ESTE PUNTO SE TIENEN LAS UNIDADES DE T1, T2, P1 Y P2
                                            valor_t1 = float(input("Introduce valor de la temperatura que te dan: "))
                                            valor_p1 = float(input("Introduce valor de la primera presión: "))
                                            valor_p2 = float(input("Introduce valor de la segunda presión: "))
                                            # EN ESTE PUNTO SE TIENEN TODOS LOS DATOS NECESARIOS
                                            # AHORA SE CONVIERTEN LAS UNIDADES DE LOS DATOS
                                            # CAMBIAR UNIDADES DE T1
                                            cambiar_incognita_temperatura()
                                            # EN ESTE PUNTO LAS UNNIDADES DE LAS PRESIONES SON CORRECTAS
                                            # AHORA SE CONVIERTEN LAS UNIDADES DE LAS PRESIONES
                                            cambiar_ud_presion(ud_p1, ud_p2)
                                            # EN ESTE PUNTO LAS UNIDADES DE TODOS LOS DATOS SON CORRECTAS
                                            correcto = True
                                            # t2 = t1*p2/p1
                                            res = round(valor_t1*valor_p2/valor_p1,2)
                                            if ud_inc_t == "ºC":
                                                res = round(res-273,2)
                                            print(f"El resultado de la temperatura es {res} {ud_inc_t}")
                                            
    # === CASO DE LA TEMPERATURA COMO INCÓGNITA Y LA PRESIÓN CONSTANTE === #

                        if cte.upper() == "P": # PRESIÓN CONSTANTE
                            while not correcto:
                                ud_v1 = int(input("Introduce las unidades del primer volumen.\n1: Litros\n2: Decímetros cúbicos\n> "))
                                if ud_v1 not in range (1,3):
                                    print("Dato incorrecto.\nVolver a introducir.")
                                else: # YA SE HAN METIDO LAS UNIDADES DE V1
                                    while not correcto:
                                        ud_v2 = int(input("Introduce las unidades del segundo volumen.\n1: Litros\n2: Decímetros cúbicos\n> "))
                                        if ud_v2 not in range (1,3):
                                            print("Dato incorrecto.\nVolver a introducir.")
                                        else: # YA SE HAN METIDO LAS UNIDADES DE V2
                                            # EN ESTE PUNTO SE TIENEN LAS UNIDADES DE T1, T2, V1 Y V2
                                            valor_t1 = float(input("Introduce valor de la temperatura que te dan: "))
                                            valor_v1 = float(input("Introduce valor del primer volumen: "))
                                            valor_v2 = float(input("Introduce valor del segundo volumen: "))
                                            # EN ESTE PUNTO SE TIENEN TODOS LOS DATOS NECESARIOS
                                            # AHORA SE CONVIERTEN LAS UNIDADES DE LOS DATOS
                                            # CAMBIAR UNIDADES DE T1
                                            cambiar_incognita_temperatura()
                                            # EN ESTE PUNTO LAS UNNIDADES DE LOS VOLÚMENES SON CORRECTOS
                                            # NO SE CAMBIA LOS VALORE DE LOS VOLÚMENES PORQUE SON EQUIVALENTES
                                            correcto = True
                                            # t2 = t1*v2/v1
                                            res = round(valor_t1*valor_v2/valor_v1,2)
                                            if ud_inc_t == "ºC":
                                                res = round(res-273,2)
                                            print(f"El resultado de la temperatura es {res} {ud_inc_t}")
                                            
                                    
    # === CASO DEL VOLUMEN COMO INCÓGNITA === #

    if incognita.upper() == "V": # DATO QUE PIDEN
        correcto = False
        while not correcto:
            ud_inc_v = int(input("¿En qué unidades te piden la incógnita?\n1: Litros\n2: Decímetros cúbicos\n> "))      
            if ud_inc_v not in range(1,3):
                print("Dato incorrecto.\nVolver a introducir.")
            else: # YA SE HAN METIDO LAS UNIDADES DE T2
                while not correcto:
                    ud_v1 = int(input("¿En qué unidades está el volumen que te dan?\n1: Litros\n2: Decímetros cúbicos\n> "))
                    if ud_v1 not in range(1,3):
                        print("Dato incorrecto.\nVolver a introducir.")
                    else: # YA SE HAN METIDO LAS UNIDADES DE V1
                        
    # === CASO DEL VOLUMEN COMO INCÓGNITA Y LA PRESIÓN CONSTANTE === #

                        if cte.upper() == "P": # PRESIÓN CONSTANTE
                            while not correcto:
                                ud_t1 = int(input("Introduce las unidades de la primera temperatura.\n1: Kelvin\n2: ºC\n> "))
                                if ud_t1 not in range (1,3):
                                    print("Dato incorrecto.\nVolver a introducir.")
                                else: # YA SE HAN METIDO LAS UNIDADES DE T1
                                    while not correcto:
                                        ud_t2 = int(input("Introduce las unidades de la segunda temperatura.\n1: Kelvin\n2: ºC\n> "))
                                        if ud_t2 not in range (1,3):
                                            print("Dato incorrecto.\nVolver a introducir.")
                                        else: # YA SE HAN METIDO LAS UNIDADES DE T2
                                            # EN ESTE PUNTO SE TIENEN LAS UNIDADES DE T1, T2, V1 Y V2
                                            valor_v1 = float(input("Introduce valor del volumen que te dan: "))
                                            valor_t1 = float(input("Introduce valor de la primera temperatura: "))
                                            valor_t2 = float(input("Introduce valor de la segunda temperatura: "))
                                            # EN ESTE PUNTO SE TIENEN TODOS LOS DATOS NECESARIOS
                                            cambiar_incognita_volumen(ud_inc_v)
                                            # AHORA SE CONVIERTEN LAS UNIDADES DE LAS TEMPERATURAS
                                            cambiar_ud_temperatura(ud_t1, ud_t2)
                                            # EN ESTE PUNTO LAS UNIDADES DE TODOS LOS DATOS SON CORRECTAS
                                            correcto = True
                                            # v2 = v1*t2/t1
                                            res = round(valor_v1*valor_t2/valor_t1,2)
                                            print(f"El resultado de la temperatura es {res} {ud_inc_v}")
                                            
    # === CASO DEL VOLUMEN COMO INCÓGNITA Y LA TEMPERATURA CONSTANTE === #

                        if cte.upper() == "T": # TEMPERATURA CONSTANTE
                            while not correcto:
                                ud_p1 = int(input("Introduce las unidades de la primera presión.\n1: atm\n2: mmHg\n3: Pa\n> "))
                                if ud_p1 not in range (1,4):
                                    print("Dato incorrecto.\nVolver a introducir.")
                                else: # YA SE HAN METIDO LAS UNIDADES DE P1
                                    while not correcto:
                                        ud_p2 = int(input("Introduce las unidades de la segunda presión.\n1: atm\n2: mmHg\n3: Pa\n> "))
                                        if ud_p2 not in range (1,4):
                                            print("Dato incorrecto.\nVolver a introducir.")
                                        else: # YA SE HAN METIDO LAS UNIDADES DE P2
                                            # EN ESTE PUNTO SE TIENEN LAS UNIDADES DE P1, P2, V1 Y V2
                                            valor_v1 = float(input("Introduce valor del volumen que te dan: "))
                                            valor_p1 = float(input("Introduce valor de la primera presión: "))
                                            valor_p2 = float(input("Introduce valor de la segunda presión: "))
                                            # EN ESTE PUNTO SE TIENEN TODOS LOS DATOS NECESARIOS
                                            # AHORA SE CONVIERTEN LAS UNIDADES DE LOS DATOS
                                            cambiar_incognita_volumen(ud_inc_v)
                                            # AHORA SE CONVIERTEN LAS PRESIONES
                                            cambiar_ud_presion(ud_p1,ud_p2)
                                            # EN ESTE PUNTO LAS UNIDADES DE TODOS LOS DATOS SON CORRECTAS
                                            correcto = True
                                            # v2 = p1*v1/p2
                                            res = round(valor_p1*valor_v1/valor_p2,2)
                                            print(f"El resultado del volumen es {res} {ud_inc_v}")
    if input("Pulsa enter para ejecutar otra vez el programa")=="":
        print()


'''
V = cte
p2 = p1*t2/t1 DONE
t2 = t1*p2/p1 DONE
P = cte
v2 = v1*t2/t1 DONE
t2 = t1*v2/v1 DONE
T = cte
p2 = p1*v1/v2 DONE
v2 = p1*v1/p2 DONE

1 atm = 760 mmHg = 101300 Pa

0ºC = 273K

1 dm^3 = 1 L

'''
