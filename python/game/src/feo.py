import random

options = ('piedra', 'papel', 'tijera')
computer_wins = 0
user_wins = 0
round = 1


while True:
  user_option = input("piedra, papel o tijera => ")
  user_option = user_option.lower()
  computer_option = random.choice(options)
  print('usuario elige',user_option)
  print('pc elige',computer_option)
  print('computer points', computer_wins)
  print('user points', user_wins)
  
  if not user_option in options:
    print('piedra, papel o tijera')
    continue
  if user_option == computer_option:
    print('Empate')
    round += 1
  elif user_option == 'piedra':
    if computer_option == 'tijera':
      print('piedra gana a tijera')
      print('usuario gana')
      user_wins += 1
    else:
      print('papel gana a piedra')
      print('computadora gana')
      computer_wins +=1
  elif user_option == 'papel':
    if computer_option == 'piedra':
      print('papel gana a piedra')
      print('usuario gana')
      user_wins += 1
    else:
      print('tijera gana a papel')
      print('computadora gana')
      computer_wins +=1
  elif user_option == 'tijera':
    if computer_option == 'papel':
      print('tijera gana a papel')
      print('usuario gana')
      user_wins += 1
    else:
      print('piedra gana a tijera')
      print('computadora gana')
      computer_wins +=1

  if user_wins == 3:
    print('usuario gana el juego')
    break
  if computer_wins == 3:
    print('computadora gana juego')
    break
