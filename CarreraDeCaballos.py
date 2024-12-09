import random
import time

valla = ("|------------------------------|")

ap1 = ["1", ":", "웃"]
ap2 = ["2", ":", "웃"]
ap3 = ["3", ":", "웃"]
ap4 = ["4", ":", "웃"]
ap5 = ["5", ":", "웃"]
ap6 = ["6", ":", "웃"]

cont1 = 0
cont2 = 0
cont3 = 0
cont4 = 0
cont5 = 0
cont6 = 0       

def avanzar ():
    for i in range (len(ap1)):
        print(ap1[i], end = "")
    print()
    print(valla)
    for i in range (len(ap2)):
        print(ap2[i], end = "")
    print()
    print(valla)
    for i in range (len(ap3)):
        print(ap3[i], end = "")
    print()
    print(valla)
    for i in range (len(ap4)):
        print(ap4[i], end = "")
    print()
    print(valla)
    for i in range (len(ap5)):
        print(ap5[i], end = "")
    print()
    print(valla)
    for i in range (len(ap6)):
        print(ap6[i], end = "")
    print()
    print(valla)

while cont1 <= 13 and cont2 <= 13 and cont3 <= 13 and cont4 <= 13 and cont5 <= 13 and cont6 <= 13:
    # SELECCIONA CARRIL QUE VA A AVANZAR
    n = random.randint(1,6)
    # IDENTIFICA EL CARRIL Y LO HACE AVANZAR
    if n == 1:
        ap1.insert(2, "  ")
        cont1 = cont1 + 1
        avanzar()
        if cont1 == 14:
            print("Ha ganado el corredor 1")
    elif n == 2:
        ap2.insert(2, "  ")
        cont2 = cont2 + 1
        avanzar()
        if cont2 == 14:
            print("Ha ganado el corredor 2")
    elif n == 3:
        ap3.insert(2, "  ")
        cont3 = cont3 + 1
        avanzar()
        if cont3 == 14:
            print("Ha ganado el corredor 3")
    elif n == 4:
        ap4.insert(2, "  ")
        cont4 = cont4 + 1
        avanzar()
        if cont4 == 14:
            print("Ha ganado el corredor 4")
    elif n == 5:
        ap5.insert(2, "  ")
        cont5 = cont5 + 1
        avanzar()
        if cont5 == 14:
            print("Ha ganado el corredor 5")
    elif n == 6:
        ap6.insert(2, "  ")
        cont6 = cont6 + 1
        avanzar()
        if cont6 == 14:
            print("Ha ganado el corredor 6")
    time.sleep(0.3)
    

    

'''
PERSONAJES:
ꆛ
웃
𓅡
𓆏
〶
⊗
𓄿
https://www.adslzone.net/como-se-hace/internet/simbolos-copiar-pegar/
'''