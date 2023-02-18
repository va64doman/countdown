import random
import simpleaudio as sa
import time

def numbers_round(numbers, target, solutions, tempSolution): 
     if target in numbers:
          solutions.append(tempSolution) 
     for i in range(len(numbers)): 
          for j in range(i+1, len(numbers)): 
               temp = numbers[:] 
               b = temp.pop(j) 
               a = temp.pop(i) 
               numbers_round(temp + [a + b], target, solutions, tempSolution + [str(a), '+', str(b)])
               numbers_round(temp + [a * b], target, solutions, tempSolution + [str(a), 'x', str(b)])
               if a < b: a, b = b, a
               if a > b: numbers_round(temp + [a - b], target, solutions, tempSolution + [str(a), '-', str(b)])
               if a % b == 0: numbers_round(temp + [a // b], target, solutions, tempSolution + [str(a), '/', str(b)])
     pass


large = [i * 25 for i in range(1,5)]
small = sorted([i for i in range(1,11)] * 2)
largeSize = -1
smallSize = -1
validInput = False
numbers = []
solutions = []
tempSolution = []
filename = 'countdown.wav'

while not validInput:
     try:
          largeSize = int(input("How many large numbers? "))
          if largeSize < 0 or largeSize > 4: print("You must have 0 to 4 large numbers.")
          else:
               smallSize = 6 - largeSize
               validInput = True
     except ValueError:
          print("You must enter an integer between 0 to 4 inclusively.")


for i in range(smallSize):
     smallIdx = random.randint(0, len(small) - 1)
     numbers.append(small.pop(smallIdx))

for i in range(largeSize):
     largeIdx = random.randint(0, len(large) - 1)
     numbers.append(large.pop(largeIdx))

target = random.randint(100, 999)
print(f"You have {numbers}.")
time.sleep(3)
print(f"Your target is {target}.")
time.sleep(3)
print("And your time starts now.")
wave = sa.WaveObject.from_wave_file(filename)
play = wave.play()
play.wait_done()
print(f"The target was {target}, did you get it? Press enter to see how to get the target.")
input()

numbers_round(numbers, target, solutions, tempSolution)
print(f"There are {len(solutions)} different solutions.")
if len(solutions) > 0:
     a = ''
     b = ''
     for idx, elements in enumerate(solutions[0]):
          if elements == '+':
               idx += 1
               b = solutions[0][idx]
               print(f"{a} + {b} = {int(a) + int(b)}")
          elif elements == '-':
               idx += 1
               b = solutions[0][idx]
               print(f"{a} - {b} = {int(a) - int(b)}")
          elif elements == 'x':
               idx += 1
               b = solutions[0][idx]
               print(f"{a} x {b} = {int(a) * int(b)}")
          elif elements == '/':
               idx += 1
               b = solutions[0][idx]
               print(f"{a} / {b} = {int(a) // int(b)}")                                    
          else:
               a = elements

input()
