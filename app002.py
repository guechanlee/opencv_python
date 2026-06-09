# OpenCV 모듈 가져오기
import cv2

'''
# 버전 확인
print(cv2.__version__)  # 4.13.0

## 이미지 불러와서 출력하기 = (https://www.pexels.com/ko-kr/)
robotImg = cv2.imread('./res/img/robot.jpg')    # 이미지 읽기
print(f'robotImg shape: {robotImg.shape}')      # 이미지 크기 --> (3882(세로), 5815(가로), 3(BGR))
robotImg = cv2.resize(robotImg, (800, 600))     # 이미지 크기 변경 --> (가로, 세로),3))

cv2.imshow('title-robotImg', robotImg)          # 이미지 출력
cv2.waitKey(0)                                  # 어떤 키를 누룰때까지 기다려라
cv2.destroyAllWindows()                         # 모든 창 닫기
'''

# ## 읽기 옵션
# robotImgColor = cv2.imread('./res/img/robot.jpg', cv2.IMREAD_COLOR)      # BGR 유지
# robotImgColor = cv2.resize(robotImgColor, (800, 600))

# robotImgGray = cv2.imread('./res/img/robot.jpg', cv2.IMREAD_GRAYSCALE)   # GRAYSCALE
# robotImgGray = cv2.resize(robotImgGray, (800, 600))

# robotImgUnchanged = cv2.imread('./res/img/robot.jpg', cv2.IMREAD_UNCHANGED)   # ALPHA 유지
# robotImgUnchanged = cv2.resize(robotImgUnchanged, (800, 600))

# cv2.imshow('title-robotImgColor', robotImgColor)
# cv2.imshow('title-robotImgGray', robotImgGray)
# cv2.imshow('title-robotImgUnchanged', robotImgUnchanged)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

## 동영상 불러와서 출력하기 (https://www.pexels.com/ko-kr/)
# OpenCV에서 동영상을 불러온다는 것은 '동영상 -> 프레임(frame) 추출 -> 이미지화 -> 출력'
'''
robotMov = cv2.VideoCapture('./res/mov/robot.mp4')
while robotMov.isOpened(): # 동영상 파일이 연결되어 있다면...
    result, frame = robotMov.read()     # result: read 성공 여부, frame: 받아온 이미지(프레임)
    if not result:
        print('END FRAME')
        break

    frame = cv2.resize(frame, (800, 600))

    print(f'frame: {frame}')
    cv2.imshow('title-robotFrame', frame)       # 매우 빠르게 frame(이미지)가 출력된다.

    if cv2.waitKey(1) == ord('q'):      # 1ms 동안 기다린다. 사용자가 'q'를 입력하면 중단한다.
        break

robotMov.release()        # 외부 자원 해제
cv2.destroyAllWindows()   # 윈도우 창 닫기
'''

# 캠에서 동영상 실시간으로 불러오기
robotMov = cv2.VideoCapture(0)
while robotMov.isOpened(): # 동영상 파일이 연결되어 있다면...
    result, frame = robotMov.read()     # result: read 성공 여부, frame: 받아온 이미지(프레임)
    if not result:
        print('END FRAME')
        break

    frame = cv2.resize(frame, (800, 600))

    print(f'frame: {frame}')
    cv2.imshow('title-robotFrame', frame)       # 매우 빠르게 frame(이미지)가 출력된다.

    if cv2.waitKey(1) == ord('q'):      # 1ms 동안 기다린다. 사용자가 'q'를 입력하면 중단한다. # 재생속도 컨트롤 기능
        break

robotMov.release()        # 외부 자원 해제
cv2.destroyAllWindows()   # 윈도우 창 닫기