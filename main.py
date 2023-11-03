
import pygame
import button
import charactor_sprite
import spritesheet
import unanimated_sprite
import health_bar_sprite
import rps
from pygame import mixer
pygame.init()
#create game window
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("The adventure of JOMEss!!")
clock = pygame.time.Clock()
#song
mixer.music.load("sfx/song.wav")
mixer.music.set_volume(0.5)
mixer.music.play(-1)
#game variables
game_paused = False
menu_state = "main"

#FIGHTING!!!!!!!!
#define colours
TEXT_COL = (255, 255, 255)

#load images
sprite_sheet_image = pygame.image.load("images/knight_idle3.png").convert_alpha()
play_img = pygame.image.load("images/button_play.png").convert_alpha()
exit_img = pygame.image.load("images/button_exit.png").convert_alpha()
player_img = pygame.image.load("images/knight_idle.png").convert_alpha()
attack_img = pygame.image.load("images/button_attack.png").convert_alpha()
monster_img = pygame.image.load("images/monster.png").convert_alpha()
game_over_img = pygame.image.load("images/game_over.png").convert_alpha()
background = pygame.image.load("images/background.png").convert_alpha()
rock_img = pygame.image.load("rock.png").convert_alpha()
paper_img = pygame.image.load("paper.png").convert_alpha()
scissors_img  = pygame.image.load("scissors.png").convert_alpha()




#load sounds
click_sound = pygame.mixer.Sound("sfx/mouse_click.mp3")

#create instances
sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)
play_button = button.Button((SCREEN_WIDTH // 2)-100, 300, play_img, 4)
exit_button = button.Button((SCREEN_WIDTH // 2)-100, 500, exit_img, 4)
attack_button = button.Button((SCREEN_WIDTH // 2)-400, 580, attack_img, 4)
game_over_sprite = unanimated_sprite.Sprite((SCREEN_WIDTH // 2)-360, 0, game_over_img, 3)
player_sprite = charactor_sprite.Sprite((SCREEN_WIDTH // 2)-500, 400, player_img, 2.5)
monster_sprite = charactor_sprite.Sprite((SCREEN_WIDTH // 2)+150, 230, monster_img, 7)
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
health_bar = health_bar_sprite.Sprite((255,0,0),(SCREEN_WIDTH // 2)-350, 50,20)
monster_sprite_mini = charactor_sprite.Sprite((SCREEN_WIDTH // 2)-390, 20, monster_img, 2)
rock_button = button.Button((SCREEN_WIDTH // 2)-450, 580, rock_img, 1)
paper_button = button.Button((SCREEN_WIDTH // 2)-50, 580, paper_img, 1)
scissors_button = button.Button((SCREEN_WIDTH // 2)+350, 580, scissors_img, 1)
rpsgame = rps.RPS("None", "None", 3)
time = 120
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render(f'{time}', True, (196, 43, 43))
textRect = text.get_rect()
textRect.center = (640,100)
monster_health = monster_sprite.health
#game loop
run = True
while run:
  elapsed = clock.tick(60)
  screen.blit(background, (0, 0))   
  #check if game is paused
  if menu_state == "main":
    #draw pause screen buttons
    if play_button.draw(screen):
        menu_state = "main_game"

      

    if exit_button.draw(screen):
        
        run = False
  #check if the options menu is open
  elif menu_state == "main_game":   #Main Game
      time-=0.1
      
      if time<=0:
        menu_state = "game_over"
      text = font.render(f'{round(time,2)}', True, (196, 43, 43))
      screen.blit(text,textRect)
      player_sprite.draw(screen)
      monster_sprite.draw(screen)
      
      
      #health bar
      
      if health_bar.draw(screen,monster_health,monster_sprite.health):
         monster_health -= 1
         print(monster_health)
      monster_sprite_mini.draw(screen)    
      
      
      #health bar
      
      if health_bar.draw(screen,monster_health,monster_sprite.health):
         monster_health -= 1
         print(monster_health)
      monster_sprite_mini.draw(screen)
      if attack_button.draw(screen):
        
        menu_state = "RPS"
        #monster_sprite.receive_damage(10)
        print(monster_sprite.health)
        
        if monster_sprite.health == 0:
           menu_state = "game_over"
  elif menu_state == "RPS":               #Rock Paper Scissors
      time-=0.1
      
      if time<=0:
        menu_state = "game_over"
      text = font.render(f'{round(time,2)}', True, (196, 43, 43))
      screen.blit(text,textRect)
      player_sprite.draw(screen)
      monster_sprite.draw(screen)
      
      if rock_button.draw(screen):
        rpsgame.play("Rock")
      if paper_button.draw(screen):
        rpsgame.play("Paper")
      if scissors_button.draw(screen):
        rpsgame.play("Scissors")
      #health bar
      if health_bar.draw(screen,monster_health,monster_sprite.health):
         monster_health -= 1
         print(monster_health)
      monster_sprite_mini.draw(screen)
       
  
  elif menu_state == "game_over":   #Game Over
     game_over_sprite.draw(screen) 
     if exit_button.draw(screen):
        run = False

     
     
  #event handler
  for event in pygame.event.get():
    
    if event.type == pygame.QUIT:
      run = False
  
  pygame.display.update()
  pygame.time.delay(100)
  
  
  
  
pygame.quit()

