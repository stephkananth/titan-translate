# Titan Translate
Website: https://stephkananth.github.io/titan-translate/

Writeup:

    What did you do?
    We made a python program that captures an image of text in any language and translates it to English. The program then      
    displays the captured image overlaid with the translated text. When the user runs the program, a window of their camera is 
    opened, and the user can press the spacebar to capture an image of text in any language and save it to the program 
    directory. When the user presses the spacebar, the camera window is closed, but then the image is opened with the 
    translated text displayed on it.
    
    How and why did it work?
    The program uses OpenCV to access their camera and capture the image, a module called Tesseract to turn the image of text 
    into a string, and Google Translate to determine the language of the original text (stored in a string) and translate it to 
    English. OpenCV was also used to display the translated text onto the captured image. It worked because we were able to 
    bring these three different modules together into one program. We drew from each of their strengths to seamlessly combine 
    them to make a program that is greater than the simple sum of their parts, a program that could potentially be very helpful 
    and useful.

    What didn't work and why?
    We also attempted to have the program speak the translated text using Google Text to Speech
    (https://pypi.python.org/pypi/gTTS), which would save the speech as an mp3 and then play it back for the user while the 
    translated text was being displayed, but it unreliable and only worked sporadically, so we decided that it was not critical 
    to the program and reverted back to a more reliable version of the program.

Sources:

OpenCV: https://opencv-python-tutroals.readthedocs.io/en/latest/

Tesseract: https://github.com/tesseract-ocr/tesseract

Google Translate: https://pypi.python.org/pypi/googletrans
