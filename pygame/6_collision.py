import pygame

pygame.init() # 1. 초기화(반드시 필요)

# 1. 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 1. 화면 타이틀 설정
pygame.display.set_caption("Nado game") # 게임 이름 이름에도 ""필요

# 5. fps   초당 프레임수
clock = pygame.time.Clock()

# 2. 배경 이미지 불러오기 (불러오고 나서 나중에 표출은 이벤트 루프 포문 밖에서 처리 스크린 블릿)
background = pygame.image.load("C:/Users/cicin/OneDrive/Desktop/phythonworkspace/pygame_biasc/background.png")  #경로는 "" 필요

# 3. 캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:/Users/cicin/OneDrive/Desktop/phythonworkspace/pygame_biasc/character.png")  #경로는 "" 필요
character_size = character.get_rect().size #3. 이미지의 크기를 구해온다
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

# 4. 이동할 좌표 변수
to_x_pos = 0
to_y_pos = 0

#5. 이동 속도
character_speed = 0.3

# 6. 적(enemy) 불러오기
enemy = pygame.image.load("C:/Users/cicin/OneDrive/Desktop/phythonworkspace/pygame_biasc/enemy.png")  #경로는 "" 필요
enemy_size = enemy.get_rect().size #3. 이미지의 크기를 구해온다
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = (screen_width / 2) - (enemy_width / 2)
enemy_y_pos = (screen_height / 2) - (enemy_height / 2)



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


    for event in pygame.event.get(): # 1. 어떤 이벤트가 발생하는가?            # : 붙이는 경우 알아보기
        if event.type == pygame.QUIT: # 1. 창이 닫히는 이벤트가 발생하였는가?       # : 붙이는 경우 알아보기
            running = False # 1. 게임이 진행중이 아님
        
        if event.type == pygame.KEYDOWN: # 4. 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:   # 4. 캐릭터를 왼쪽으로
                to_x_pos -= character_speed  # to_x_pos = to_x_pos - 5
            if event.key == pygame.K_RIGHT:  # 4. 캐릭터를 오른쪽으로
                to_x_pos += character_speed
            if event.key == pygame.K_UP:   # 4. 캐릭터를 위쪽으로
                to_y_pos -= character_speed
            if event.key == pygame.K_DOWN:   # 4. 캐릭터를 아래쪽으로
                to_y_pos += character_speed

        if event.type == pygame.KEYUP:   # 4. 방향키가 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:  # 4. 가로방향 누르고 떼는경우
                to_x_pos = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:  # 4. 세로방향 누르고 떼는경우
                to_y_pos = 0
        
    character_x_pos += to_x_pos * dt #4. 캐릭터 위치 갱신 이벤트에 따른  #5. dt곱해서 이동속도를 프레임에 따라 일정하게
    character_y_pos += to_y_pos * dt #4. 캐릭터 위치 갱신 이벤트에 따른  #5. dt곱해서 이동속도를 프레임에 따라 일정하게
    # 4. IF문 과 동일 레벨이면 한번 누르면 끝난다 이유가 뭘까?  

    # 4. 가로경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    if character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    # 4. 세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    if character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height
    
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
        
    
    # 화면에 표출하기
    #screen.fill((0,225,0))  # 직접 rgb로 채울수도 있다
    screen.blit(background, (0, 0)) # 2. 배경 그리기(표출) , 0,0부터 크기만큼 채워진다
    screen.blit(character, (character_x_pos, character_y_pos))  # 3. 캐릭터 표출 , 0,0부터 크기만큼 채워진다
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) 
    pygame.display.update()  #2. 게임화면을 다시 그리기  -> 와일문이 한번 돌떄마다 계속 업데이트를 해줘야댐

# 1. pygame 종료
pygame.quit