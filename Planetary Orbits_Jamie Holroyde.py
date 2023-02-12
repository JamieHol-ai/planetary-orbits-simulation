import pygame, sys, math, time
from pygame.locals import *
from math import *
from decimal import *
pygame.init()

screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("Planetary Orbits")
font = pygame.font.Font('freesansbold.ttf',14)
GM = 1.33E+20 #Gravitational Constant G (6.67E-11) x mass of Sun (1.99E30kg)
loops = 0
loopsvar = 0
years = -1
yearcounter = 0
computertime = 0.02
timevar = 2
model_time = 86400 #makes a new calculation every 24 hours model time
model_timedis = "minute"
scale = 10000000000
scaledis = 100
zoomvairable = 0
speedvairable = 0
zoomandspeedcount = 100
offset = 500

#Mercury
Mercuryloops = loops
Mercuryloopsvar = loopsvar
Mercuryyearcounter = yearcounter
Mercuryyears = years
Mercury_x_init = 0
Mercury_y_init = 0.6E+11
Mercury_v_x_init = 4.7E+4
Mercury_v_y_init = 0
Mercuryypos = 0
Mercuryxpos = 0
Mercurytime = 0
Mercuryx = Mercury_x_init
Mercuryy = Mercury_y_init

Mercury_a_x = -GM*Mercuryx/pow((Mercuryx*Mercuryx+Mercuryy*Mercuryy),1.5)
Mercury_a_y = -GM*Mercuryy/pow((Mercuryx*Mercuryx+Mercuryy*Mercuryy),1.5)
Mercury_v_x = Mercury_v_x_init-0.5*model_time*GM*Mercuryx/pow((Mercuryx*Mercuryx+Mercuryy*Mercuryy),1.5)
Mercury_v_y = Mercury_v_y_init-0.5*model_time*GM*Mercuryy/pow((Mercuryx*Mercuryx+Mercuryy*Mercuryy),1.5)
Mercuryxholder = Mercuryx
Mercuryyholder = Mercuryy


#Venus
Venusloops = loops
Venusloopsvar = loopsvar
Venusyearcounter = yearcounter
Venusyears = years
Venus_x_init = 0
Venus_y_init = 1.075E+11
Venus_v_x_init = 35000
Venus_v_y_init = 0
Venusxpos = 0
Venusypos = 0
Venustime = 0
Venusx = Venus_x_init
Venusy = Venus_y_init

Venus_a_x = -GM*Venusx/pow((Venusx*Venusx+Venusy*Venusy),1.5)
Venus_a_y = -GM*Venusy/pow((Venusx*Venusx+Venusy*Venusy),1.5)
Venus_v_x = Venus_v_x_init-0.5*model_time*GM*Venusx/pow((Venusx*Venusx+Venusy*Venusy),1.5)
Venus_v_y = Venus_v_y_init-0.5*model_time*GM*Venusy/pow((Venusx*Venusx+Venusy*Venusy),1.5)
Venusxholder = Venusx
Venusyholder = Venusy

#Earth
Earthloops = loops
Earthloopsvar = loopsvar
Earthyearcounter = yearcounter
Earthyears = years
Earth_x_init = 0
Earth_y_init = 1.47E+11
Earth_v_x_init = 3.03E+4
Earth_v_y_init = 0
Earthypos = 0
Earthxpos = 0
Earthtime = 0
Earthx = Earth_x_init
Earthy = Earth_y_init

Earth_a_x = -GM*Earthx/pow((Earthx*Earthx+Earthy*Earthy),1.5)
Earth_a_y = -GM*Earthy/pow((Earthx*Earthx+Earthy*Earthy),1.5)
Earth_v_x = Earth_v_x_init-0.5*model_time*GM*Earthx/pow((Earthx*Earthx+Earthy*Earthy),1.5)
Earth_v_y = Earth_v_y_init-0.5*model_time*GM*Earthy/pow((Earthx*Earthx+Earthy*Earthy),1.5)
Earthxholder = Earthx
Earthyholder = Earthy

#Mars
Marsloops = loops
Marsloopsvar = loopsvar
Marsyearcounter = yearcounter
Marsyears = years
Mars_x_init = 0
Mars_y_init = 2.07E+11
Mars_v_x_init = 2.41E+04
Mars_v_y_init = 0
Marsxpos = 0
Marsypos = 0
Marstime = 0
Marsx = Mars_x_init
Marsy = Mars_y_init

