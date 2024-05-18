# (퀴즈) 하늘에서 똥피하기 

# [게임조건]

# 1. 캐릭터는 화면 가장 아래에 위치, 좌우만 이동가능
# 2. 똥은 화면 가장 위에서 떨어짐, x좌표는 매번 랜덤으로 설정
# 3. 캐릭터가 똥을 피하면 다음 똥이 다시 떨어짐
# 4. 캐릭터가 똥과 충돌하면 게임 종료
# 5. fps는 30으로 고정

# [게임 이미지]
# 1. 배경 : 640 * 480 (세로,가로) backgroup.png
# 2. 캐릭터 : 70 * 70 character.png
# 3. 똥 : 70 * 70 enemy.png


import pygame
import random

############################################################################################################3
#### (0) 기본 초기화 부분(반드시 해야되는 것들) - 화면크기, 타이틀, fps, 
pygame.init() # 1. 초기화(반드시 필요)
# 1. 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 1. 화면 타이틀 설정
pygame.display.set_caption("이현이 피하기 게임") # 게임 이름 이름에도 ""필요

# 5. fps   초당 프레임수
clock = pygame.time.Clock()


############################################################################################################3
#### (1) 사용자 게임 초기화  - 배경, 캐릭터 , 이동변수, 이동속도, 적이미지, 폰트, 시간, 시작시간 등

# 2. 배경 이미지 불러오기 (불러오고 나서 나중에 표출은 이벤트 루프 포문 밖에서 처리 스크린 블릿)
background = pygame.image.load("/Users/hyb/Downloads/pygame/background.png")  #경로는 "" 필요

# 3. 캐릭터(스프라이트) 불러오기
character = pygame.image.load("/Users/hyb/Downloads/pygame/character.png")  #경로는 "" 필요
character_size = character.get_rect().size #3. 이미지의 크기를 구해온다
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

# 4. 이동할 좌표 변수(캐릭터)
to_x_pos = 0
# to_y_pos = 0

#5. 이동 속도
character_speed = 0.7

# 6. 적(enemy) 불러오기
enemy = pygame.image.load("/Users/hyb/Downloads/pygame/enemy.png")  #경로는 "" 필요
enemy_size = enemy.get_rect().size #3. 이미지의 크기를 구해온다
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = random.randint(0,screen_width-enemy_width)
enemy_y_pos = 0

# 이동할 좌표 변수(적)
to_y_pos = 0.3

# 7. 폰트정의
game_font = pygame.font.SysFont("applegothic", 20)  #7. 폰트 객체 생성 (폰트종류, 크기)
print(pygame.font.get_fonts())

# 7. 총 시간
total_time = 60

# 7. 시작 시간정보 
start_ticks = pygame.time.get_ticks()

# 점수 변수
total_score = 0


# 1. 이벤트 루프
running = True
while running:  # 1. : 붙이는 경우 알아보기
    dt = clock.tick(60)  # 5. 프레임에 따른 보정값 ()안에 값은 프레임수
    
    #print("fps : "+str(clock.get_fps()))  #5. 프레임수 확인
    #print("dt : "+ str(dt))               #5. 보정값 확인

    # 5. 캐릭터가 1초에 100만큼 이동
    # 5. 10fps : 1초에 10번 동작 - > 1번에 몇만큼 이동? 10만큼 이동
    # 5. 20fps : 1초에 20번 동작 - > 1번에 몇만큼 이동? 5만큼 이동
    # 5. 프레임이 달라진다고 게임의 이동속도가 달라지면 안됨

