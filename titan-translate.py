from subprocess import Popen, PIPE
from googletrans import Translator

pipe = Popen('tesseract image.png stdout', shell=True, stdout=PIPE).stdout
output = pipe.read().decode("utf-8").strip()

print()
print(output)

translator = Translator()
print(translator.translate(output))
print(type(translator.translate(output)))