Mars_a_x = -GM*Marsx/pow((Marsx*Marsx+Marsy*Marsy),1.5)
Mars_a_y = -GM*Marsy/pow((Marsx*Marsx+Marsy*Marsy),1.5)
Mars_v_x = Mars_v_x_init-0.5*model_time*GM*Marsx/pow((Marsx*Marsx+Marsy*Marsy),1.5)
Mars_v_y = Mars_v_y_init-0.5*model_time*GM*Marsy/pow((Marsx*Marsx+Marsy*Marsy),1.5)
Marsxholder = Marsx
Marsyholder = Marsy


#Jupiter
Jupiterloops = loops
Jupiterloopsvar = loopsvar
Jupiteryearcounter = yearcounter
Jupiteryears = years
Jupiter_x_init = 0
Jupiter_y_init = 7.41E+11
Jupiter_v_x_init = 1.31E+04
Jupiter_v_y_init = 0
Jupiterypos = 0
Jupiterxpos = 0
Jupitertime = 0
Jupiterx = Jupiter_x_init
Jupitery = Jupiter_y_init

Jupiter_a_x = -GM*Jupiterx/pow((Jupiterx*Jupiterx+Jupitery*Jupitery),1.5)
Jupiter_a_y = -GM*Jupitery/pow((Jupiterx*Jupiterx+Jupitery*Jupitery),1.5)
Jupiter_v_x = Jupiter_v_x_init-0.5*model_time*GM*Jupiterx/pow((Jupiterx*Jupiterx+Jupitery*Jupitery),1.5)
Jupiter_v_y = Jupiter_v_y_init-0.5*model_time*GM*Jupitery/pow((Jupiterx*Jupiterx+Jupitery*Jupitery),1.5)
Jupiterxholder = Jupiterx
Jupiteryholder = Jupitery


#Saturn
Saturnloops = loops
Saturnloopsvar = loopsvar
Saturnyearcounter = yearcounter
Saturnyears = years
Saturn_x_init = 0
Saturn_y_init = 1.35E+12
Saturn_v_x_init = 9.68E+03
Saturn_v_y_init = 0
Saturnypos = 0
Saturnxpos = 0
Saturntime = 0
Saturnx = Saturn_x_init
Saturny = Saturn_y_init

Saturn_a_x = -GM*Saturnx/pow((Saturnx*Saturnx+Saturny*Saturny),1.5)
Saturn_a_y = -GM*Saturny/pow((Saturnx*Saturnx+Saturny*Saturny),1.5)
Saturn_v_x = Saturn_v_x_init-0.5*model_time*GM*Saturnx/pow((Saturnx*Saturnx+Saturny*Saturny),1.5)
Saturn_v_y = Saturn_v_y_init-0.5*model_time*GM*Saturny/pow((Saturnx*Saturnx+Saturny*Saturny),1.5)
Saturnxholder = Saturnx
Saturnyholder = Saturny


#Uranus
Uranusloops = loops
Uranusloopsvar = loopsvar
Uranusyearcounter = yearcounter
Uranusyears = years
Uranus_x_init = 0
Uranus_y_init = 2.74E+12
Uranus_v_x_init = 7.11E+03
Uranus_v_y_init = 0
Uranusypos = 0
Uranusxpos = 0
Uranustime = 0
Uranusx = Uranus_x_init
Uranusy = Uranus_y_init

Uranus_a_x = -GM*Uranusx/pow((Uranusx*Uranusx+Uranusy*Uranusy),1.5)
Uranus_a_y = -GM*Uranusy/pow((Uranusx*Uranusx+Uranusy*Uranusy),1.5)
Uranus_v_x = Uranus_v_x_init-0.5*model_time*GM*Uranusx/pow((Uranusx*Uranusx+Uranusy*Uranusy),1.5)
Uranus_v_y = Uranus_v_y_init-0.5*model_time*GM*Uranusy/pow((Uranusx*Uranusx+Uranusy*Uranusy),1.5)
Uranusxholder = Uranusx
Uranusyholder = Uranusy


