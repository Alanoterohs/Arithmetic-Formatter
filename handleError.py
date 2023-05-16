import re


def checkLimit(operations):
  if operations.size() >= 5:
    return True
  else:
    return False


def checkOperators(operations):
  operatorDivision = "/"
  operatorMultiplication = "*"

  for operation in operations:
    if operatorDivision in operation or operatorMultiplication in operation:
      return True
  return False


def checkDigits(operations):
  pattern = "[0-9]"

  for operation in operations:
    if not re.search(pattern, operation):
      return True
  return False


def checkEachOperand(operations):
  pattern = "[0-9]{0,4}"

  for operation in operations:
    for stringArr in operation.split():
      if stringArr.isdigit() and stringArr.size() > 4:
        return True
  return False