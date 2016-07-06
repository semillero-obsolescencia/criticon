import sys
import pyttsx
import os, random
habla = None
x = None
rang = os.listdir("Angelica")
rdavid = os.listdir("David")
rcarla = os.listdir("Carla")

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
    uno = random.choice(rang)
    habla = "Angelica/" + uno
    print habla
    espeak()
  elif x == "dos":
    dos = random.choice(rdavid)
    habla = "David" + dos 
    print habla
    espeak()
  elif x == "tres":
    tres = random.choice(rcarla)
    habla = "Carla" + tres
    print habla
    espeak()
  else:
    habla = buscando
    print habla
    espeak()

  



