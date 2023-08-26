user_option = input('piedra, papel o tijera ----> ')
user_option == user_option.lower()
computer_option = 'piedra'


#si los dos tiene las mismas opciones es empate
if user_option == computer_option:
  print('Empate ')

#Si el usuario tiene piedra y la computadora tiene tijera, gana la piedra
elif user_option == 'piedra':
  if computer_option == 'tijera':
    print('piedra gana a tijera')
    print('user gano')
  else:
    print('piedra gana a tijera')
    print('computer gano')

#Si el usuario tiene papel y la computadora tiene piedra, gana la piedra    
elif user_option == 'papel':
  if computer_option == 'piedra':
    print('papel gana a piedra')
    print('usuario gano')
  else:
    print('tijera gana a papel')
    print('computer gana')

#Si el usuario tiene tijera y la computadora tiene papel, gana la tijera       
elif user_option == 'tijera':
  if computer_option == 'papel':
    print('tijera gana a papel')
    print('user gano')
  else:
    print('piedra gana a tijera')
    print('computer gana')
  