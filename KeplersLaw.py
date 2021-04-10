import sys, math, time
from math import *
from decimal import *
from vpython import *

window = canvas(title='3D planet simulation', width=1000, height=1000) 

GM = 1.33E+20
model_time = 86400
scale = 10000000000
loops = 0
loopsvar = 0
years = -1
yearcounter = 0
rest = 0.05
RADIUS = 10
planets = []
#scene.lights = []

class Sun():
    def __init__(self):
        # construct a sphere for the sun
        sphere(pos = vector(0,0,0), radius = 3, color = color.yellow, canvas = window, make_trail=True)
        # make a light where the sun is
        local_light(pos=vector(0,0,0), color=color.yellow)

class planet():
    def __init__(self, pos, vel, radius, planetColor):
        self.pos = vector(pos[0], pos[1], pos[2])
        self.acc = vector(0,0,0)
        self.vel = vector(vel[0], vel[1], vel[2])
        self.radius = radius
        self.color = planetColor
        self.sphere = sphere(pos = self.pos, radius = self.radius, color = self.color, canvas = window, make_trail=True)
        planets.append(self)

        self.acc.x = -GM*self.pos.x/pow((self.pos.x*self.pos.x+self.pos.y*self.pos.y),1.5)
        self.acc.y = -GM*self.pos.y/pow((self.pos.x*self.pos.x+self.pos.y*self.pos.y),1.5)
        self.vel.x = self.vel.x-0.5*model_time*GM*self.pos.x/pow((self.pos.x*self.pos.x+self.pos.y*self.pos.y),1.5)
        self.vel.y = self.vel.y-0.5*model_time*GM*self.pos.y/pow((self.pos.x*self.pos.x+self.pos.y*self.pos.y),1.5)
        self.xholder = self.pos.x
        self.yholder = self.pos.y

    def update(self):
        self.acc.x = -GM*self.pos.x/pow((self.pos.x*self.pos.x+self.pos.y*self.pos.y),1.5)
        self.acc.y = -GM*self.pos.y/pow((self.pos.x*self.pos.x+self.pos.y*self.pos.y),1.5)
        self.vel.x = self.vel.x+self.acc.x*model_time
        self.vel.y = self.vel.y+self.acc.y*model_time
        self.xholder = self.pos.x
        self.yholder = self.pos.y
        #self.pos.xpos = (self.pos.x+self.vel.x*model_time)/scale
        #self.pos.ypos = (self.pos.y+self.vel.y*model_time)/scale
        self.pos.x = (self.pos.x+self.vel.x*model_time)
        self.pos.y = (self.pos.y+self.vel.y*model_time)
        self.sphere.pos = self.pos

sun = sphere(pos = vector(0,0,0), radius = RADIUS, color = color.yellow, canvas = window, make_trail=True)
#lamp = local_light(pos=vector(0,0,0), color=color.yellow)
Mercury = planet((0, 0.6E+11, 0), (4.7E+4, 0, 0), RADIUS, color.green)
Venus = planet((0, 1.075E+11, 0), (35000, 0, 0), RADIUS, color.purple)
Earth = planet((0, 1.47E+11, 0), (3.03E+04, 0, 0), RADIUS, color.blue)
Mars = planet((0, 2.07E+11, 0), (2.41E+04, 0, 0), RADIUS, color.red)
Jupiter = planet((0, 7.41E+11, 0), (1.31E+04, 0, 0), RADIUS, color.cyan)
Saturn = planet((0, 1.35E+12, 0), (9.68E+03, 0, 0), RADIUS, color.orange)
Uranus = planet((0, 2.74E+12, 0), (7.11E+03, 0, 0), RADIUS, color.magenta)
Neptune = planet((0, 4.44E+12, 0), (5.50E+03, 0, 0), RADIUS, color.white)

while True:
    for planet in planets:
        planet.update()
    time.sleep(rest)