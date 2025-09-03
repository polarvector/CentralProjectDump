from turtle import *
from random import randint as rint
from math import sin, cos, tan, asin, acos, atan, atan2, pi
import sys
import string

def random_walk(n):
     direction = rint(1,3)
     if direction == 1: forward(n)
     elif direction == 2: left(90); forward(n)
     else: right(90);forward(n)

def random_stalk(n):
     direction = rint(1,4)
     if direction == 1: forward(n)
     elif direction == 2: left(90); forward(n)
     elif direction == 3: back(n)
     else: right(90);forward(n)

def truly_random_walk(n):
     direction = rint(1,3)
     if direction == 1: forward(n)
     elif direction == 2: left(rint(0,90)); forward(n)
     else: right(rint(0,90));forward(n)

def random_walks():
     left(45)
     if len(sys.argv) != 2: scale = 10
     else: scale = sys.argv[1]

     for i in range(1000):
          #speed(rint(0,10))
          speed(0)
          random_walk(scale)
          #random_stalk(scale)
          #truly_random_walk(scale)

def line(n):
     forward(n)
     back(2*n)
     forward(n)

def local_home(iter):
     home()
     left(int(sys.argv[4])*iter)

def cartesian_plane(n, scale, iter):
     for _ in range(4):
          local_home(iter)
          if _ >= 2:
               left(90)

          if _ % 2 == 0:
               sign = 1
          else: sign = -1

          for i in range(n):
               #speed(rint(0,10))
               line(n * scale)
               left(90 * sign)
               forward(scale)
               right(90 * sign)

def twist():
     for _ in range(int(sys.argv[3])):
          cartesian_plane(int(sys.argv[1]), int(sys.argv[2]), _)

def rectangle(l,b):
     for _ in range(2):
          forward(l)
          left(90)
          forward(b)
          left(90)

def mangenkyou(r=100,a=75):
     setup()
     for i in range(4):
          left(90)
          forward(r*cos(a)/2)
          circle(r*cos(a)/2, theta=20)
          penup()
          left(90)
          forward(r*cos(a)/2)
          left(90)
          forward(r*cos(a)/2)
          left(90)
          pendown()
          penup()
          forward(r/3)
          pendown()   

def eye(r=100,a=75,spiral=0):
     setup()
     aRad = a*pi/180

     def iris(r,aRad):
          r = r*sin(aRad)
          for i in range(27):
               if spiral != 0:
                    aRad = a*pi/180
                    r = r*sin(aRad)
               left(90)
               forward(r)
               theta = atan(2*cos(aRad))
               right(180*(1-theta/pi))
               forward(r/cos(theta))
               left(180*(1-theta/pi))
               forward(r/cos(theta))
               right(180*(1-theta/pi))
               forward(r)
               left(90)
               penup()
               forward(r/3)
               pendown()

     def corona_0(r,aRad):
          r *= sin(aRad)
          theta = atan(2*cos(aRad))
          for i in range(54):
               left(360-180*(1-theta/pi))
               forward(r/cos(theta))
               back(0.5*r/cos(theta))
               left(90-360-180*(1-theta/pi))
               left(360-180*(1-theta/pi))
               forward(r/cos(theta))
               back(0.5*r/cos(theta))
               right(90-360-180*(1-theta/pi))
               right(90)
               penup()
               forward(r/3)
               pendown()
     
     def corona_1(r,aRad):
          theta = atan( r*sin(aRad)/(2*r*cos(aRad)) )
          r *= sin(aRad)
          for i in range(40):
               left(deg(theta))
               forward(r/sin(theta))
               back(r/(2*sin(theta)))
               right(2*deg(theta))
               back(r/(2*sin(theta)))
               forward(r/sin(theta))
               right(deg(theta))
               penup()
               forward(r/3)
               pendown()

     iris(r,aRad)
     corona_0(r,aRad)
     corona_1(r,aRad)

