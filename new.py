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


print("HERE")
print(output)

translator = Translator()
print(translator.translate(output))
print(type(translator.translate(output)))