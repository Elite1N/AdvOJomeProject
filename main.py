import pygame
import button
import charactor_sprite
import spritesheet
import unanimated_sprite
import health_bar_sprite
import random
import rps
from black_jack import Black_jack
from pygame import mixer
import textobject
pygame.init()
#create game window
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Adventure in Novigrad")
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
monster_img = pygame.image.load("images/monster.png").convert_alpha()
game_over_img = pygame.image.load("images/game_over.png").convert_alpha()
background = pygame.image.load("images/background.png").convert_alpha()
player_img = pygame.image.load("images/knight_idle.png").convert_alpha()

draw_img = pygame.image.load("images/button_draw.png").convert_alpha()
stay_img = pygame.image.load("images/button_stay.png").convert_alpha()
play_img = pygame.image.load("images/button_play.png").convert_alpha()
exit_img = pygame.image.load("images/button_exit.png").convert_alpha()
attack_img = pygame.image.load("images/button_attack.png").convert_alpha()

rock_img = pygame.image.load("images/rock.png").convert_alpha()
paper_img = pygame.image.load("images/paper.png").convert_alpha()
scissors_img  = pygame.image.load("images/scissors.png").convert_alpha()



#load sounds
click_sound = pygame.mixer.Sound("sfx/mouse_click.mp3")

