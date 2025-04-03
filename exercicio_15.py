# Exercício 15
# Multiplicador

def multiplier(*args):
    multi = 1

    for i in args:
        multi *= i
    
    return multi


argumentos = input('Digite os números que você deseja multiplicar (Separe-os com " "): ').strip()
arr = argumentos.split(' ')

i = 0

for j in range(len(arr)):
    arr[i] = int(arr[i]) # type: ignore

    i += 1

resultado = multiplier(*arr)
print(resultado)

