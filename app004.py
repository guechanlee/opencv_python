import cv2
import numpy as np
'''
## 원 생성
circleBG = np.zeros((480, 640, 3), dtype=np.uint8)
COLOR = (255 ,255, 0)   # 색상
RADIUS = 100            # 반지름
THINKNESS = 3           # 테두리 선 두께

cv2.circle(circleBG,        (150, 150), RADIUS, COLOR, THINKNESS, cv2.LINE_AA)
#          어디에 그릴거니?    중심점       반지름   색상      두께       선의 타입
# 
cv2.circle(circleBG,        (450, 450), RADIUS, COLOR, cv2.FILLED, cv2.LINE_AA)

cv2.imshow('title-circle', circleBG)
cv2.waitKey(0) 
cv2.destroyAllWindows()
'''
'''
## 사각형 그리기
rectangleBG = np.zeros((480, 640, 3), dtype=np.uint8)
COLOR = (255 ,255, 0)   # 색상
THINKNESS = 3           # 테두리 선 두께

cv2.rectangle(rectangleBG,   (50, 100),(200, 200), COLOR, THINKNESS, cv2.LINE_AA)
#          어디에 그릴거니?    중심점         색상      두께       선의 타입
# 
# cv2.rectangle(rectangleBG, (300, 100), (500, 300), COLOR, cv2.FILLED, cv2.LINE_AA)

cv2.imshow('title-rectangle', rectangleBG)
cv2.waitKey(0) 
cv2.destroyAllWindows()
'''
'''
## 다각형 그리기
polygonBG = np.zeros((480, 640, 3), dtype=np.uint8)

COLOR = (255, 255, 0)   # 색상
THINKENESS = 3          # 두께

points01 = np.array([
    [50, 50],
    [150, 150],
    [50, 150],
])

points02 = np.array([
    [250, 50],
    [350, 150],
    [250, 150],
])

cv2.polylines(polygonBG,  [points01, points02],         True,              COLOR, THINKENESS, cv2.LINE_AA)
#            어디에 그릴지?  어떤녀석 그릴거야? 닫힌도형 or 열린도형    색상      두께      선의 타입

cv2.imshow('title-polygonBG', polygonBG)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
'''
## 이미지 복사 & 저장
robotImgGrayscale = cv2.imread('./res/img/robot.jpg', cv2.IMREAD_GRAYSCALE)
robotImgGrayscale = cv2.resize(robotImgGrayscale, (800, 575))

cv2.imshow('title-robotImgGrayscale', robotImgGrayscale)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('./save/img/robot_grascale.jpg', robotImgGrayscale)
'''
'''
# 간단하게 저장 하는 법
robotImgGrayscale = cv2.imread('./res/img/robot.jpg', cv2.IMREAD_GRAYSCALE)
robotImgGrayscale = cv2.resize(robotImgGrayscale, (800, 575))
result = cv2.imwrite('./save/img/robot_grascale.jpg', robotImgGrayscale)
print(f'result: {result}')  # 불리언 타입
'''

## 동영상 복사 저장
robotMOV = cv2.VideoCapture('./res/mov/robot.mp4') # 동영상 파일 읽기

# 코덱 정의
# cv2.VideoWriter_fourcc('D', 'I', 'V', 'X')
fourcc = cv2.VideoWriter_fourcc(*'DIVX') # 'D', 'I', 'V', 'X'

width = int(robotMOV.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(robotMOV.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = robotMOV.get(cv2.CAP_PROP_FPS)

robotMovOutput = cv2.VideoWriter('./save/mov/robotMov-output.mp4', fourcc, fps, (width, height))

while robotMOV.isOpened:
    result, frame = robotMOV.read()     # 프레임 1개 읽는다.
    if not result:
        print('MOVIE END!')
        break
    
    robotMovOutput.write(frame)

    frame = cv2.resize(frame, (600, 600))
    cv2.imshow('title-robotMOV', frame)


    if cv2.waitKey(1) == ord('q'):
        print('MOVIE END!')
        break

robotMOV.release()
cv2.destroyAllWindows()
