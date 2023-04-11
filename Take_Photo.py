import datetime
import cv2

url = "rtsp://admin:10DmKCFm@11.0.1.6:554/Streaming/Channels/101"
capture = cv2.VideoCapture(url)

# настройка размерка изображений
capture.set(3, 1080)
capture.set(4, 720)

while True:
    ret, frame = capture.read()
    # выводит видео-картинку на экран
    cv2.imshow('frame', frame)
    # при нажатии "q" выходим - прерываем работу скрипта
    key = cv2.waitKey(1)
    if key == ord('q'):
        print("programm was broken")
        break
    # сохраняем фото только при нажатии клавиши "s"
    if key == ord('s'):
        print("taking photo..")
        now = datetime.datetime.now()
        img_name = "./photo/{}_opencv_frame_{}.jpg".format('11.0.1.6', now.strftime("%Y%m%d%H%M%S"))
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))

capture.release()
cv2.destroyAllWindows()
