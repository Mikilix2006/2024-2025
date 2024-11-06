import math

def esPrimo(n):
    i = 2 # Divisor
    while i < math.sqrt(n):
        if n % i == 0:
            return False
        else:
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
