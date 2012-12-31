def add(*arguments):
  total = 0

  for arg in arguments:
    arg = normaliseSeparator(arg)
    if arg != "":
      total += sum(map(int, arg.split(",")))

  return total

def normaliseSeparator(numbers):
  return numbers.replace("\n", ",")