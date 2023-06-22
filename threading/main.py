import random
import threading
import time

def print_blinkies(family):
  for blinky in family:
    print(blinky, end='')
    time.sleep(0.01)
  print(end='\n')

class Blinky:
    def __init__(self, family):
      self.face = '(o.o)'
      self.family = family

    def __str__(self):
       return self.face

    def show_face(self, new_face, delay):
       self.face = new_face
       print_blinkies(family)
       time.sleep(delay)

    def run(self):
       while True:
          self.show_face('(-.-)', 0.1)
          self.show_face('(o.o)', random.uniform(0.1, 1.5))  

family = []
family.extend(Blinky(family) for i in range(10))
for blinky in family:
  threading.Thread(target=blinky.run).start()
family[0].run()