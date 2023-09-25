def divisors(num):
    divisors = [ i for i in range(1, num + 1) if num % i == 0]
    return divisors
    
def run():
    try:
        num = int(input("Ingresa un numero: "))
        if num < 0:
            raise ValueError("Solo numeros positivos")
        print(divisors(num))
        print("termino mi programa")
    except ValueError:
        print("Debes ingresar un numero positivo")    

if __name__ == "__main__":
    run()