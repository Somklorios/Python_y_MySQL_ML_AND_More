import random

options = ('piedra', 'papel', 'tijera  ')

computer_wins = 0
user_wins = 0

rounds = 1

#con while + tab podemos indexar la secuencia dentro e while
while True:
  print('* ' * 20)
  print('ROUND', rounds)
  print('* ' * 20)

  print('computer_wins', computer_wins)
  print('user_wins', user_wins)

  user_option = input('piedra, papel o tijera ---->   ')
  user_option == user_option.lower()

  #esta parte nos alerta en caso de que el usuario escoja una opcion no valida 
  if not user_option in options:
    print('esa opcion no es valida')
  computer_option = random.choice(options)

  print('User options ----> ', user_option)
  print('Computer_option ---->  ', computer_option)


  #si los dos tiene las mismas opciones es empate
  if user_option == computer_option:
    print('Empate ')

  #Si el usuario tiene piedra y la computadora tiene tijera, gana la piedra
  elif user_option == 'piedra':
    if computer_option == 'tijera':
      print('piedra gana a tijera')
      print('user gano')
      user_wins += 1
    else:
      print('piedra gana a tijera')
      print('computer gano')
      computer_wins += 1

  #Si el usuario tiene papel y la computadora tiene piedra, gana la piedra    
  elif user_option == 'papel':
    if computer_option == 'piedra':
      print('papel gana a piedra')
      print('usuario gano')
      user_wins += 1
    else:
      print('tijera gana a papel')
      print('computer gana')
      computer_wins += 1 #la compu gano

  #Si el usuario tiene tijera y la computadora tiene papel, gana la tijera       
  elif user_option == 'tijera':
    if computer_option == 'papel':
      print('tijera gana a papel')
      print('user gano')
      user_wins += 1
    else:
      print('piedra gana a tijera')
      print('computer gana')
      computer_wins += 1

  if computer_wins == 2:
    print('El ganador es la computadora')    
    break

  if user_wins == 2:
    print('El ganador es el usuario')
    break

  rounds += 1
    