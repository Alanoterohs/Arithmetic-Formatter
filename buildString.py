from re import split


def buildString(operations):
  matrizString = []
  index = 0
  buildMatriz(operations, 0, matrizString, index)
  buildMatriz(operations, 1, matrizString, index)
  print(matrizString)


def buildMatriz(operations, mod, matrizString, index):
  print(matrizString)
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
