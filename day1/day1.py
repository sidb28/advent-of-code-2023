import re
digits = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}
sum = 0
with open('./day1.txt') as inputfile:
  for val in inputfile:
    for digit in digits: # remove this entire loop for part 1 of the question
      val = val.replace(digit, digit+digits[digit]+digit)
    nums = re.findall(r'[0-9]', val)
    # print(nums[0], nums[-1], nums[0]+nums[-1])
    sum += int(nums[0]+nums[-1])

print(sum)
