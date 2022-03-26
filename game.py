from ion import *
from button import *
from random import *
off=0
ply=False
def pg(g,nmnn,x,y):
  tx=randint(0,15)
  ty=randint(0,10)
  if not ((tx in ((x-2)%16,(x-1)%16,x,(x+1)%16,(x+2)%16)) and (ty in ((y-2)%11,(y-1)%11,y,(y+1)%11,(y+2)%11))):
    if g[tx][ty].mn>=0:
      g[tx][ty].mn=-1
      for q in list(filter(lambda s:s[0] in range(16) and s[1] in range(11),[(tx+1,ty+1),(tx+1,ty),(tx+1,ty-1),(tx,ty+1),(tx,ty-1),(tx-1,ty+1),(tx-1,ty),(tx-1,ty-1)])):
        if g[q[0]][q[1]].mn!=-1:
          g[q[0]][q[1]].mn+=1
      nmnn-=1
  return g,nmnn
def aff(g,x,y):
  g[x][y].pr()
  if g[x][y].mn>0:
    g[x][y].pfg(("chiffre",g[x][y].mn))
  if x in range(1,15) and y in range(1,10):
    if g[x][y].mn==0:
      if not g[x+1][y].ps:
        aff(g,x+1,y)
      if not g[x-1][y].ps:
        aff(g,x-1,y)
      if not g[x][y+1].ps:
        aff(g,x,y+1)
      if not g[x][y-1].ps:
        aff(g,x,y-1)
def gr(x,y):
  g=[]
  for i in range(x):
    g.append([])
    for k in range(y):
      b = Button(i*20,k*20,20,20)
      b.plc()
      g[i].append(b)
  g[0][0].of(True)
  return g
g=gr(16,11)
pr=0
nmn=25
while True:
  if keydown(KEY_RIGHT):
    if pr==0:
      g[off%16][off//16].of(False)
      if off<175:
        off+=1
      else:
        off=0
      g[off%16][off//16].of(True)
      pr=1
  elif keydown(KEY_LEFT):
    if pr==0:
      g[off%16][off//16].of(False)
      if off>0:
        off-=1
      else:
        off=175
      g[off%16][off//16].of(True)
      pr=1
  elif keydown(KEY_UP):
    if pr==0:
      g[off%16][off//16].of(False)
      if off>15:
        off-=16
      else:
        off=176-(16-off)
      g[off%16][off//16].of(True)
      pr=1
  elif keydown(KEY_DOWN):
    if pr==0:
      g[off%16][off//16].of(False)
      if off<160:
        off+=16
      else:
        off=16-(176-off)
      g[off%16][off//16].of(True)
      pr=1
  elif keydown(KEY_EXE):
    if not ply:
      while nmn != 0:
        g,nmn=pg(g,nmn,off%16,off//16)
        g[off%16][off//16].pr()
      aff(g,off%16,off//16)
      ply=True
    else:
      if pr==0:
        g[off%16][off//16].pr()
        if g[off%16][off//16].mn==-1:
          g[off%16][off//16].pfg(("bombe",))
        elif g[off%16][off//16].mn>0:
          g[off%16][off//16].pfg(("chiffre",g[off%16][off//16].mn))
        pr=1
  else:
    pr=0
