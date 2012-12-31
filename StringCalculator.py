def add(*arguments):
  total = 0

  for arg in arguments:
    arg = arg.replace("\n", ",")
    if arg != "":
      total += sum(map(int, arg.split(",")))

  return total
