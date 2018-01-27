import cv2
import unicodedata
cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0

while True:
    ret, frame = cam.read()
    cv2.imshow("test", frame)
    if not ret:
        break
    k = cv2.waitKey(1)

    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "opencv_frame.png"
        cv2.imwrite(img_name, frame)
        print("written!".format(img_name))
        img_counter += 1


cam.release()

cv2.destroyAllWindows()

#TitanTranslateFile
from subprocess import Popen, PIPE
from googletrans import Translator


def ignoreError(s):
    if isinstance(s, str):
        return (unicodedata.normalize('NFKD', s).encode('ASCII', 'ignore').decode('utf-8', 'ignore'))
    return s

pipe = Popen('tesseract opencv_frame.png stdout', shell=True, stdout=PIPE).stdout
output = ignoreError(pipe.read().decode("utf-8").strip())

translator = Translator()
<<<<<<< HEAD
print(translator.translate(output))
print(type(translator.translate(output)))


#Adding text to image and pulling it up
import numpy as np
img = cv2.imread('opencv_frame.png',cv2.IMREAD_COLOR)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Testing testing testing',(40,130), font, 1, (225,255,225), 2, cv2.LINE_AA)


cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
=======
print(translator.translate(output).text)
>>>>>>> 892722eeb2f13df8019a5f5c4a87e820ef54ce4e
