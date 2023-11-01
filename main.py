
import pygame
import button
import sprite
from pygame import mixer
pygame.init()

#create game window
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("The adventure of JOMEss!!")

#song
mixer.music.load("sfx/song.wav")
mixer.music.set_volume(0.5)
mixer.music.play(-1)
#game variables
game_paused = False
menu_state = "main"


#define colours
TEXT_COL = (255, 255, 255)

#load images
play_img = pygame.image.load("images/button_play.png").convert_alpha()
exit_img = pygame.image.load("images/button_exit.png").convert_alpha()
player_img = pygame.image.load("images/knight_idle.png").convert_alpha()
attack_img = pygame.image.load("images/button_attack.png")
monster_img = pygame.image.load("images/monster.png")
background = pygame.image.load("images/background.png")

#load sounds
click_sound = pygame.mixer.Sound("sfx/mouse_click.mp3")

#create instances
play_button = button.Button((SCREEN_WIDTH // 2)-100, 300, play_img, 4)
exit_button = button.Button((SCREEN_WIDTH // 2)-100, 500, exit_img, 4)
attack_button = button.Button((SCREEN_WIDTH // 2)-400, 580, attack_img, 4)

player_sprite = sprite.Sprite((SCREEN_WIDTH // 2)-500, 400, player_img, 2.5)
monster_sprite = sprite.Sprite((SCREEN_WIDTH // 2)+150, 230, monster_img, 7)
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

#game loop
run = True
while run:
  
  screen.blit(background, (0, 0))
  #check if game is paused
  
  if menu_state == "main":
    #draw pause screen buttons
    if play_button.draw(screen):
        click_sound.play()
        menu_state = "main_game"
      
      

    if exit_button.draw(screen):
      
        run = False
  #check if the options menu is open
  if menu_state == "main_game":
      player_sprite.draw(screen)
      monster_sprite.draw(screen)
      attack_button.draw(screen)
  #event handler
  for event in pygame.event.get():
    
    if event.type == pygame.QUIT:
      run = False
  
  pygame.display.update()

pygame.quit()