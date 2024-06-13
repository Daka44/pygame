import pygame, sys, time, os, random
from pygame.locals import *

current_directory = os.getcwd()
print("현재 작업 디렉토리:", current_directory)

FPS = 60
MAX_WIDTH = 400
MAX_HEIGHT = 600

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((MAX_WIDTH,MAX_HEIGHT))
score = 0
game_over=False
# path = "E:\프로그래밍\dist"
bg_path = os.path.join("image", "background.png")
# bg_path = os.path.join(current_directory, bg_path)
background_image = pygame.image.load("class\파이썬\프로젝트\파이게임\image\background.png").convert()



class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def draw(self):
        return pygame.draw.rect(screen, (0,0,255), (self.x, self.y, 40, 40))
    def move(self):
        if pressed_keys[K_RIGHT]:
            if self.x < MAX_WIDTH-40:
                self.x += 5
        if pressed_keys[K_LEFT]:
            if self.x > 0:
                self.x -= 5


enemy_path = os.path.join("image", "똥.png")
enemy_path = os.path.join(current_directory, enemy_path)

class Enemy:
    def __init__(self):
        self.x = random.randrange(0, MAX_WIDTH-40)
        self.y = 50
        self.speed = random.randrange(10, 15)
        self.enemy = pygame.image.load(enemy_path)
        self.enemy = pygame.transform.scale(self.enemy,(40,40))

    def draw(self):
        return screen.blit(self.enemy, (self.x, self.y))

    def draw2(self, image):
        return screen.blit(image, (self.x, self.y))    

    def move(self):
        global score 
        self.y = self.y + self.speed
        if self.y >= MAX_HEIGHT:
            score+=1    
            self.y = 50
            self.x = random.randrange(0, MAX_WIDTH-40)
            self.speed = random.randrange(7, 15)

class Button:
    def __init__(self, x, y, width, height, text, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)
        text_surface = font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_clicked(self,p):
        global game_over
        if self.rect.collidepoint(p):    
            game_over = False

player = Player(MAX_WIDTH/2, MAX_HEIGHT - 40)
enemies = []
lives = 3
# heart = Heart()
for _ in range(6):
    enemy = Enemy()
    enemies.append(enemy)

game_over_path = os.path.join("image", "game_over.ttf")
game_over_path = os.path.join(current_directory, game_over_path)

font = pygame.font.Font(game_over_path, 55)
button = Button(MAX_WIDTH // 2-42, MAX_HEIGHT // 2 +30, 80 , 40, "restart" , (0,0,0))
button2 = Button(MAX_WIDTH // 2-42, MAX_HEIGHT // 2 +30, 80 , 40, "GO" , (0,0,0))
def start():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                if button2.rect.collidepoint(event.pos):
                    score = 0
                    player.x, player.y = MAX_WIDTH/2, MAX_HEIGHT - 40
                    for enemy in enemies:
                        enemy.y = 50  
                    for i in range(3, 0, -1):
                        screen.fill((255, 255, 255))#화면을 흰색으로 채                       
                        count=font.render(str(i), True, (0, 0, 0)) 
                        screen.blit(count, (MAX_WIDTH // 2 - 10, MAX_HEIGHT // 2 + 50))
                        pygame.display.update()
                        time.sleep(1)
                    return False
        screen.fill((255, 255, 255))
        text1 = font.render("START", True, (0, 0, 0))
        screen.blit(text1, (MAX_WIDTH // 2 - 40, MAX_HEIGHT // 2 - 20))
        button2.draw()
        pygame.display.update()



def restart():
    global score
    try:
        with open('score', 'a') as f:
            f.write(str(score) + '\n') 
    except FileNotFoundError:
        with open('score', 'w') as f:
            f.write("0" + '\n')
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                if button.rect.collidepoint(event.pos):  
                    score = 0
                    player.x, player.y = MAX_WIDTH/2, MAX_HEIGHT - 40
                    for enemy in enemies:
                        enemy.y = 50
                    for i in range(5, 0, -1):
                        screen.fill((255, 255, 255))#화면을 흰색으로 채움
                        screen.blit(text1, (MAX_WIDTH // 2 - 70, MAX_HEIGHT // 2 - 20))
                        screen.blit(score_text, (MAX_WIDTH // 2 - 10, MAX_HEIGHT // 2 ))
                        count=font.render(str(i), True, (0, 0, 0)) 
                        screen.blit(count, (MAX_WIDTH // 2 - 10, MAX_HEIGHT // 2 + 50))
                        pygame.display.update()
                        time.sleep(1)
                    print("재시작")
                    return False

        screen.fill((255, 255, 255))#화면을 흰색으로 채움
        text1 = font.render("Game Over", True, (0, 0, 0))
        numbers = []
        with open('score', 'r') as f:
            for line in f:
                line = line.strip()
                if line.isdigit():
                    number = int(line)
                    numbers.append(number)
        max_value = max(numbers)
        best_score = font.render("Best: " + str(max_value), True, (0, 0, 0))
        score_text=font.render(str(score), True, (0, 0, 0))
        screen.blit(best_score, (MAX_WIDTH - 100, 10))
        screen.blit(text1, (MAX_WIDTH // 2 - 55, MAX_HEIGHT // 2 - 20))
        screen.blit(score_text, (MAX_WIDTH // 2 - 10, MAX_HEIGHT // 2 ))        
        button.draw()
        pygame.display.update()

def main():
    global score,lives, game_over,max_value,background_image 
    
    n=1
    nando = 15
    li = list(range(0,10000,nando))
    numbers = []
    with open('score', 'r') as f:
        for line in f:
            line = line.strip()
            if line.isdigit():
                number = int(line)
                numbers.append(number)
    max_value = max(numbers, default=0)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        clock.tick(FPS) 
        global pressed_keys        
        pressed_keys = pygame.key.get_pressed()
        
        if not game_over:
            
            screen.blit(background_image, (0,0))   
            player_rect = player.draw()
            player.move()
            
            if score in li and n <= 6:
                n+=1
                li.remove(score)
                
            for enemy in enemies[:n]:
                enemy_rect = enemy.draw()
                enemy.move()
                
                if player_rect.colliderect(enemy_rect): 
                                                        
                    game_over = restart()
                    n=1
                    li = list(range(0,10000,nando))
            
            
            # 왼쪽 상단 점수
            text_surface = font.render(str(score), True, (150,75,0))
            screen.blit(text_surface, (10, 10))
            # 오른쪽 상단 최고 점수
            with open('score', 'r') as f:
                for line in f:
                    line = line.strip()
                    if line.isdigit():
                        number = int(line)
                        numbers.append(number)
            max_value = max(numbers, default=0)
            best_score_text = font.render("Best: " + str(max_value), True, (0, 0, 0))
            screen.blit(best_score_text, (MAX_WIDTH - 100, 10))

            
        pygame.display.update()
    

if __name__ == '__main__':
    start()
    main()  # 게임 루프 시작