#Neptune
Neptuneloops = loops
Neptuneloopsvar = loopsvar
Neptuneyearcounter = yearcounter
Neptuneyears = years
Neptune_x_init = 0
Neptune_y_init = 4.44E+12
Neptune_v_x_init = 5.50E+03
Neptune_v_y_init = 0
Neptuneypos = 0
Neptunexpos = 0
Neptunetime = 0
Neptunex = Neptune_x_init
Neptuney = Neptune_y_init

Neptune_a_x = -GM*Neptunex/pow((Neptunex*Neptunex+Neptuney*Neptuney),1.5)
Neptune_a_y = -GM*Neptuney/pow((Neptunex*Neptunex+Neptuney*Neptuney),1.5)
Neptune_v_x = Neptune_v_x_init-0.5*model_time*GM*Neptunex/pow((Neptunex*Neptunex+Neptuney*Neptuney),1.5)
Neptune_v_y = Neptune_v_y_init-0.5*model_time*GM*Neptuney/pow((Neptunex*Neptunex+Neptuney*Neptuney),1.5)
Neptunexholder = Neptunex
Neptuneyholder = Neptuney

screen.fill((0,0,0))
pygame.draw.circle(screen,(0,0,255),(Mercuryxpos,Mercuryypos),3) #Mercury
pygame.draw.circle(screen,(0,0,255),(Venusxpos,Venusypos),3) #Venus
pygame.draw.circle(screen,(0,0,255),(Earthxpos,Earthypos),3) #Earth
pygame.draw.circle(screen,(255,0,0),(Marsxpos,Marsypos),3) #Mars
pygame.draw.circle(screen,(129,89,19),(Jupiterxpos,Jupiterypos),3) #Jupiter
pygame.draw.circle(screen,(239,176,66),(Saturnxpos,Saturnypos),3) #Saturn
pygame.draw.circle(screen,(4,236,236),(Uranusxpos,Uranusypos),3) #Uranus
pygame.draw.circle(screen,(26,92,92),(Neptunexpos,Neptuneypos),3) #Neptune
pygame.draw.circle(screen,(246,255,0),(offset,offset),3) #sun 
pygame.display.update()