#create instances
game_over_sprite = unanimated_sprite.Sprite((SCREEN_WIDTH // 2)-360, 0, game_over_img, 3)
player_sprite = charactor_sprite.Sprite((SCREEN_WIDTH // 2)-500, 400, player_img, 2.5)
monster_sprite = charactor_sprite.Sprite((SCREEN_WIDTH // 2)+150, 230, monster_img, 7)
monster_sprite_mini = charactor_sprite.Sprite((SCREEN_WIDTH // 2)-390, 20, monster_img, 2)

background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
health_bar = health_bar_sprite.Sprite((255,0,0),(SCREEN_WIDTH // 2)-350, 50,20)
health_bar_final = health_bar_sprite.Sprite((255,0,0),(SCREEN_WIDTH // 2)-350, 50,20)


draw_button = button.Button((SCREEN_WIDTH // 2)-100, 600, draw_img, 4)
stay_button = button.Button((SCREEN_WIDTH // 2)+100, 600, stay_img, 4)
exit_button1 = button.Button((SCREEN_WIDTH // 2)-100, 500, exit_img, 4)
exit_button2 = button.Button((SCREEN_WIDTH // 2)+300, 600, exit_img, 4)
play_button = button.Button((SCREEN_WIDTH // 2)-100, 300, play_img, 4)
exit_button = button.Button((SCREEN_WIDTH // 2)-100, 500, exit_img, 4)
attack_button = button.Button((SCREEN_WIDTH // 2)-400, 580, attack_img, 4)

rock_button = button.Button((SCREEN_WIDTH // 2)-450, 550, rock_img, 1)
paper_button = button.Button((SCREEN_WIDTH // 2)-50, 550, paper_img, 1)
scissors_button = button.Button((SCREEN_WIDTH // 2)+350, 550, scissors_img, 1)

playerpick = rock_img
player_choice_button = button.Button((SCREEN_WIDTH // 2)-450, 300, playerpick, 1)

rpsgame = rps.RPS("None")

#constant
time = 120

monster_health = 0
FPS = 60
Final_boss = False


#menu_state = "black_jack"
bjvalid = False
bj = None
check = False

game_list = ["black_jack","RPS"]
#game loop
run = True

while run: 
  random_damage = random.randint(1, 3)
  screen.blit(background, (0, 0))
  random_game = random.choice(game_list)

  if menu_state == "main":
    if play_button.draw(screen):
        menu_state = "main_game"

    if exit_button.draw(screen): 
        run = False
  #check if the options menu is open
  elif menu_state == "main_game":
      time-=1/60
      TimeText = textobject.Text(640,100,32,(196, 43, 43),f'{round(time,1)}',screen)
      TimeText.draw()
      if time<=0:
        menu_state = "game_over"

      player_sprite.draw(screen)
      monster_sprite.draw(screen)

      
      #health bar
      
      if health_bar.draw(screen,monster_health,monster_sprite.health):
         monster_health += 1
         #print("monster_sprite:",monster_sprite.health)
         print("monster_health:",monster_health)

      if health_bar.draw(screen,monster_health,monster_sprite.health) == False:
         monster_health -= 1
         #print("monster_sprite:",monster_sprite.health)
         print("monster_health:",monster_health)
      

      monster_sprite_mini.draw(screen)
      #print(health_bar.draw(screen,monster_health,monster_sprite.health))
      if attack_button.draw(screen):
          menu_state = random_game
                     
      if monster_sprite.health <= 0:
          menu_state = "final_boss"
          final_boss = True
             
        
        
  elif menu_state == "final_boss":       #final boss
    if final_boss:
       monster_sprite.health = 100
       monster_health = 0
       final_boss = False
    
    if health_bar.draw(screen,monster_health,monster_sprite.health):
         monster_health += 1
         print("monster_sprite:",monster_sprite.health)
         print("monster_health:",monster_health)

    if health_bar.draw(screen,monster_health,monster_sprite.health) == False:
         monster_health -= 1
         print("monster_sprite:",monster_sprite.health)
         print("monster_health:",monster_health)
    
    if monster_health == 0:
       menu_state = "game_over"
    TimeText = textobject.Text(640,100,32,(196, 43, 43),f'{round(time,1)}',screen)
    TimeText.draw()
    time-=1/60
     
      
  elif menu_state == "game_over":         #gameover
     game_over_sprite.draw(screen)
     if exit_button1.draw(screen):
        run = False
  
  elif menu_state == "RPS":               #Rock Paper Scissors
      TimeText = textobject.Text(640,100,32,(196, 43, 43),f'{round(time,1)}',screen)
      TimeText.draw()
      time-=1/60
      
      Result = textobject.Text(640,150,32,(196, 43, 43),f'{rpsgame.win} - {rpsgame.lose}',screen)
      Result.draw()
      
      RoundCount = textobject.Text(640,475,32,(250, 250, 250),f'Round {rpsgame.win + rpsgame.lose} / 3',screen)
      RoundCount.draw()
      
      player_choice_button = button.Button((SCREEN_WIDTH // 2)-450, 350, playerpick, 0.5)
      screen.blit(player_choice_button.image , player_choice_button.rect.topleft)
      
      if time<=0:
        menu_state = "game_over"
      
      player_sprite.draw(screen)
      monster_sprite.draw(screen)
  
      #Rock Paper Scissors!!!!!
      if rock_button.draw(screen):
        rpsgame.play("Rock")
        playerpick = rock_img
        
      if paper_button.draw(screen):
        rpsgame.play("Paper")
        playerpick = paper_img
        
      if scissors_button.draw(screen):
        rpsgame.play("Scissors")
        playerpick = scissors_img
      
      if rpsgame.wincheck():
        monster_sprite.receive_damage()
        menu_state = "main_game"
        rpsgame.victory = False
        
      if rpsgame.lostcheck():
        menu_state = "main_game"
        rpsgame.defeat = False 
        time-=15
        

  elif menu_state == "black_jack":            #BlackJack
    TimeText = textobject.Text(640,100,32,(196, 43, 43),f'{round(time,1)}',screen)
    TimeText.draw()
    time-=1/60
    if not(bjvalid):
      bj = Black_jack(screen)
      bjvalid = True

    bj.draw_all()
    
    if check == False:
      
      if draw_button.draw(screen):
         
         bj.player_draw()
         
         if bj.end_check_win() == 0:
            
            check = True
         
         else:
            
            bj.show = False
      
      if stay_button.draw(screen) :
        print(bj.end_check_win())

        if bj.end_check_win() == 0:
          print("Lose")
          monster_sprite.receive_health()

        if bj.end_check_win() == 1:
          print("win")
          monster_sprite.receive_damage()
          
        if bj.end_check_win() == 2:
          print("tie")
        check = True
    
    if check :
       if exit_button2.draw(screen):
         menu_state = "main_game"
         bj.reset()
         bj = Black_jack(screen)
         #print(monster_sprite.health)
         check = False
  elif menu_state == "black_jack_result":
     bj.draw_all()
  
  
  
  #event handler
  for event in pygame.event.get():
    
    if event.type == pygame.QUIT:
      run = False
    elif event.type == pygame.KEYDOWN:
       if menu_state == "final_boss":
        if event.key == pygame.K_SPACE:
          monster_sprite.receive_damage(random_damage)
        if time <= 0 :
          menu_state = "game_over"  
  pygame.display.update()
  clock.tick(FPS)
  
pygame.quit()
