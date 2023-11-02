import pygame
import random

choices = ["Rock", "Paper", "Scissors"]
count = 0
class RPS:
    def __init__(self):
        self.player_choice = "None"
        self.computer_choice = "None"
        #self.result = "None"
        self.count = 0

    def play(self, player_choice):
        self.player_choice = player_choice
        self.computer_choice = random.choice(choices)
        if self.player_choice == self.computer_choice:
            #elf.result = "Tied"
            pass
        elif (self.player_choice == "Rock" and self.computer_choice == "Scissors") or \
                (self.player_choice == "Paper" and self.computer_choice == "Rock") or \
                (self.player_choice == "Scissors" and self.computer_choice == "Paper"):
            #self.result = "You Win"
            self.count+=1
            
        else:
            #self.result = "Computer Wins"
            self.count=0
        if self.count >= 2:
            print ('You win!!!')
        else :
            print ('Fuck you!!!')


