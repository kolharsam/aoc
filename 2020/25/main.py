cardProb = 17115212
doorProb = 3667832

cardSample = 5764801
doorSample = 17807724

def rsa(pub):
  sub = 7
  val = 1
  loop = 0
  
  while val != pub:
    val = val * sub
    val = val % 20201227
    loop+=1
  
  return loop

def encrypt(val, loop_size):
  v = 1
  while loop_size != 0:
    v = v * val
    v = v % 20201227
    loop_size-=1
  
  return v

lcard = rsa(cardProb)
ldoor = rsa(doorProb)

print(encrypt(cardProb, ldoor))
