import cv2
import numpy as np

## 스케치북 생성
# 세로(480) 가로(640) 3채널(BGR)
'''
sketchbookImg = np.zeros((480, 640, 3), dtype=np.uint8)
cv2.imshow('title-sketchbookImg', sketchbookImg)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

# 흰색 스케치북
# sketchbookImg = np.zeros((480, 640, 3), dtype=np.uint8)
# sketchbookImg[:] = (255, 255, 255)    # B  G  R  -> 0 ~ 255
# cv2.imshow('title-sketchbookImg', sketchbookImg)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
'''
## 특정 영역 색칠 하기
sketchbookImg = np.zeros((480, 640, 3), dtype=np.uint8)
sketchbookImg[:] = (0, 0, 0)    # B  G  R  -> 0 ~ 255

sketchbookImg[100:200, 300:400] = (255,255,255)
            # 세로:세로  가로:가로
sketchbookImg[300:400, 100:200] = (0,255, 255)
            # 세로:세로  가로:가로

cv2.imshow('title-sketchbookImg', sketchbookImg)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

## 직선 만들기
sketchbookImg = np.zeros((480, 640, 3), dtype=np.uint8)
sketchbookImg[:] = (0, 0, 0)    # B  G  R  -> 0 ~ 255

COLOR_4 = (0, 0, 255) # Red
COLOR_8 = (0, 255, 0) # GREEN
COLOR_AA = (255, 0, 0) # BLUE
THINKNESS = 3   # 두께

cv2.line(sketchbookImg, (10, 10), (400, 400), COLOR_4, THINKNESS, cv2.LINE_4 )
#        어디에 만들거니   시작점     끝점        색상      두께        라인타입

cv2.line(sketchbookImg, (10, 10), (500, 400), COLOR_8, THINKNESS, cv2.LINE_8)
cv2.line(sketchbookImg, (10, 10), (600, 400), COLOR_AA, THINKNESS, cv2.LINE_AA)

cv2.imshow('title-sketchbookImg', sketchbookImg)
cv2.waitKey(0)
cv2.destroyAllWindows()