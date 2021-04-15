def solution1(nums):
  for x in nums:
    y = 2020 - x
    if y in nums:
      print("solution 1:", x * y)
      break


def solution2(nums):
  found = False

  for x in nums:
    if found:
      break
    for y in nums:
      d = 2020 - x - y
      if d in nums:
        print("solution 2:", x * y * d)
        found = True
        break

with open("./data.txt") as file:
  inputs = file.read()
  nums = set(map(lambda x: int(x), filter(lambda x: x != "", inputs.split("\n"))))
  solution1(nums)
  solution2(nums)
