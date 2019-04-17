import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math
import numpy
import random

colors = (
    (1,0.5,0),
    (0.5,0,0.5),
    (0.5,0,0.5),
    (1,0.5,0),
    (1,0.5,0),
    (1,0,1),
    (1,1,1),
    (0,0,0),
    (0.5,0.5,0.5),
    (1,0.5,0.3),
    (1,0,0),
    (0,0.3,0.6),
)

class Stars:
    vert = [
    [-1,0,-1],
    [1,0,-1],
    [-1,2,-1],
    [-1,0,1],
    [1,0,1],
    [1,2,-1],
    [-1,2,1],
    [1,2,1],
    ]

    vert2 = [
    [-1,0,-1],
    [1,0,-1],
    [-1,2,-1],
    [-1,0,1],
    [1,0,1],
    [1,2,-1],
    [-1,2,1],
    [1,2,1],
    ]

    edges = [
    [0,1],
    [0,2],
    [0,3],
    [1,4],
    [1,5],
    [2,5],
    [2,6],
    [3,4],
    [3,6],
    [7,6],
    [7,4],
    [7,5],
    ]

    surfaces = [
    [0,1,5,2],
    [0,2,6,3],
    [0,1,4,3],
    [2,5,7,6],
    [1,4,7,5],
    [3,4,7,6],
    ]


    def __init__(self, x_init, y_init, z_init):
        self.x_init = x_init
        self.y_init = y_init
        self.z_init = z_init
        self.edges = HostileCubes.edges
        self.surfaces = HostileCubes.surfaces
        self.center = [self.x_init, self.y_init, self.z_init]
        self.vert2 = list(numpy.multiply(numpy.array(HostileCubes.vert), 0.1))
        self.vert = list(map(lambda vertex: (vertex[0] + self.x_init, vertex[1] + self.y_init, vertex[2] + self.z_init), self.vert2))

    def fill(self):
        glBegin(GL_QUADS)
        for surface in self.surfaces:
            for vertex in surface:
                glColor3fv((1,1,1))
                glVertex3fv(self.vert[vertex])

        glEnd()

    def move(self, x, y, z):
        self.vert = list(map(lambda vertex: (vertex[0] + x, vertex[1] + y, vertex[2] + z), self.vert))
        self.center = numpy.array(self.vert).sum(axis=0)/8
        self.fill()

class HostileCubes:
    vert = [
    [-1,0,-1],
    [1,0,-1],
    [-1,2,-1],
    [-1,0,1],
    [1,0,1],
    [1,2,-1],
    [-1,2,1],
    [1,2,1],
    ]

    vert2 = [
    [-1,0,-1],
    [1,0,-1],
    [-1,2,-1],
    [-1,0,1],
    [1,0,1],
    [1,2,-1],
    [-1,2,1],
    [1,2,1],
    ]

    edges = [
    [0,1],
    [0,2],
    [0,3],
    [1,4],
    [1,5],
    [2,5],
    [2,6],
    [3,4],
    [3,6],
    [7,6],
    [7,4],
    [7,5],
    ]

    surfaces = [
    [0,1,5,2],
    [0,2,6,3],
    [0,1,4,3],
    [2,5,7,6],
    [1,4,7,5],
    [3,4,7,6],
    ]


    def __init__(self, x_init):
        self.x_init = x_init
        self.y_init = 0
        self.z_init = -80
        self.edges = HostileCubes.edges
        self.surfaces = HostileCubes.surfaces
        self.center = [self.x_init, self.y_init, self.z_init]
        self.vert2 = list(numpy.multiply(numpy.array(HostileCubes.vert), 0.5))
        self.vert = list(map(lambda vertex: (vertex[0] + self.x_init, vertex[1] + self.y_init, vertex[2] + self.z_init), self.vert2))
        self.position = glGetDoublev(GL_MODELVIEW_MATRIX)
        self.x = self.position[3][0]
        self.y = self.position[3][1]
        self.z = self.position[3][2]

    def draw(self):
        glLineWidth(3)
        glBegin(GL_LINES)
        for edge in self.edges:
            for vertex in edge:
                glColor3f(0.5,0,0.5)
                glVertex3fv(self.vert[vertex])
        glEnd()

    def fill(self):
        glBegin(GL_QUADS)
        for surface in self.surfaces:
            for vertex in surface:
                glColor3fv((0,0,0))
                glVertex3fv(self.vert[vertex])

        glEnd()
        self.draw()


    def move(self, x, y, z):
        self.vert = list(map(lambda vertex: (vertex[0] + x, vertex[1] + y, vertex[2] + z), self.vert))
        self.center = numpy.array(self.vert).sum(axis=0)/8
        self.position = glGetDoublev(GL_MODELVIEW_MATRIX)
        self.x = self.position[3][0]
        self.y = self.position[3][1]
        self.z = self.position[3][2]
        self.fill()
class Ground:
    ground_vertices = [
    [-3.5,0,10],
    [3.5,0,10],
    [3.5,0,-200],
    [-3.5,0,-200],
    ]
    ground_side = [[0,1,2,3]]

    def __init__(self):
        self.ground_vertices = Ground.ground_vertices
        self.color = None

    def draw(self):
        glBegin(GL_QUADS)
        for surface in self.ground_side:
            x = 0
            for vertex in surface:
                x += 1
                glColor3fv(colors[x])
                glVertex3fv(self.ground_vertices[vertex])
        glEnd()

