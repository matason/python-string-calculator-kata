def add(numbers):
  total = 0

  if numbers != "":
    total = sum(map(int, numbers.split(",")))

  return total
