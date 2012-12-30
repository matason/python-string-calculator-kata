def add(*arguments):
  total = 0

  for arg in arguments:
    if arg != "":
      total += sum(map(int, arg.split(",")))

  return total
