def divisors(num):
    divisors = [ i for i in range(1, num + 1) if num % i == 0]
    return divisors
    
def run():
        # tenemos que eliminar el int del input, ya que isnumeric da por hecho que es un numero 
        num = input("Ingresa un numero: ")
        assert not(num.isalpha()), "Debes ingresar un numero "
        assert (num.isnumeric()) > 0, "Debes ingresar un numero positivo"
        print(divisors(int(num)))
        print("termino mi programa")

if __name__ == "__main__":
    run()

    # ya tengo que dos condiciones que el usuario debe de cumplir, que no ingrese letras y que solo sean numero positivos

    #.isalpha(): verifica si todos los caracteres en la cadena num son letras(alfabéticas).

    #.isnumeric" solo reconoce como strings numericos aquellos que solo tienen numeros

    # Se lee asi, afirmo que si todos los caracteres de num.isalpha no son letras, me de vuelva TRUE y por tanto imprima "Debes ingresar un numero"