import re

SEPARATOR = ","

def add(*arguments):
  total = 0

  for arg in arguments:
    if arg != "":
      arg = normaliseSuppliedSeparator(arg)
      arg = normaliseSeparator(arg)
      total += sum(map(int, arg.split(SEPARATOR)))

  return total

def normaliseSeparator(numbers):
  return numbers.replace("\n", SEPARATOR)

def normaliseSuppliedSeparator(numbers):
  if re.match("//.{1}\n", numbers):
    separator = numbers[2]
    numbers = numbers[4:]
    numbers = numbers.replace(separator, SEPARATOR)

  return numbers
