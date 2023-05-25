import handleError
from buildString import buildString


def arithmetic_arranger(operations):
  if handleError.checkLimit(operations):
    return "Error: Too many problems."
  elif handleError.checkOperators(operations):
    return "Error: Operator must be '+' or '-'."
  elif handleError.checkDigits(operations):
    return "Error: Numbers must only contain digits."
  elif (handleError.checkEachOperand(operations)):
    return "Error: Numbers cannot be more than four digits."
  return buildString(operations)