class Cube:
    prev_vert = [
    [-1,0,-1],
    [1,0,-1],
    [-1,2,-1],
    [-1,0,1],
    [1,0,1],
    [1,2,-1],
    [-1,2,1],
    [1,2,1],
    ]

    vert = [
    [-1,0,-1],
    [1,0,-1],
    [-1,2,-1],
    [-1,0,1],
    [1,0,1],
    [1,2,-1],
    [-1,2,1],
    [1,2,1],
    ]

    edges = [
    [0,1],
    [0,2],
    [0,3],
    [1,4],
    [1,5],
    [2,5],
    [2,6],
    [3,4],
    [3,6],
    [7,6],
    [7,4],
    [7,5],
    ]

    surfaces = [
    [0,1,5,2],
    [0,2,6,3],
    [0,1,4,3],
    [2,5,7,6],
    [1,4,7,5],
    [3,4,7,6],
    ]


    def __init__(self, mul=1):
        self.edges = Cube.edges
        self.surfaces = Cube.surfaces
        self.vert = list(numpy.multiply(numpy.array(Cube.vert), mul))
        self.prev_vert = None
        self.center = numpy.array(self.vert).sum(axis=0)/8
        self.position = glGetDoublev(GL_MODELVIEW_MATRIX)
        self.x = self.position[3][0]
        self.y = self.position[3][1]
        self.z = self.position[3][2]
    def draw(self):
        glLineWidth(3)
        glBegin(GL_LINES)
        for edge in self.edges:
            for vertex in edge:
                glColor3f(1,0.2,0)
                glVertex3fv(self.vert[vertex])
        glEnd()
    def fill(self):
        glBegin(GL_QUADS)
        for surface in self.surfaces:
            for vertex in surface:
                glColor3f(1,0.4,0)
                glVertex3fv(self.vert[vertex])

        glEnd()
        self.draw()

    def move(self, x, y, z):
        self.prev_vert = self.vert
        self.vert = list(map(lambda vertex: (vertex[0] + x, vertex[1] + y, vertex[2] + z), self.vert))
        self.center = numpy.array(self.vert).sum(axis=0)/8
        if self.center[0] < -3.1:
            self.vert = self.prev_vert
        if self.center[0] > 3.1:
            self.vert = self.prev_vert

    def jump(self, dy):
        self.move(0,dy,0)

def spawner(h_cubes, cube):
    return h_cubes.append(cube)

def starspawner(starlist, star):
    return starlist.append(star)

def Zoom(z):
    glTranslatef(0, 0, z)

def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    score = 0
    gluPerspective(45, (display[0]/display[1]), 0.1, 130)
    glTranslatef(0,-2.5, 0)
    position = glGetDoublev(GL_MODELVIEW_MATRIX)
    glEnable(GL_DEPTH_TEST)

    starlist = []
    for i in range(25):
        rx = random.randrange(-50, 50, 10)
        ry = random.randrange(-50, 50, 10)
        rz = random.randrange(-130, 0, 10)
        if ry <= 0 and ry >= -5:
            ry += 5
        starspawner(starlist, Stars(rx, ry, rz))

    z_index = 1
    c = Cube(0.5)
    g = Ground()
    q = 20
    time = 5
    h_cubes = []
    dt = time
    vel = 0.15
    dy = 0
    accel = 0.005
    maxvel = 0.15
    velh = 0.3
    clock = pygame.time.Clock()
    jumping = False
    kuk = True

    while kuk:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameover()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_h:
                    kuk = False
                    gameover()


        #glRotatef(math.pi/2,3,3,3)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            c.move(-vel, 0, 0)
        if keys[pygame.K_RIGHT]:
            c.move(vel,0,0)
        if keys[pygame.K_s]:
            c.move(0,0,-vel)
        if keys[pygame.K_w]:
            c.move(0,0,vel)
        if keys[pygame.K_SPACE] and jumping == False:
            jumping = True
            dy = 0.25

        if jumping:
            c.jump(dy)
            dy -= 0.01
            if c.center[1] <= 0.5:
                c.center[1] = 0.5
                dy = 0
                jumping = False

        if dt <= 0:
            r = random.randrange(-3, 3, 1)
            spawner(h_cubes, HostileCubes(r))
            dt = time

        if(z_index >= 0.05):
            Zoom(-z_index)
            z_index *= 0.9

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        for i, cube in enumerate(h_cubes):
            cube.move(0,0,velh)

        for i, cube in enumerate(h_cubes):
            if cube.center[2] > 10:
                h_cubes.pop(i)
                score += 1
                print(score, velh)
                if score%q == 0:
                    q*=2
                    velh *= 1.2
                    time *= 0.8
            if abs(c.center[0]-cube.center[0]) < 1 and abs(c.center[2]-cube.center[2]) < 1 and abs(c.center[1]-cube.center[1] < 1):
                c.fill()
                print(c.center)
                kuk = False
                gameover()

        for i, star in enumerate(starlist):
            star.move(0,0,velh)

        for i, star in enumerate(starlist):
            if star.center[2] > 10:
                starlist.pop(i)
                rx = random.randrange(-50, 50, 10)
                ry = random.randrange(-50, 50, 10)
                rz = random.randrange(-130, 0, 10)
                if ry <= 0 and ry >= -5:
                    ry += 5
                starspawner(starlist, Stars(rx,ry,rz))

        print(clock)
        position = glGetDoublev(GL_MODELVIEW_MATRIX)
        c.fill()
        g.draw()
        dt -= 0.1
        pygame.display.flip()

def gameover():
    pygame.quit()
    quit()

main()
