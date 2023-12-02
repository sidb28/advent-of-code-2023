import re
total_part1 = 0
total_part2 = 0 # for part 2
limits = {'red': 12, 'green': 13, 'blue': 14}

with open('./day2.txt') as inputfile:
  for game in inputfile:
    min_required = {'red': 1, 'green': 1, 'blue': 1} # for part 2
    power = 1 # for part 2
    valid_game = True
    colon_index = game.index(':')
    rounds = game[colon_index+1:].split(';')
    for round in rounds:
      regex_match = re.findall(r'(\d+)\s+(\w+)', round)
      for count, color in regex_match:
        if int(count) > limits[color]:
          valid_game = False
        min_required[color] = max(min_required[color], int(count)) # for part 2
    if valid_game:
      total_part1 += int(game[game.index(' '):colon_index])
    for val in min_required.values(): # for part 2
      power *= int(val)
    total_part2 += power # for part 2

print('Part 1:', total_part1)
print('Part 2:', total_part2) # for part 2
