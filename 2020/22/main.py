from collections import deque
from copy import deepcopy

file_inp = open("22.in", "r")
player_decks = file_inp.read().strip().split("\n\n")

player1 = [int(x) for x in player_decks[0].split("Player 1:\n")[1].split("\n")]
player2 = [int(x) for x in player_decks[1].split("Player 2:\n")[1].split("\n")]

p1Q = deque(deepcopy(player1))
p2Q = deque(deepcopy(player2))
win = 'p1'

while True:
  if len(p1Q) == 0 or len(p2Q) == 0:
    if len(p1Q) == 0:
      win = 'p2'
    break
  
  play1 = p1Q.popleft()
  play2 = p2Q.popleft()
  
  if play1 > play2:
    p1Q.append(play1)
    p1Q.append(play2)
  else:
    p2Q.append(play2)
    p2Q.append(play1)
    
def score(li):
  s = 0
  c = len(li)
  for x in li:
    s += c * x
    c-=1
  return s

winlist = list(p1Q) if win == 'p1' else list(p2Q)
# part 1
print(score(winlist))

def playgame(l1, l2):
  l1Q = deque(l1)
  l2Q = deque(l2)
  dub = 'p1'
  cache = set()
  
  while True:
    if len(l1Q) == 0 or len(l2Q) == 0:
      if len(l1Q) == 0:
        dub = 'p2'
      return dub, l1Q, l2Q
    
    if (tuple(l1Q), tuple(l2Q)) in cache:
      l1Q.append(l1Q.popleft())
      l1Q.append(l2Q.popleft())
      continue
    cache.add((tuple(l1Q), tuple(l2Q)))
    
    p1 = l1Q.popleft()
    p2 = l2Q.popleft()
    
    print(p1, p2, l1Q, l2Q)
    
    if len(l1Q) >= p1 and len(l2Q) >= p2:
    # play sub game here
      dub, _, _ = playgame([list(deepcopy(l1Q))[x] for x in range(p1)], [list(deepcopy(l2Q))[x] for x in range(p2)])
      if dub == 'p1':  
        l1Q.append(p1)
        l1Q.append(p2)
      else:
        l2Q.append(p2)
        l2Q.append(p1)
    else:
      if p1 > p2:
        l1Q.append(p1)
        l1Q.append(p2)
      else:
        l2Q.append(p2)
        l2Q.append(p1)

win, p1Q, p2Q = playgame(deepcopy(player1), deepcopy(player2))
winlist = list(p1Q) if win == 'p1' else list(p2Q)
# part 2
print(score(winlist))
