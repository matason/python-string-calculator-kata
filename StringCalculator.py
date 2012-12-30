def add(numbers):
  if numbers == "":
    return 0

  return sum(map(int, numbers.split(",")))
