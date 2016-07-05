import sys
import pyttsx

# main() function
def main():
  # use sys.argv if needed
  print 'running speech-test.py...'
  engine = pyttsx.init()
  with open ("esteestexto.txt")as f:
      lines = f.readlines()
  engine.say(lines)
  engine.runAndWait()

# call main
if __name__ == '__main__':
  main()
