import re

SEPARATOR = ","

def add(*arguments):
  total = 0

  for numbers in arguments:
    if numbers != "":
      numbers = normaliseSuppliedSeparator(numbers)
      numbers = normaliseSeparator(numbers)
      total += sum(map(int, numbers.split(SEPARATOR)))

  return total

def normaliseSeparator(numbers):
  return numbers.replace("\n", SEPARATOR)

def normaliseSuppliedSeparator(numbers):
  if re.match("//.{1}\n", numbers):
    separator = numbers[2]
    numbers = numbers[4:]
    numbers = numbers.replace(separator, SEPARATOR)

  return numbers
