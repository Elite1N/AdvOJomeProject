import pygame
import random

choices = ["Rock", "Paper", "Scissors"]
class RPS:
    def __init__(self,player_choice):
        self.player_choice = player_choice
        self.computer_choice = "None"
        self.win = 0
        self.lose = 0
        self.victory = False
        self.defeat = False

    def play(self, player_choice):
        
        self.player_choice = player_choice
        self.computer_choice = random.choice(choices)
        

        print('Player: ' , self.player_choice)
        print('Computer' , self.computer_choice)
        if self.player_choice == self.computer_choice:
            print ("Tied")
        elif (self.player_choice == "Rock" and self.computer_choice == "Scissors") or \
                (self.player_choice == "Paper" and self.computer_choice == "Rock") or \
                (self.player_choice == "Scissors" and self.computer_choice == "Paper"):
            print ('You win')
            self.win +=1

            
        else:
            print ("Computer wins")
            self.lose+=1

        
        print ("Wins",self.win)
        print ("Losses",self.lose)
        
        
        
        if self.lose >=2 :
            print ('You also sucks')
            self.count = 0 
            self.win = 0
            self.lose = 0  
            self.defeat = True         
        
        
        elif self.win >= 2 :
            print ('Total domination')
            self.count = 0 
            self.win = 0       
            self.lose = 0 
            self.victory = True
            
        print ('-----------------------')

    def wincheck(self):
        return self.victory
    def lostcheck(self):
        return self.defeat

        

