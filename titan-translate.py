from subprocess import Popen, PIPE

pipe = Popen('tesseract image.png stdout', shell=True, stdout=PIPE).stdout
output = pipe.read().decode("utf-8").strip()

print()
print(output)
