from kandinsky import *
from bombe import *
from chiffre import *
B=(255,255,255)
N=(0,0,0)
G=(220,220,220)
GF=(180,180,180)

class Button:
    def __init__(self,x,y,px,py):
        self.x,self.y=x,y
        self.px,self.py=px,py
        self.ps=False
        self.fg=(None,None)
        self.off=False
        self.mn=0
    def plc(self):
      fr = fill_rect
      if self.ps:
        fr(self.x,self.y,self.px,self.py,N)
        if self.off==False:
          fr(self.x+1,self.y+1,self.px-1,self.py-1,G)
        else:
          fr(self.x+1,self.y+1,self.px-1,self.py-1,GF)
      else:
        fr(self.x,self.y,self.px-1,self.py-1,B)
        fr(self.x+1,self.y+1,self.px-1,self.py-1,N)
        if self.off==False:
          fr(self.x+1,self.y+1,self.px-2,self.py-2,G)
        else:
          fr(self.x+1,self.y+1,self.px-2,self.py-2,GF)
    def delt(self):
        fr(self.x,self.y,self.px,self.py,B)
    def pfg(self,fg):
        if fg[0]=="chiffre":
          self.fg = fg
          if fg[1]==1:
            plac(fg[1],self.x+7,self.y+3)
          else:
            plac(fg[1],self.x+5,self.y+3)
        elif fg[0]=='bombe':
          self.fg = fg
          place(b,self.x+2,self.y+2)
        else:
          pass
    def pr(self):
      self.delt()
      self.ps=True
      self.plc()
    def of(self,b):
      self.delt()
      self.off=b
      self.plc()
      self.pfg(self.fg)