import math

def esPrimo(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range (2,round(math.sqrt(n)+5,1)):
        if n % i == 0:
            return False
        else:
            if i > math.sqrt(n):
                return True

min = int(input("Desde que número quieres la lista?: "))
while min < 1:
    print("Sólo admitidos números mayores a 1")
    min = int(input("Desde que número quieres la lista?: "))

max = int(input("Hasta que número quieres la lista?: "))
while max < min:
    print("Sólo admitidos máximos mayores a los mínimos")
    max = int(input("Hasta que número quieres la lista?: "))
        
while min <= max:
    if esPrimo(min):
        print(f"{min} ")
        min = min + 1
    else:
        min = min + 1