#time.clock()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    #Mercury
    if Mercuryyearcounter < 2 and Mercuryx > Mercuryxholder and Mercuryy < Mercuryyholder:
        Mercuryyearcounter += 1
    if not Mercuryx > Mercuryxholder and not Mercuryy < Mercuryyholder:
        Mercuryyearcounter = 0
    Mercuryloops += 1
    Mercuryloopsvar += 1
    if Mercuryyearcounter == 1:
        loopsvar = 0
        Mercuryyears += 1

    #Venus
    if Venusyearcounter < 2 and Venusx > Venusxholder and Venusy < Venusyholder:
        Venusyearcounter += 1
    if not Venusx > Venusxholder and not Venusy < Venusyholder:
        Venusyearcounter = 0
    Venusloops += 1
    Venusloopsvar += 1
    if Venusyearcounter == 1:
        loopsvar = 0
        Venusyears += 1

    #Earth
    if Earthyearcounter < 2 and Earthx > Earthxholder and Earthy < Earthyholder:
        Earthyearcounter += 1
    if not Earthx > Earthxholder and not Earthy < Earthyholder:
        Earthyearcounter = 0
    Earthloops += 1
    Earthloopsvar += 1
    if Earthyearcounter == 1:
        loopsvar = 0
        Earthyears += 1

    #Mars
    if Marsyearcounter < 2 and Marsx > Marsxholder and Marsy < Marsyholder:
        Marsyearcounter += 1
    if not Marsx > Marsxholder and not Marsy < Marsyholder:
        Marsyearcounter = 0
    Marsloops += 1
    Marsloopsvar += 1
    if Marsyearcounter == 1:
        loopsvar = 0
        Marsyears += 1

    #Jupiter
    if Jupiteryearcounter < 2 and Jupiterx > Jupiterxholder and Jupitery < Jupiteryholder:
        Jupiteryearcounter += 1
    if not Jupiterx > Jupiterxholder and not Jupitery < Jupiteryholder:
        Jupiteryearcounter = 0
    Jupiterloops += 1
    Jupiterloopsvar += 1
    if Jupiteryearcounter == 1:
        loopsvar = 0
        Jupiteryears += 1

    #Saturn
    if Saturnyearcounter < 2 and Saturnx > Saturnxholder and Saturny < Saturnyholder:
        Saturnyearcounter += 1
    if not Saturnx > Saturnxholder and not Saturny < Saturnyholder:
        Saturnyearcounter = 0
    Saturnloops += 1
    Saturnloopsvar += 1
    if Saturnyearcounter == 1:
        loopsvar = 0
        Saturnyears += 1

    #Uranus
    if Uranusyearcounter < 2 and Uranusx > Uranusxholder and Uranusy < Uranusyholder:
        Uranusyearcounter += 1
    if not Uranusx > Uranusxholder and not Uranusy < Uranusyholder:
        Uranusyearcounter = 0
    Uranusloops += 1
    Uranusloopsvar += 1
    if Uranusyearcounter == 1:
        loopsvar = 0
        Uranusyears += 1

    #Neptune
    if Neptuneyearcounter < 2 and Neptunex > Neptunexholder and Neptuney < Neptuneyholder:
        Neptuneyearcounter += 1
    if not Neptunex > Neptunexholder and not Neptuney < Neptuneyholder:
        Neptuneyearcounter = 0
    Neptuneloops += 1
    Neptuneloopsvar += 1
    if Neptuneyearcounter == 1:
        loopsvar = 0
        Neptuneyears += 1

    #zoom and speed
    #speed
    pressed_keys = pygame.key.get_pressed()
    speedvairable += 1     
    if speedvairable >= zoomandspeedcount:
        speedvairable = 0
        if pressed_keys[K_LEFT]:
            if not timevar == 4:
                timevar += 1
        if pressed_keys[K_RIGHT]:
            if not timevar == 0:
                timevar -= 1
        if timevar == 0:
                zoomandspeedcount = 200
                computertime = 0
        if timevar == 1:
                computertime = 0.01
                zoomandspeedcount = 100
        if timevar == 2:
                computertime = 0.02
                zoomandspeedcount = 50
        if timevar == 3:
                computertime = 0.03
                zoomandspeedcount = 25
        if timevar == 4:
                computertime = 0.04
                zoomandspeedcount = 12

    #zoom
    zoomvairable += 1
    if zoomvairable >= zoomandspeedcount:
        zoomvairable = 0
        vairable = 0
        if pressed_keys[K_UP]:
            scale /= 2
            scaledis *= 2
        if pressed_keys[K_DOWN]:
            scale *= 2
            scaledis /= 2       

    #planet position calculations
    Mercury_a_x = -GM*Mercuryx/pow((Mercuryx*Mercuryx+Mercuryy*Mercuryy),1.5)
    Mercury_a_y = -GM*Mercuryy/pow((Mercuryx*Mercuryx+Mercuryy*Mercuryy),1.5)
    Mercury_v_x = Mercury_v_x+Mercury_a_x*model_time
    Mercury_v_y = Mercury_v_y+Mercury_a_y*model_time
    Mercuryxholder = Mercuryx
    Mercuryyholder = Mercuryy
    Mercuryx = Mercuryx+Mercury_v_x*model_time
    Mercuryy = Mercuryy+Mercury_v_y*model_time
    Mercuryxp = ((Mercuryx / scale)+offset)
    Mercuryyp = ((Mercuryy / scale)+offset)
    Mercuryxpos = round(Mercuryxp)
    Mercuryypos = round(Mercuryyp)

    Venus_a_x = -GM*Venusx/pow((Venusx*Venusx+Venusy*Venusy),1.5)
    Venus_a_y = -GM*Venusy/pow((Venusx*Venusx+Venusy*Venusy),1.5)
    Venus_v_x = Venus_v_x+Venus_a_x*model_time
    Venus_v_y = Venus_v_y+Venus_a_y*model_time
    Venusxholder = Venusx
    Venusyholder = Venusy
    Venusx = Venusx+Venus_v_x*model_time
    Venusy = Venusy+Venus_v_y*model_time
    Venusxp = ((Venusx / scale)+offset)
    Venusyp = ((Venusy / scale)+offset)
    Venusxpos = round(Venusxp)
    Venusypos = round(Venusyp)

    Earth_a_x = -GM*Earthx/pow((Earthx*Earthx+Earthy*Earthy),1.5)
    Earth_a_y = -GM*Earthy/pow((Earthx*Earthx+Earthy*Earthy),1.5)
    Earth_v_x = Earth_v_x+Earth_a_x*model_time
    Earth_v_y = Earth_v_y+Earth_a_y*model_time
    Earthxholder = Earthx
    Earthyholder = Earthy
    Earthx = Earthx+Earth_v_x*model_time
    Earthy = Earthy+Earth_v_y*model_time
    Earthxp = ((Earthx / scale)+offset)
    Earthyp = ((Earthy / scale)+offset)
    Earthxpos = round(Earthxp)
    Earthypos = round(Earthyp)

    Mars_a_x = -GM*Marsx/pow((Marsx*Marsx+Marsy*Marsy),1.5)
    Mars_a_y = -GM*Marsy/pow((Marsx*Marsx+Marsy*Marsy),1.5)
    Mars_v_x = Mars_v_x+Mars_a_x*model_time
    Mars_v_y = Mars_v_y+Mars_a_y*model_time
    Marsxholder = Marsx
    Marsyholder = Marsy
    Marsx = Marsx+Mars_v_x*model_time
    Marsy = Marsy+Mars_v_y*model_time
    Marsxp = ((Marsx / scale)+offset)
    Marsyp = ((Marsy / scale)+offset)
    Marsxpos = round(Marsxp)
    Marsypos = round(Marsyp)

    Jupiter_a_x = -GM*Jupiterx/pow((Jupiterx*Jupiterx+Jupitery*Jupitery),1.5)
    Jupiter_a_y = -GM*Jupitery/pow((Jupiterx*Jupiterx+Jupitery*Jupitery),1.5)
    Jupiter_v_x = Jupiter_v_x+Jupiter_a_x*model_time
    Jupiter_v_y = Jupiter_v_y+Jupiter_a_y*model_time
    Jupiterxholder = Jupiterx
    Jupiteryholder = Jupitery
    Jupiterx = Jupiterx+Jupiter_v_x*model_time
    Jupitery = Jupitery+Jupiter_v_y*model_time
    Jupiterxp = ((Jupiterx / scale)+offset)
    Jupiteryp = ((Jupitery / scale)+offset)
    Jupiterxpos = round(Jupiterxp)
    Jupiterypos = round(Jupiteryp)

    Saturn_a_x = -GM*Saturnx/pow((Saturnx*Saturnx+Saturny*Saturny),1.5)
    Saturn_a_y = -GM*Saturny/pow((Saturnx*Saturnx+Saturny*Saturny),1.5)
    Saturn_v_x = Saturn_v_x+Saturn_a_x*model_time
    Saturn_v_y = Saturn_v_y+Saturn_a_y*model_time
    Saturnxholder = Saturnx
    Saturnyholder = Saturny
    Saturnx = Saturnx+Saturn_v_x*model_time
    Saturny = Saturny+Saturn_v_y*model_time
    Saturnxp = ((Saturnx / scale)+offset)
    Saturnyp = ((Saturny / scale)+offset)
    Saturnxpos = round(Saturnxp)
    Saturnypos = round(Saturnyp)

    Uranus_a_x = -GM*Uranusx/pow((Uranusx*Uranusx+Uranusy*Uranusy),1.5)
    Uranus_a_y = -GM*Uranusy/pow((Uranusx*Uranusx+Uranusy*Uranusy),1.5)
    Uranus_v_x = Uranus_v_x+Uranus_a_x*model_time
    Uranus_v_y = Uranus_v_y+Uranus_a_y*model_time
    Uranusxholder = Uranusx
    Uranusyholder = Uranusy
    Uranusx = Uranusx+Uranus_v_x*model_time
    Uranusy = Uranusy+Uranus_v_y*model_time
    Uranusxp = ((Uranusx / scale)+offset)
    Uranusyp = ((Uranusy / scale)+offset)
    Uranusxpos = round(Uranusxp)
    Uranusypos = round(Uranusyp)

    Neptune_a_x = -GM*Neptunex/pow((Neptunex*Neptunex+Neptuney*Neptuney),1.5)
    Neptune_a_y = -GM*Neptuney/pow((Neptunex*Neptunex+Neptuney*Neptuney),1.5)
    Neptune_v_x = Neptune_v_x+Neptune_a_x*model_time
    Neptune_v_y = Neptune_v_y+Neptune_a_y*model_time
    Neptunexholder = Neptunex
    Neptuneyholder = Neptuney
    Neptunex = Neptunex+Neptune_v_x*model_time
    Neptuney = Neptuney+Neptune_v_y*model_time
    Neptunexp = ((Neptunex / scale)+offset)
    Neptuneyp = ((Neptuney / scale)+offset)
    Neptunexpos = round(Neptunexp)
    Neptuneypos = round(Neptuneyp)


    #timedis = round(time.clock())
    print(Mercuryxpos, Mercuryypos, Venusxpos, Venusypos, Earthxpos, Earthypos, Marsxpos, Marsypos, Jupiterxpos, Jupiterypos, Saturnxpos, Saturnypos, Uranusxpos, Uranusypos, Neptunexpos, Neptuneypos)
   
    screen.fill((0,0,0))

    #Scale lines
    pygame.draw.line(screen,(255,255,255),(0,offset),(1000,offset),1)
    pygame.draw.line(screen,(255,255,255),(offset,0),(offset,1000),1)

    #Planets
    pygame.draw.circle(screen,(130,170,52),(Mercuryxpos,Mercuryypos),3) #Mercury
    pygame.draw.circle(screen,(135,102,39),(Venusxpos,Venusypos),3) #Venus
    pygame.draw.circle(screen,(0,0,255),(Earthxpos,Earthypos),3) #Earth
    pygame.draw.circle(screen,(255,0,0),(Marsxpos,Marsypos),3) #Mars
    pygame.draw.circle(screen,(129,89,19),(Jupiterxpos,Jupiterypos),3) #Jupiter
    pygame.draw.circle(screen,(239,176,66),(Saturnxpos,Saturnypos),3) #Saturn
    pygame.draw.circle(screen,(4,236,236),(Uranusxpos,Uranusypos),3) #Uranus
    pygame.draw.circle(screen,(26,92,92),(Neptunexpos,Neptuneypos),3) #Neptune 
    pygame.draw.circle(screen,(246,255,0),(offset,offset),3) #sun 

    #title
    screen.blit(font.render("Planetary Orbits By Jamie Holroyde",True,(255,255,255)),(400,10))

    #contents
    screen.blit(font.render("Zoom: "+str(scaledis)+"% (adjust using up and down arrows",True,(255,255,255)),(5,5))
    screen.blit(font.render("Delay: "+str(computertime)+" (adjust using left and right arrows)",True,(255,255,255)),(5,20))
    screen.blit(font.render("Scale is in E^12 meters",True,(255,255,255)),(5,35))
    screen.blit(font.render("Mercury Years: "+str(Mercuryyears),True,(130,170,52)),(5,50))
    screen.blit(font.render("Venus Years: "+str(Venusyears),True,(135,102,39)),(5,65))
    screen.blit(font.render("Earth Years: "+str(Earthyears),True,(0,0,255)),(5,80))
    screen.blit(font.render("Mars Years: "+str(Marsyears),True,(255,0,0)),(5,95))
    screen.blit(font.render("Jupiter Years: "+str(Jupiteryears),True,(129,89,19)),(5,110))
    screen.blit(font.render("Saturn Years: "+str(Saturnyears),True,(239,176,66)),(5,125))
    screen.blit(font.render("Uranus Years: "+str(Uranusyears),True,(4,236,236)),(5,140))
    screen.blit(font.render("Neptune Years: "+str(Neptuneyears),True,(246,255,0)),(5,155))

    #scale x
    screen.blit(font.render(("1"),True,(255,255,255)),((1E+12 / scale + offset),(offset)))
    screen.blit(font.render(("2"),True,(255,255,255)),((2E+12 / scale + offset),(offset)))
    screen.blit(font.render(("3"),True,(255,255,255)),((3E+12 / scale + offset),(offset)))
    screen.blit(font.render(("4"),True,(255,255,255)),((4E+12 / scale + offset),(offset)))
    screen.blit(font.render(("5"),True,(255,255,255)),((5E+12 / scale + offset),(offset)))
    screen.blit(font.render(("6"),True,(255,255,255)),((6E+12 / scale + offset),(offset)))
    screen.blit(font.render(("7"),True,(255,255,255)),((7E+12 / scale + offset),(offset)))
    screen.blit(font.render(("8"),True,(255,255,255)),((8E+12 / scale + offset),(offset)))
    screen.blit(font.render(("9"),True,(255,255,255)),((9E+12 / scale + offset),(offset)))
    screen.blit(font.render(("10"),True,(255,255,255)),((10E+12 / scale + offset),(offset)))
    screen.blit(font.render(("0"),True,(255,255,255)),((0E+12 / scale + offset),(offset)))
    screen.blit(font.render(("1"),True,(255,255,255)),((-1E+12 / scale + offset),(offset)))
    screen.blit(font.render(("2"),True,(255,255,255)),((-2E+12 / scale + offset),(offset)))
    screen.blit(font.render(("3"),True,(255,255,255)),((-3E+12 / scale + offset),(offset)))
    screen.blit(font.render(("4"),True,(255,255,255)),((-4E+12 / scale + offset),(offset)))
    screen.blit(font.render(("5"),True,(255,255,255)),((-5E+12 / scale + offset),(offset)))
    screen.blit(font.render(("6"),True,(255,255,255)),((-6E+12 / scale + offset),(offset)))
    screen.blit(font.render(("7"),True,(255,255,255)),((-7E+12 / scale + offset),(offset)))
    screen.blit(font.render(("8"),True,(255,255,255)),((-8E+12 / scale + offset),(offset)))
    screen.blit(font.render(("9"),True,(255,255,255)),((-9E+12 / scale + offset),(offset)))
    screen.blit(font.render(("10"),True,(255,255,255)),((-10E+12 / scale + offset),(offset)))

    #scale y
    screen.blit(font.render(("1"),True,(255,255,255)),((offset),(1E+12 / scale + offset)))
    screen.blit(font.render(("2"),True,(255,255,255)),((offset),(2E+12 / scale + offset)))
    screen.blit(font.render(("3"),True,(255,255,255)),((offset),(3E+12 / scale + offset)))
    screen.blit(font.render(("4"),True,(255,255,255)),((offset),(4E+12 / scale + offset)))
    screen.blit(font.render(("5"),True,(255,255,255)),((offset),(5E+12 / scale + offset)))
    screen.blit(font.render(("6"),True,(255,255,255)),((offset),(6E+12 / scale + offset)))
    screen.blit(font.render(("7"),True,(255,255,255)),((offset),(7E+12 / scale + offset)))
    screen.blit(font.render(("8"),True,(255,255,255)),((offset),(8E+12 / scale + offset)))
    screen.blit(font.render(("9"),True,(255,255,255)),((offset),(9E+12 / scale + offset)))
    screen.blit(font.render(("10"),True,(255,255,255)),((offset),(10E+12 / scale + offset)))
    screen.blit(font.render(("0"),True,(255,255,255)),((offset),(0E+12 / scale + offset)))
    screen.blit(font.render(("1"),True,(255,255,255)),((offset),(-1E+12 / scale + offset)))
    screen.blit(font.render(("2"),True,(255,255,255)),(((offset),-2E+12 / scale + offset)))
    screen.blit(font.render(("3"),True,(255,255,255)),((offset),(-3E+12 / scale + offset)))
    screen.blit(font.render(("4"),True,(255,255,255)),((offset),(-4E+12 / scale + offset)))
    screen.blit(font.render(("5"),True,(255,255,255)),((offset),(-5E+12 / scale + offset)))
    screen.blit(font.render(("6"),True,(255,255,255)),((offset),(-6E+12 / scale + offset)))
    screen.blit(font.render(("7"),True,(255,255,255)),((offset),(-7E+12 / scale + offset)))
    screen.blit(font.render(("8"),True,(255,255,255)),(((offset),-8E+12 / scale + offset)))
    screen.blit(font.render(("9"),True,(255,255,255)),((offset),(-9E+12 / scale + offset)))
    screen.blit(font.render(("10"),True,(255,255,255)),((offset),(-10E+12 / scale + offset)))

    pygame.display.update()
    time.sleep(computertime)