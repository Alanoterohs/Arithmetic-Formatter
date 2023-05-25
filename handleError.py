import re


def checkLimit(operations):
  if len(operations) >= 5:
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

  for operation in operations:
    for stringArr in operation.split():
      if stringArr.isdigit() and len(stringArr) > 4:
        return True
  return False