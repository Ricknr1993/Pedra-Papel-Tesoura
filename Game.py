import time
import random

rock = '''
   
    ______
___'  _____)
      (_____)
      (_____)
      (____)
---'__ (__)
'''

paper ='''
    ________
---'   _____)____
          _______)
          _______)
         _______)
--- .__  ______)    
'''

scissors='''
    _______
---'    ____)____
         _________)       
         (________)
        (___)
---'__  (__)
'''

user_choise=int(input('''Qual sua escolha?
0 para Rocha
1 para Papel 
2 Para Tesoura
'''))

game_imagens=[rock,paper,scissors ]
print(game_imagens[user_choise])



computer_choise=random.randint(0,2)
print("Computer chose :")
print(game_imagens[computer_choise])



if user_choise == 0 and computer_choise == 2 :
    print("You Wins")
elif computer_choise == 0 and user_choise == 2:
    print("You lose")
elif user_choise > computer_choise:
    print("You win !")
elif computer_choise > user_choise:
    print("You lose!")
elif computer_choise == user_choise:
    print("Its a draw")    
elif user_choise >=3 or user_choise < 0 :
    print("You typed an invalid number ,you lose!")    


time.sleep(50)
