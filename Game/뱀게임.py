    #모든 줄에 주석 젛기
#1. 게임에 필요한 라이브러리를 import
#2. 게임에 필요한 기본설정

import pygame #파이게임 파일 불러오기
from pygame.locals import QUIT, Rect, KEYDOWN, K_UP, K_LEFT, K_RIGHT, K_DOWN
                            #종료, 그리기, 키 눌렀을떄, 위키, 왼쪽키, 오른쪽키, 아래키
import random #랜덤 파일 불러오기
import sys # 시스템 파일 불러오기

# 2. 게임에 필요한 기본설정
pygame.init() # 파이게임 초기값
화면 = pygame.display.set_mode( (1000, 1000) ) # 화면 구성
프레임 = pygame.time.Clock() # 프레임에 파이게임 시간 설정
# Frame per Second : FPS : 초당 프레임[정지사진] 수
음식 = [ ] # 여러개 음식을 저장할 리스트
뱀 = [ ] # 여러개 뱀 꼬리를 저장할 리스트
(가로, 세로) = (50, 50) # 가로길이 세로길이

    # 배경넣기
배경 = pygame.image.load("숲 사진.jfif")

pygame.mixer.music.load("nightlife-michael-kobrin-95bpm-3783 (1).mp3")
pygame.mixer.music.play(-1)
# 3. 함수 만들기
    # 1. 음식 함수 2. 음식 이름 3. 그리기 함수
        #1. 음식 함수 : 뱀이 음식을 먹었을 떄 새로운 음식 추가
my글꼴 = pygame.font.SysFont("malgungothic", 30)
점수 = 0
def 음식생성():
    while True:
        위치 = ( random.randint(0, 가로-1), random.randint(0, 세로-1))
                        #0부터 49까지의 난수 생성
        if 위치 in 음식 or 위치 in 뱀 : # 해당 위치에 음식이나 뱀이 있으면
            continue # while 다시 실행
        else:
            음식.append(위치) # 음식리스트에 해당 위치 추가
            break
        #2. 음식 이동 함수 : 뱀이 음식을 먹었을 때
def 음식이동(위치): # 음식을 다른 위치로 이동
    임의변수 = 음식.index(위치) # 해당 위치에 음식 찾기
    del 음식[임의변수] # 해당 위치에 음식삭제
    음식생성() # 음식생성 함수 호출 [ 새로운 음식 생성]

        #3. 그리기()
def 그리기(점수판):
    화면.fill((0, 0, 0)) # 검정색으로 정하기

    #음식 그리기
    for food in 음식:
        pygame.draw.ellipse( 화면, (0, 255, 0), Rect(food[0]*20,food[1]*20, 20, 20))
    #뱀 그리기
    for body in 뱀:
        pygame.draw.rect(화면, (0, 255, 200), Rect(body[0]*20, body[1] * 20, 20, 20))

    if 점수판 != None:  # 정수에 내용이 있으면
        화면.blit(점수판, (10, 10))

    pygame.display.update() # 화면 업데이트




#4. 게임실행

키 = K_DOWN # 아래키
게임종료 = False # 게임종료 스위치
뱀.append( (int(세로/2), int(가로/2)))
for i in range(30):
    음식생성()

while True:
    화면.blit(배경, (0, 0))
    for 동작 in pygame.event.get():
        if 동작.type == QUIT :
            pygame.quit()
            sys.exit()
        elif 동작.type == KEYDOWN:#키를 눌렀을 때
            키 = 동작.key

    #키를 눌렀을 때 대한 액션
    if not 게임종료 : #게임종료가 false 이면
        if 키 == K_LEFT:
            머리 = (뱀[0][0]-1, 뱀[0][1])
        elif 키 == K_RIGHT:
            머리 = (뱀[0][0] +1, 뱀[0][1])
        elif 키 == K_DOWN:
            머리 = (뱀[0][0] , 뱀[0][1]+1)
        elif 키 == K_UP:
            머리 = (뱀[0][0] , 뱀[0][1]-1)

        if 머리 in 뱀 or 머리[0] < 0 or 머리[0] > 세로 or 머리[0] > 가로 :

            게임종료 = True
        #뱀 머리 추가
        뱀.insert(0, 머리)
        if 머리 in 음식:
            음식이동(머리)
            점수 += 1
            if 점수 == 점수+10:
                점수 = 점수+10


        else:
            뱀.pop() # 가장 뒤에있는 항목 제거



        점수판 = my글꼴.render("현재 먹은 횟수 "+str(점수), True,(255,255,0))


    그리기(점수판)
    프레임.tick(5)