############################################################################################################3
#### (2) 이벤트 처리(키보드 마우스 등)

    for event in pygame.event.get(): # 1. 어떤 이벤트가 발생하는가?            # : 붙이는 경우 알아보기
        if event.type == pygame.QUIT: # 1. 창이 닫히는 이벤트가 발생하였는가?       # : 붙이는 경우 알아보기
            running = False # 1. 게임이 진행중이 아님
        
        if event.type == pygame.KEYDOWN: # 4. 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:   # 4. 캐릭터를 왼쪽으로
                to_x_pos -= character_speed  # to_x_pos = to_x_pos - 5
            if event.key == pygame.K_RIGHT:  # 4. 캐릭터를 오른쪽으로
                to_x_pos += character_speed
            # if event.key == pygame.K_UP:   # 4. 캐릭터를 위쪽으로
            #     to_y_pos -= 0
            # if event.key == pygame.K_DOWN:   # 4. 캐릭터를 아래쪽으로
            #     to_y_pos += 0

        if event.type == pygame.KEYUP:   # 4. 방향키가 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:  # 4. 가로방향 누르고 떼는경우
                to_x_pos = 0
            # if event.key == pygame.K_UP or event.key == pygame.K_DOWN:  # 4. 세로방향 누르고 떼는경우
            #     to_y_pos = 0
    
############################################################################################################3
#### (3) 게임캐릭터 위치정의 - 캐릭터 위치갱신, 경계값 등
        
    character_x_pos += to_x_pos * dt #4. 캐릭터 위치 갱신 이벤트에 따른  #5. dt곱해서 이동속도를 프레임에 따라 일정하게
    # character_y_pos += to_y_pos * dt #4. 캐릭터 위치 갱신 이벤트에 따른  #5. dt곱해서 이동속도를 프레임에 따라 일정하게
    
    enemy_y_pos += to_y_pos * dt #4. 캐릭터 위치 갱신 이벤트에 따른  #5. dt곱해서 이동속도를 프레임에 따라 일정하게
    # character_y_pos += to_y_pos * dt #4. 캐릭터 위치 갱신 이벤트에 따른  #5. dt곱해서 이동속도를 프레임에 따라 일정하게


    # 4. IF문 과 동일 레벨이면 한번 누르면 끝난다 이유가 뭘까?  

    # 4. 가로경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    if character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    # 4. 세로 경계값 처리
    # if character_y_pos < 0:
    #     character_y_pos = 0
    # if character_y_pos > screen_height - character_height:
    #     character_y_pos = screen_height - character_height
    if enemy_y_pos > screen_height:
        enemy_x_pos = random.randint(0,screen_width-enemy_width)
        enemy_y_pos = 0
        to_y_pos += 0.01
        total_score += 10
############################################################################################################3
#### (4) 충돌처리

    # 6. 충돌처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 6. 충돌체크
    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running = False


############################################################################################################3
#### (5) 화면에 그리기
    
    # 화면에 표출하기
    #screen.fill((0,225,0))  # 직접 rgb로 채울수도 있다
    screen.blit(background, (0, 0)) # 2. 배경 그리기(표출) , 0,0부터 크기만큼 채워진다
    screen.blit(character, (character_x_pos, character_y_pos))  # 3. 캐릭터 표출 , 0,0부터 크기만큼 채워진다
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) #6. 적 표출

    # 7. 타이머 집어넣기
    # 7. 경과시간 계산
    elasped_time = (pygame.time.get_ticks() - start_ticks) / 1000 # 경과시간(ms)를 1000으로 나누어 초단위(s)로 표시

    timer = game_font.render(str(int(total_time - elasped_time)), True, (0, 0, 0)) #7. 정의된 폰트 변수로 렌더(그림)
     # 7. render ( 입력내용, 안티알리아스 트루, 글자색상)
    screen.blit(timer, (10, 10))
    #7. 타이머 변수 위치가 스크린 앞에 있으면 표출이 안되는 이유? ##
    score = game_font.render("점수 : "+str(total_score)+"점", True, (0, 0, 0))
    screen.blit(score, (screen_width-150, 20))

    #7. 만약 시간이 0 이하이면 게임종료
    if total_time - elasped_time <= 0 :
        print("타임아웃")
        running = False



    pygame.display.update()  #2. 게임화면을 다시 그리기  -> 와일문이 한번 돌떄마다 계속 업데이트를 해줘야댐

# 7. 종료 전 잠시대기 
pygame.time.delay(2000) # 2초정도 대기

# 1. pygame 종료
pygame.quit()

