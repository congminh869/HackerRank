import fileinput
import random

def parse_params():
  lines = []
  for line in fileinput.input(files ='input.txt'):
    lines.append(line.replace("\n",""))
  num_cases = int(lines[0][1])
  # print(num_cases)
  tests = []
  for i in range(num_cases):
    # print('i = ',i)
    probs = lines[4*i + 1].strip().split(",")
    # print(probs)
    probs = [float(x) for x in probs]
    # print(probs)
    num_ladders, num_snakes = lines[4*i + 2].strip().split(",")
    # print('num_ladders = ',num_ladders)
    # print('num_snakes',num_snakes)
    # check num of ladder and num of snakes. Smaller than 15 
    ladders = lines[4*i + 3].strip().split(" ")
    # print('ladders = ',ladders)
    snakes = lines[4*i + 4].strip().split(" ")
    # print('snakes = ',snakes)
    tests.append([probs, ladders, snakes])
    # print(tests)
    # print('----------------------------------------')
  return tests

class BoardGame:
  def __init__(self, events):
    '''
    cộng 2 giá trị đầu và cuối của thang và rắn rồi chia ra làm 2 mảng srarts và ends 
    '''
    self.current = 1
    self.starts = []
    self.ends = []
    for p in events:
      start, end = [int(x) for x in p.split(",")]
      self.starts.append(start)
      self.ends.append(end)
    
  def move(self, num):
    if self.current + num <= 100:
      self.current += num
    print('current = ',self.current)
    print('starts = ',self.starts)
    if self.current in self.starts:
      self.current = self.ends[self.starts.index(self.current)]
    return self.current

def add_one_by_one(l):
  '''

  '''
  print('l = ',l)
  new_l = []
  cumsum = 0
  for elt in l:
    # print('elt = ',elt)
    cumsum += elt
    # print('cumsum = ',cumsum)
    new_l.append(cumsum)
  # print('new_l = ',new_l)
  return new_l
    
class Die:
  def __init__(self, probs):
    self.probs = add_one_by_one(probs)

  def roll(self):
    rand = random.uniform(0, 1)
    if rand <= self.probs[0]:
        return 1
    elif rand > self.probs[0] and rand <= self.probs[1]:
        return 2
    elif rand > self.probs[1] and rand <= self.probs[2] :
        return 3
    elif rand > self.probs[2] and rand <= self.probs[3]:
        return 4
    elif rand > self.probs[3] and rand <= self.probs[4]:
        return 5
    else:
        return 6
 

def play(probs, ladders, snakes):
  # print('probs = ', probs)
  # print('ladders = ',ladders)
  # print('snakes = ',snakes)
  # print('ladders + snakes = ',ladders + snakes)
  # events = ladders + snakes
  # for p in events:
  #   print('p = ',p)
  #   start, end = [int(x) for x in p.split(",")]
  #   print('start = ',start)
  #   print('end = ',end)
  # print('------')
  board = BoardGame(ladders + snakes)
  die = Die(probs)
  num_moves = 0
  while num_moves < 1000 and board.move(die.roll()) != 100:
    num_moves += 1
  return num_moves


# print('starts')
tests = parse_params()
# print('tests',tests)
for params in tests:
  play(*params)
  # print(params)
  # sum = 0
  # num_trials = 0
  # for i in range(5000): # 5000 trials
  #   num_moves = play(*params)
  #   if num_moves < 1000:
  #     sum += num_moves
  # print (int(sum / 5000))
