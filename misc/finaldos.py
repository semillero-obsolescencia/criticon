import sys
import pyttsx
habla = None
x = None
uno = "esteestexto.txt"
dos = "esteotro.txt"
tres = "yotro.txt"
buscando = "buscando.txt"



def espeak():
    print 'running speech-test.py...'
    engine = pyttsx.init()
    engine.setProperty("rate",40)
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[19].id)
    with open (habla)as f:
      lines = f.readlines()
    engine.say(lines)
    engine.runAndWait()

while x != "no":
  print 'cmd para elegir archivo...'
  x = raw_input()
  if x == "uno":
    habla = uno
    print habla
    espeak()
  elif x == "dos":
    habla = dos 
    print habla
    espeak()
  elif x == "tres":
    habla = tres
    print habla
    espeak()
  else:
    habla = buscando
    print habla
    espeak()

  



