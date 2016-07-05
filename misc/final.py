import sys
import pyttsx
habla = None
uno = "esteestexto.txt"
dos = "esteotro.txt"
tres = "yotro.txt"
buscando = "buscando.txt"
x = buscando

def main():

    print 'cmd para elergir archivo...'
    while x == raw_input():
      if x == "uno":
          habla = uno
          print x
      elif x == "dos":
          habla = dos 
          print x
      elif x == "tres":
          habla = tres
          print x
      else:
          habla = buscando
      print 'running speech-test.py...'
      engine = pyttsx.init()
      with open (habla)as f:
          lines = f.readlines()
      engine.say(lines)
      engine.runAndWait()


if __name__ == '__main__':
  main()