def circle(r, theta=10, rotation=360, dir=1): 
     if dir not in [1,-1]:
          return print("Invalid direction parameter. CW = 1, CCW = -1")
     forward(r)
     left(dir*90)
     theta_r = pi*theta/180
     for i in range(int(rotation/theta)):
          forward(r*sin(theta_r))
          left(dir*90)
          forward(r*(1-cos(theta_r)))
          right(dir*90)
          left(dir*theta)

def write(text, r=100, a=75):
     setup()
     aRad = a*pi/180

     def gap(sp=r/3):
          penup()
          forward(sp)
          pendown()          

     def straighten(len):
          return len*sin(aRad)

     def A(r,a):
          left(a)
          forward(r)
          right(2*a)
          forward(r/2)
          left(a)
          back(1.5*r*cos(aRad))
          forward(1.5*r*cos(aRad))
          right(a)
          forward(r/2)
          left(a)
          gap()

     def B(r,a):
          r = straighten(r)
          left(90)
          forward(r*3/4)
          circle(r/4,rotation=180, dir=-1)
          left(90)
          forward(r*1/4)
          left(180)
          circle(r/4,rotation=180, dir=-1)
          left(180)
          gap()

     def C(r,a):
          gap()

     def D(r,a):
          gap(sp=-r/12)
          r = straighten(r)
          left(90)
          forward(r*1/2)
          circle(r/2,rotation=180, dir=-1)
          left(180)
          gap(sp=5*r/6)

     def E(r,a):
          F(r,a,e=1)

     def F(r,a,e=0):
          r = straighten(r)
          left(90)
          forward(r)
          right(90)
          forward(2*r*cos(aRad))
          forward(-2*r*cos(aRad))
          left(90)
          back(r/2)
          right(90)
          forward(1.5*r*cos(aRad))
          forward(-1.5*r*cos(aRad))
          left(90)
          back(r/2)
          right(90)
          forward(e*2*r*cos(aRad))
          gap(sp= r/3 + (1-e)*2*r*cos(aRad) )

     def G(r,a):
          gap()

     def H(r,a):
          r = straighten(r)
          left(90)
          forward(r)
          back(r/2)
          right(90)
          back(r/16)
          forward(2*r/tan(aRad))
          forward(r/16)
          back(r/16)
          left(90)
          forward(r/2)
          back(r)
          right(90)
          gap()

     def I(r,a):
          forward(r*cos(aRad))
          left(90)
          forward(straighten(r))
          left(90)
          forward(r*cos(aRad))
          right(180)
          forward(2*r*cos(aRad))
          back(r*cos(aRad))
          right(90)
          forward(straighten(r))
          left(90)
          forward(r*cos(aRad))
          gap()

     def J(r,a):
          gap()

     def K(r,a):
          left(90)
          r = straighten(r)
          forward(r)
          back(r/2)
          theta = atan(2/tan(aRad))
          right(deg(theta))
          forward(0.5*r/cos(theta))
          back(0.5*r/cos(theta))
          left(deg(theta))
          right(180)
          left(deg(theta))
          forward(0.5*r/cos(theta))
          back(0.5*r/cos(theta))
          right(deg(theta))
          forward(r/2)
          left(90)
          gap()

     def L(r,a):
          r = straighten(r)
          left(90)
          forward(r)
          back(r)
          right(90)
          forward(2*r/tan(aRad))
          gap()

     def M(r,a):
          r = straighten(r)
          left(90)
          forward(r)
          theta = atan(2*cos(aRad))
          right(180 - deg(theta))
          forward(r/cos(theta))
          left(180 - deg(theta))
          right(deg(theta))
          forward(r/cos(theta))
          right(180 - deg(theta))
          forward(r)
          left(90)
          gap()

     def N(r,a):
          r = straighten(r)
          left(90)
          forward(r)
          theta = atan(2*cos(aRad))
          right(180*(1-theta/pi))
          forward(r/cos(theta))
          left(180*(1-theta/pi))
          forward(r)
          back(r)
          right(90)
          gap()

     def O(r,a):
          left(90)
          forward(r*sin(aRad))
          back(r*sin(aRad)/2)
          left(90)
          forward(r*cos(aRad))
          back(2*r*cos(aRad))
          forward(r*cos(aRad))
          left(90)
          forward(r*sin(aRad)/2)
          left(90)
          gap()

     def P(r,a):
          r = straighten(r)
          left(90)
          forward(r*3/4)
          circle(r/4,rotation=180, dir=-1)
          left(90)
          forward(r/2)
          left(90)
          gap()

     def Q(r,a):
          O(r,a)

     def R(r,a):
          r = straighten(r)
          left(90)
          forward(r*3/4)
          circle(r/4,rotation=180, dir=-1)
          left(90)
          theta = asin(1/2) # obtained through: (r/4) / (r/2)
          left(theta*180/pi)
          forward(r/(2*cos(theta)))
          left(90 - theta*180/pi)
          gap()

     def S(r,a):
          gap()

     def T(r,a):
          penup()
          forward(r*cos(aRad))
          pendown()
          left(90)
          forward(straighten(r))
          right(90)
          forward(r*cos(aRad))
          back(2*r*cos(aRad))
          forward(r*cos(aRad))
          right(90)
          forward(straighten(r))
          left(90)
          gap()

     def U(r,a):
          gap()
     
     def V(r,a,v=1):
          left(a)
          forward(r)
          back(r)
          left(180-2*a)
          forward(r)
          back(r)
          right(180-2*a+a)
          if v==1:
               gap()

     def W(r,a):
          V(r,a,v=0)
          penup()
          forward(2*r*cos(aRad))
          pendown()
          V(r,a,v=0)
          gap(sp=r)

     def X(r,a):
          theta = atan( straighten(r)/(2*r*cos(aRad)) )
          left(deg(theta))
          r = straighten(r)
          forward(r/sin(theta))
          back(r/(2*sin(theta)))
          right(2*deg(theta))
          back(r/(2*sin(theta)))
          forward(r/sin(theta))
          left(deg(theta))
          gap()

     def Y(r,a):
          left(90)
          r = straighten(r)
          forward(r/2)
          theta = atan(2*cos(aRad))  # atan(p/b) = atan( r Cos(aRad) / r/2)
          left(deg(theta))
          forward(r/(2*cos(theta)))
          back(r/(2*cos(theta)))
          right(2*deg(theta))
          forward(r/(2*cos(theta)))
          back(r/(2*cos(theta)))
          left(deg(theta))
          back(r/2)
          right(90)
          gap()

     def Z(r,a):
          left(90)
          penup()
          forward(straighten(r))
          pendown()
          right(90)
          theta = atan( straighten(r)/(2*r*cos(aRad)) )
          forward(2*r*cos(aRad))
          right(180-deg(theta))
          forward(straighten(r)/sin(theta))
          left(180-deg(theta))
          forward(2*r*cos(aRad))
          gap()

     def space(r,a):
          gap(sp=r)
    
     func_map = {}
     for letter in string.ascii_uppercase:
         func_map[letter] = locals()[letter] # assigning functions to their respective letters
     func_map[" "] = locals()["space"]

     for letter in text:
          if letter in func_map:
               func_map[letter](r,a) # the magic happens here. Calls function associated with the letter
          else:
               print(f"No function for this character: {letter}")

def setup():
     speed(0)
     ht()
     back(400)
     screensize(1600,900)
     bgcolor("black")
     color("white")
     shape("turtle")
     #hideturtle()

def deg(angle):
     return angle*180/pi
     
def rad(angle):
     return angle*pi/180

def main():
     #if len(sys.argv) == 2: random_walks()
     #elif len(sys.argv) == 5: twist()
     #elif len(sys.argv) == 3 and sys.argv[1] == "-circle": circle(int(sys.argv[2]))
     #else: random_walks()
     #eye()
     #mangenkyou()
     write(input("What shall the tiny turtle write?\n\n").strip().upper())
     #done()

if __name__ == "__main__":
     main()

# usage: random_walk.py [unit_scale] [grid_dimension] [number_of_grids] [rotation_angle_per_iteration]
# usage: random_walk.py [unit_scale]
# usage: random_walk.py -circle [radius]