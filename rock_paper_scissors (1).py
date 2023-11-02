import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rock, Paper, Scissors")

# Load images
rock_img = pygame.image.load("rock.png")
paper_img = pygame.image.load("paper.png")
scissors_img = pygame.image.load("scissors.png")

# Create a list of game choices
choices = ["Rock", "Paper", "Scissors"]

class Game:
    def __init__(self):
        self.player_choice = "None"
        self.computer_choice = "None"
        self.result = "None"
        self.count = 0
        self.tries = 0
    def play(self, player_choice):
        self.player_choice = player_choice
        self.computer_choice = random.choice(choices)
        if self.player_choice == self.computer_choice:
            self.result = "Tied"
            
        elif (self.player_choice == "Rock" and self.computer_choice == "Scissors") or \
                (self.player_choice == "Paper" and self.computer_choice == "Rock") or \
                (self.player_choice == "Scissors" and self.computer_choice == "Paper"):
            self.result = "You Win"
            self.count +=1
        else:
            self.result = "Computer Wins"
            self.count = 0
        if self.count == 3 :
            print ("You Win!!!!!")
        print (self.count)
    def draw(self):
        screen.fill(WHITE)
        screen.blit(rock_img, (100, 200))
        screen.blit(paper_img, (300, 200))
        screen.blit(scissors_img, (500, 200))

        font = pygame.font.Font(None, 36)
        text = font.render("Your Choice: " + self.player_choice, True, (0, 0, 0))
        screen.blit(text, (50, 50))

        text = font.render("Computer's Choice: " + self.computer_choice, True, (0, 0, 0))
        screen.blit(text, (50, 100))

        text = font.render("Result: " + self.result, True, (0, 0, 0))
        screen.blit(text, (50, 150))

        pygame.display.flip()

def main():
    game_instance = Game()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if 100 <= x <= 200:
                    game_instance.play("Rock")
                    game_instance.tries+=1
                elif 300 <= x <= 400:
                    game_instance.play("Paper")
                    game_instance.tries+=1
                elif 500 <= x <= 600:
                    game_instance.play("Scissors")
                    game_instance.tries+=1
             
            if game_instance.tries == 3 :
                print ('Out of tries')
        game_instance.draw()

    pygame.quit()

if __name__ == '__main__':
    main()
