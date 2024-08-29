import sys

f = open("input.bin", "rb")
inp = f.read()
f.close()
inp = [int(j) for j in list("".join([bin(i + 256)[3:] for i in inp]))]

f = open("program.txt", "r")
prog = f.read().split("\n")
f.close()

prog = [i.strip() for i in prog]

currentIndex = 0
currentBit = 0
bitTable = {}

commandslist = ["HEY!", "DONT FUCK WITH ME", "THIS SHIT WILL GET YOU EVICTED",
"YOU SON OF A BITCH", "SHITHEAD LITTLE PUNK", "SHITHEAD", "*pause to intimidate*",
"*pause*", "PEICE OF SHIT", "I CAN GO IN YOUR HOUSE WHENEVER I WANT"]

programCommands = []
for i in prog:
  if i in commandslist:
    programCommands.append(commandslist.index(i))

correspondences = []
stack = []
for i in range(len(programCommands)):
  if programCommands[i] == 8:
    stack.append(i)
  elif programCommands[i] == 9:
    try:
      correspondences.append((stack.pop(), i))
    except:
      sys.exit("unmatched 'I CAN GO IN YOUR HOUSE WHENEVER I WANT'")
if stack != []:
  sys.exit("unmatched 'PEICE OF SHIT'")

programHasStarted = False

while currentIndex < len(programCommands):
  currentCommand = programCommands[currentIndex]
  for i in range(7):
    if currentBit + i not in bitTable:
      bitTable[currentBit + i] = False
  if currentCommand == 0:
    programHasStarted = True
    currentIndex += 1
  if programHasStarted:
    if currentCommand == 1:
      bitTable[currentBit] = not bitTable[currentBit]
      currentIndex += 1
    elif currentCommand == 2:
      currentBit += 1
      currentIndex += 1
    elif currentCommand == 3:
      currentBit -= 1
      currentIndex += 1
    elif currentCommand == 4:
      stringToPrint = ""
      for i in range(8):
        stringToPrint += str(int(bitTable[currentBit + i]))
      stringToPrint = chr(int(stringToPrint, 2))
      print(stringToPrint, end = "")
      currentIndex += 1
    elif currentCommand == 5:
      print(int(bitTable[currentBit]), end = "")
      currentIndex += 1
    elif currentCommand == 6:
      if len(inp) < 8:
        inp += [0]*8
      for i in range(8):
        bit = inp.pop(0)
        bitTable[currentBit + i] = bool(bit)
      currentIndex += 1
    elif currentCommand == 7:
      if len(inp) == 0:
        inp += [0]*8
      bit = inp.pop(0)
      bitTable[currentBit] = bool(bit)
      currentIndex += 1
    elif currentCommand == 8:
      if bitTable[currentBit]:
        currentIndex += 1
      else:
        currentIndex = [i for i in correspondences if i[0] == currentIndex][0][1]
    elif currentCommand == 9:
      if not bitTable[currentBit]:
        currentIndex += 1
      else:
        currentIndex = [i for i in correspondences if i[1] == currentIndex][0][0]
  else:
    currentIndex += 1
  
