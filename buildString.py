from re import split, findall


def buildString(operations):
  matrizString = []
  index = 0
  halfSizeMatriz = len(operations)
  buildMatriz(operations, 0, matrizString, index)
  buildMatriz(operations, 1, matrizString, index)
  lineBuild(matrizString, halfSizeMatriz)
  print(matrizString)
  #print(halfSizeMatriz)


def buildMatriz(operations, mod, matrizString, index):
  #print(matrizString)
  global elementWithOperand
  for operation in operations:
    #print(operation)
    for number in split(r"[+|-]", operation):
      #print(number)
      if index % 2 == mod:
        if mod == 1:
          number = "+" + number if "+" in operation else "-" + number
        matrizString.append(number.strip())
      index += 1

      #else:

  #print(matrizString)


def lineBuild(matrizString, halfSizeMatriz):
  pattern = "[0-9]"
  for operation in range(0, halfSizeMatriz):
    sizeFirst = len(findall('\d+', matrizString[operation])[0])
    sizeSecond = len(findall('\d+', matrizString[operation + halfSizeMatriz])[0])
    if sizeFirst > sizeSecond:
      matrizString.append(lines(sizeFirst + 2))
    else:
      matrizString.append(lines(sizeSecond + 2))


def lines(size):
  line = ""
  for x in range(size):
    line += "-"
  print(line)
  return line
