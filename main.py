import random
import asyncio
import time

def print_blinkies(family):
  for blinky in family:
    print(blinky, end='')
  print(end='\n')

class Blinky:
    def __init__(self, family):
      self.face = '(o.o)'
      self.family = family

    def __str__(self):
       return self.face

    async def show_face(self, new_face, delay):
       self.face = new_face
       print_blinkies(family)
       await asyncio.sleep(delay)

    async def run(self):
       while True:
          await self.show_face('(-.-)', 0.1)
          await self.show_face('(o.o)', random.uniform(0.1, 1.5))  

family = []
family.extend(Blinky(family) for i in range(10))

async def run_all():
  tasks = []
  for blinky in family:
    tasks.append(asyncio.ensure_future(blinky.run()))
  for tasks in tasks:
     await tasks

asyncio.run(run_all())