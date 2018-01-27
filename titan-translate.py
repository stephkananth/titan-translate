from subprocess import Popen, PIPE
from googletrans import Translator

pipe = Popen('tesseract image.png stdout', shell=True, stdout=PIPE).stdout
output = pipe.read().decode("utf-8").strip()

print()
print(output)

translator = Translator()
<<<<<<< HEAD
print(translator.translate(output).text)

=======
print(translator.translate(output))
print(type(translator.translate(output)))
>>>>>>> 51408fe21a6608e0227262b250abc3f779d9a894
